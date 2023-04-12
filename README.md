# API Documentation

This API provides access to a movie database and allows users to retrieve information on movies based on various criteria.

## Endpoints

### /movies/name:{star}

This endpoint retrieves all movies featuring a particular star.

**Method:** GET

**Parameters:**
- `star`: the name of the star (string)

**Example:**

```json
GET /movies/name:Tom%20Cruise HTTP/1.1
Host: example.com

Response:
{
"name": ["Top Gun", "Mission: Impossible", "Minority Report"]
}
```


### /movies/year:{year}

This endpoint retrieves all movies released in a particular year.

**Method:** GET

**Parameters:**
- `year`: the year (string)

**Example:**

```json
GET /movies/year:1999 HTTP/1.1
Host: example.com

Response:
{
"movies": ["The Matrix", "The Sixth Sense", "American Beauty"]
}
```


### /movies/year/before/year:{year}

This endpoint retrieves all movies released before a particular year.

**Method:** GET

**Parameters:**
- `year`: the year (string)

**Example:**

```json 
GET /movies/year/before/year:1990 HTTP/1.1
Host: example.com

Response:
{
"movies": ["Back to the Future", "The Terminator", "The Princess Bride"]
}
```


### /movies/year/after/year:{year}

This endpoint retrieves all movies released after a particular year.

**Method:** GET

**Parameters:**
- `year`: the year (string)

**Example:**

```json
GET /movies/year/after/year:2010 HTTP/1.1
Host: example.com

Response:
{
"movies": ["Inception", "The Social Network", "Toy Story 3"]
}
```


## Dependencies

This API has the following dependencies:
- `funcs`: A module containing functions for retrieving movie data
- `fastapi`: A Python web framework for building APIs
- `urllib.parse`: A module for parsing URLs and performing URL encoding/decoding.
