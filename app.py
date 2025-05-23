from flask import Flask
from controllers.movie_controller import movie_bp

app = Flask(__name__)
app.register_blueprint(movie_bp)

if __name__ == '__main__':
    app.run(debug=True)