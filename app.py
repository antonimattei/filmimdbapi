from flask import Flask, render_template
from controllers.movie_controller import movie_bp  # Importe o Blueprint
import os

app = Flask(__name__)

# Registre o Blueprint (roteamento de filmes)
app.register_blueprint(movie_bp, url_prefix='/movies')  # Ex: /movies/list

@app.route("/")
def home():
     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 1000)), debug=False)