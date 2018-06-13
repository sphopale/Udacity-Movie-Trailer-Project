class Movie():
    """ Creates the movie abstarct class, which will be used to create
        movie instances.

      Attributes:
        movie_title: This is the title of the movie (String).
        movie_storyline : This is the movie overview (String).
        poster_image (str): This is path to the image (String).
        trailer_youtube (str): This is path to the youtube movie link(String).
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
