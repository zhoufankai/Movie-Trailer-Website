

class Movie():
    """ The class provids storing movie information 
    Args:        
        title(str): movie trailer's title.
        poster_image_url(str): the poster image's url.
        trailer_youtube_url(str): the trailer's url on youtube.
    Attributes:
        title(str): movie trailer's title.
        poster_image_url(str): the poster image's url.
        trailer_youtube_url(str): the trailer's url on youtube.
    """
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
