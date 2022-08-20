from flask import Flask
from sqlalchemy import create_engine

import os
app = Flask(__name__)

mysql_uri = os.environ["MYSQL_URI"]
postgres_uri = os.environ["POSTGRES_URI"]


def get_movies(db_uri):
    """
    Retrieves all movies from the database.
    """
    movies = []

    engine = create_engine(db_uri).connect()

    for row in engine.execute("SELECT * FROM movie ORDER by rating DESC"):
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
    This method is called when opening the webapp.
    """

    # Mysql
    movies_mysql = get_movies(mysql_uri)
    movies_mysql_li = render_movie_li(movies_mysql)

    # Postgres
    movies_postgres = get_movies(postgres_uri)
    movies_postgres_li = render_movie_li(movies_postgres)

    # Read the index.html and add the movies rendered to it.
    return open('index.html').read() % (movies_mysql_li, movies_postgres_li)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)