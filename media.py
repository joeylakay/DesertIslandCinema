import webbrowser


class Movie(object):

    """Template movie class for my movie favorites website.

        Attributes:
            movie_title(str): Title of the movie instance.
            movie_storyline(str):  Brief summary of movie instance.
            poster_image(str): url for poster image of movie instance.
            trailer_youtube_url(str): url for movie instance trailer.
            movie_genre(str): Genre of the movie instance.
            release_year(int): Year the movie was released.
            running_time(int):  Total running time of the movie.

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url, movie_genre, release_year,
                 running_time):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        self.genre = movie_genre
        self.relyear = release_year
        self.total_running_time = running_time

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
