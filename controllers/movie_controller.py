from flask import Blueprint, render_template, request
from models.movie_model import search_movies

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