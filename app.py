from flask import Flask
from controllers.movie_controller import movie_bp, index  # Importe index
import os

app = Flask(__name__)

app.register_blueprint(movie_bp, url_prefix='/movies')

# Use a função index do movie_controller para a rota /
app.add_url_rule("/movies", view_func=index)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 1000)), debug=False)