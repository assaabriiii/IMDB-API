from typing import Union
from funcs import *
from fastapi import FastAPI
from urllib.parse import unquote


app = FastAPI()


@app.get("/movies/name:{star}")
def api_movies_from_star(star: str,):
    name = unquote(star)
    result = all_movies_from_star(name)
    return {"name": result}


@app.get("/movies/random")
def api_random_movie():
    result = random_movie()
    return {"movie": result}

@app.get("/movies/year:{year}")
def api_movies_from_year(year: str,):
    year = unquote(year)
    result = movies_from_year(year)
    return {"movies": result}


@app.get("/movies/year/before/year:{year}")
def api_movies_before_year(year: str,):
    year = unquote(year)
    result = movies_from_year_before(year)
    return {"movies": result}


@app.get("/movies/year/after/year:{year}")
def api_movies_before_year(year: str,):
    year = unquote(year)
    result = movies_from_year_after(year)
    return {"movies": result}
