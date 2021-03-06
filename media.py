# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 15:54:46 2017

@author: abhin
"""
import webbrowser

class Movie(object):
    """
    Class to store movies related information
    """
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)