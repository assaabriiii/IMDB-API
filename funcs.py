import sqlite3 


def all_movies_from_star(name:str):
    conn = sqlite3.connect('movies/movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE LOWER(name) = LOWER(?)))",(name,))
    result = cursor.fetchall()
    result = tuple_to_string(result)
    conn.close()
    return result


def random_movie():
    conn = sqlite3.connect('movies/movies.db')
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM movies ORDER BY RANDOM() LIMIT 1') 
    result = cursor.fetchone()
    result = fix_random_movie(result)
    conn.close()
    return result


def movies_from_year(year:int):
    conn = sqlite3.connect('movies/movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies WHERE year = (?)', (year,))
    result = cursor.fetchall()
    result = fix_movies_list(result)
    conn.close()
    return result


def movies_from_year_before(year:int):
    conn = sqlite3.connect('movies/movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies WHERE year <= (?)', (year,))
    result = cursor.fetchall()
    result = tuple_to_string(result)
    conn.close()    
    return result


def movies_from_year_after(year:int):
    conn = sqlite3.connect('movies/movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies WHERE year >= (?)', (year,))
    result = cursor.fetchall()
    result = tuple_to_string(result)
    conn.close()
    return result

def tuple_to_string(result):
    res = []
    for i in result:
        res.append(str(i).strip("()").strip(',').strip("'"))
    return res


def fix_random_movie(result):
    return [result[1], result[2]]


def fix_movies_list(result): 
    res = []
    for i in result: 
        res.append(i[1])
    return res
        
        
