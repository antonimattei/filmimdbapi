from flask import Blueprint, render_template, request
from models.movie_model import search_movies, get_movie_by_id  # Adicione esta importação

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/')
def index():
    title = request.args.get('title')
    page = int(request.args.get('page', 1))
    
    if title:
        result = search_movies(title, page=page)
        return render_template(
            'index.html',
            movies=result["movies"],
            pagination=result["pagination"],
            search_title=title
        )
    return render_template('index.html', movies=[], search_title=None)

# Adicione esta nova rota
@movie_bp.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = get_movie_by_id(movie_id)
    if not movie:
        return render_template('404.html'), 404
    return render_template('movie_details.html', movie=movie)