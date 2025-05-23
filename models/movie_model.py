from imdb import IMDb
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
import math

ia = IMDb()
executor = ThreadPoolExecutor(max_workers=5)  # Pool de threads

@lru_cache(maxsize=100)
def search_movies(title: str, page: int = 1, per_page: int = 5):
    try:
        results = ia.search_movie(title)
        total_results = len(results)
        total_pages = math.ceil(total_results / per_page)

        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        page_results = results[start_idx:end_idx]

        futures = [executor.submit(_process_movie, movie) for movie in page_results]
        movies = [future.result() for future in futures]

        pagination = generate_pagination_links(page, total_pages)
        
        return {
            "movies": movies,
            "pagination": {
                **pagination,
                "current_page": page,
                "total_pages": total_pages
            }
        }
    except Exception as e:
        print(f"Erro na busca: {e}")
        return {"movies": [], "pagination": {}}

def _process_movie(movie):
    """Processa dados de um filme individual"""
    ia.update(movie, info=['main'])
    return {
        'id': movie.movieID,
        'title': movie.get('title', 'N/A'),
        'year': movie.get('year', 'N/A'),
        'rating': movie.get('rating', 'Sem nota')
    }
    
def generate_pagination_links(current_page, total_pages):
    """Gera a estrutura de links de paginação"""
    pagination = {
        'first': None,
        'previous': None,
        'pages': [],
        'next': None,
        'last': None,
        'has_gap_before': False,
        'has_gap_after': False
    }

    if total_pages > 1:
        pagination['first'] = 1
        if current_page > 1:
            pagination['previous'] = current_page - 1

        # Intervalo de 5 páginas ao redor da atual
        start_page = max(1, current_page - 2)
        end_page = min(total_pages, current_page + 2)

        # Ajusta para mostrar sempre 5 páginas quando possível
        if end_page - start_page < 4:
            if current_page < 3:
                end_page = min(total_pages, 5)
            else:
                start_page = max(1, total_pages - 4)

        pagination['pages'] = list(range(start_page, end_page + 1))

        # Verifica se há páginas antes/depois do intervalo
        pagination['has_gap_before'] = start_page > 2
        pagination['has_gap_after'] = end_page < total_pages - 1

        if current_page < total_pages:
            pagination['next'] = current_page + 1
        pagination['last'] = total_pages

    return pagination
def get_movie_by_id(movie_id):
    """Obtém detalhes completos de um filme pelo ID"""
    try:
        movie = ia.get_movie(movie_id)
        ia.update(movie, info=['main', 'vote details'])
        
        return {
            'id': movie.movieID,
            'title': movie.get('title', 'N/A'),
            'year': movie.get('year', 'N/A'),
            'rating': movie.get('rating', 'Not rated'),
            'genres': ', '.join(movie.get('genres', [])),
            'directors': ', '.join([d['name'] for d in movie.get('directors', [])]),
            'plot': movie.get('plot outline', 'No plot available'),
            'cover_url': movie.get('cover url')
        }
    except Exception as e:
        print(f"Error fetching movie {movie_id}: {e}")
        return None