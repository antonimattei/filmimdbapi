from flask import Flask
from controllers.movie_controller import movie_bp
import os

app = Flask(__name__)

# Registre o Blueprint (roteamento de filmes)
app.register_blueprint(movie_bp, url_prefix='/movies')  # Ex: /movies/list

@app.route("/")
def home():
    return "Página inicial do site!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 1000)), debug=False)