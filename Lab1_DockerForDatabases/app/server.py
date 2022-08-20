from flask import Flask
from sqlalchemy import create_engine

import os
app = Flask(__name__)

mysql_uri = os.environ["MYSQL_URI"]
# postgres_uri = os.environ["POSTGRES_URI"]


def get_movies():
    """
    Retrieves all movies from the database.
    """
    movies = []

    engine = create_engine(mysql_uri).connect()

    for row in engine.execute("SELECT * FROM movies ORDER by rating DESC"):
        movies.append({"name": row[0], "rating": row[1]})

    return movies


def render_movie_li(movies):
    """
    Creates a HTML list (<li>) of all movies.
    """
    html = ""

    for movie in movies:
        html = html + """
            <li class="list-group-item">
                <span class="badge">%s
                    <span class="glyphicon glyphicon-star"></span>
                </span>
                %s
            </li>
        """ % (movie['rating'], movie['name'])

    return html


@app.route('/')
def index():
    """
    This method is called upon opening the webapp.
    """
    movies = get_movies()
    movies_li = render_movie_li(movies)

    # Read the index.html and add the movies_li to it.
    return open('index.html').read() % (movies_li)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)