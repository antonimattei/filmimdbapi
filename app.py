from flask import Flask, render_template, request, redirect, url_for
import requests
from imdb import IMDb

app = Flask(__name__)
ia = IMDb()

@app.route('/')
def index():
    title = request.args.get('title')
    movies = []
    if title:
        movies = ia.search_movie(title)
    return render_template('index.html', movies=movies, search_title=title)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = ia.get_movie(movie_id)
    return render_template('movie_details.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
