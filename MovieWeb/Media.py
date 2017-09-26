import Video
import webbrowser


class Movie(Video.VideoBase):
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        Video.VideoBase.__init__(self,movie_title,movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
     
    def ShowTrailer(self):
        webbrowser.open(self.trailer_youtube_url)


