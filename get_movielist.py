import csv


def get_fav_movies():
    """ Get the favorite movie list from the csv file 
    
    This function returns the details of the favorite movies 
    fro the csv file
    
    Returns:
       array of the favorite movie
    """
    csv_file = csv.DictReader(open('my_favourite_movies.csv', 'r'))
    Movie_Db = []
    for row in csv_file:
        Movie_Db.append(row)
    return Movie_Db
