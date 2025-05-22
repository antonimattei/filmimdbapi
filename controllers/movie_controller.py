from flask import Blueprint, render_template, request
from models.movie_model import search_movies, get_movie_by_id

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/')
def index():
    title = request.args.get('title')
    movies = search_movies(title) if title else []
    return render_template('index.html', movies=movies, search_title=title)

@movie_bp.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)