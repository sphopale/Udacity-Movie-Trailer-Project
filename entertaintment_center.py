import urllib.request
import media
import json
import fresh_tomatoes
import get_movielist

API_KEY = "601bdfb5c7983bb533d2698c3fdd02c7"


def create_movies_details():
    """ Creates the movies array to pass to the Fresh Tomatoes website.

    This function gets the details of the movies listed in the fav_movie_list
    from the The Movie Database API and returns the details.
    
    Return:
        movies: An array of Movie instances.
    """
    fav_movie_list = get_movielist.get_fav_movies()
    movies = []
    for x in range(len(fav_movie_list)):
        movie = get_json_details(fav_movie_list[x]['Name'])
        movie = media.Movie(movie["title"], movie["overview"],
                                          get_poster_url() +
                                          movie["poster_path"],
                                          get_movie_trailer(movie["id"]))
        movies.insert(x, movie)
    fresh_tomatoes.open_movies_page(movies)


def get_json_details(fav_movie):
    """ Get the json details from The Movie Database
    
    This function gets the details based on the favourite movies in the list 
    from  The Movie database 

    Args: Takes favourite movies list

    Returns:
       array of movie details
    """
    jsonurl = urllib.request.urlopen("https://api.themoviedb.org/3/search"
                                     "/movie?api_key=" + API_KEY +
                                     "&query="+"%20".join(fav_movie.split()))
    api = json.loads(jsonurl.read())
    for i in range(api["total_results"]):
        if (api["results"][i]["title"] == fav_movie):
            return api["results"][i]
        else:
            return "null"


def get_movie_trailer(movie_id):
    """ Get the movie trailer link from the movie database
    
    This function returns the details of the link to the movie trailer 
    database
    
    Args: movie_id from The Movie Database

    Returns:
       link to the movie trailer
    """
    jsonurl = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" +
                                     str(movie_id) + "/videos?api_key=" +
                                     API_KEY)
    api_trailer = json.loads(jsonurl.read())
    if (len(api_trailer["results"]) != 0):
        key = api_trailer["results"][0]["key"]
        you_tube_path = "https://www.youtube.com/watch?v="+key
        return you_tube_path
    else:
        return "null"


def get_poster_url():
    """ Get the movie poster base url from the movie database
    
    This function returns the details of the base url details to 
    the movie poster  database
    
    
    Returns:
       base url for the poster url
    """
    config_url = "https://api.themoviedb.org/3/configuration?api_key="+API_KEY
    results = urllib.request.urlopen(config_url)
    api_image = json.loads(results.read())
    url = api_image["images"]["secure_base_url"] +\
        api_image["images"]["poster_sizes"][4]
    return url
create_movies_details()
