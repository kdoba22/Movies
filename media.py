import webbrowser

""" creates a Movie class that takes 4 arguments, movie_title, movie_storyline, poster_image, and trailer_youtube """
class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
