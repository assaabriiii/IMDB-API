import sqlite3 


conn = sqlite3.connect('movies/movies.db')
cursor = conn.cursor()


def close_connection():
    conn.close()


def all_movies_from_star(name:str):
    cursor.execute("SELECT title FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE LOWER(name) = LOWER(?)))",(name,))
    result = cursor.fetchall()
    close_connection()
    return result


def random_movie(): 
    cursor.execute('SELECT * FROM movies ORDER BY RANDOM() LIMIT 1') 
    result = cursor.fetchone()
    conn.close()
    close_connection()
    return result


def movies_from_year(year:int):
    cursor.execute('SELECT * FROM movies WHERE year = (?)', (year,))
    result = cursor.fetchall()
    return result


def movies_from_year_before(year:int):
    cursor.execute('SELECT * FROM movies WHERE year <= (?)', (year,))
    result = cursor.fetchall()
    return result


def movies_from_year_after(year:int):
    cursor.execute('SELECT * FROM movies WHERE year >= (?)', (year,))
    result = cursor.fetchall()
    return result

    