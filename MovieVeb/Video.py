class VideoBase(object):
    """视频基础类提供视频的基本属性"""
    def __init__(self,movie_title,movie_storyline):
        self.title = movie_title
        self.storyline = movie_storyline
