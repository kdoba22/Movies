import webbrowser


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ creates a Movie class that takes 4 arguments, movie_title,
            movie_storyline, poster_image, and trailer_youtube """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ opens the selected movie trailer """
        webbrowser.open(self.trailer_youtube_url)
