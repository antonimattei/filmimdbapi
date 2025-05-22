from imdb import IMDb

ia = IMDb()

def search_movies(title):
    return ia.search_movie(title)

def get_movie_by_id(movie_id):
    return ia.get_movie(movie_id)