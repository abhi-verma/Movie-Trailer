# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 15:55:56 2017

@author: abhin
"""

import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 'A Story of a boy and his toys that come to life.', 'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 'https://www.youtube.com/watch?v=ZZv1vki4ou4')

avatar = media.Movie('Avatar', 'A marine on an alien.', 'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg', 'https://www.youtube.com/watch?v=5PSNL1qE6VY')

rush = media.Movie('Rush', 'Enthralling F1 rivalry between two racing legends.', 'https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg', 'https://www.youtube.com/watch?v=lzNbGH1oZJc')

shawshank_redemption = media.Movie('Shawshank Redemption', 'Story of a convict''s hope.', 'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg', 'https://www.youtube.com/watch?v=NmzuHjWmXOc')

pursuit_of_happyness = media.Movie('The Pursuit Of Happyness', 'Rags to riches story.', 'https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg', 'https://www.youtube.com/watch?v=SYg7RRYKWGw')

dark_knight = media.Movie('The Dark Knight', 'Batman and Joker in a Nolan masterclass.', 'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg', 'https://www.youtube.com/watch?v=EXeTwQWrcwY')

movies = [toy_story, avatar, rush, shawshank_redemption, pursuit_of_happyness, dark_knight]
fresh_tomatoes.open_movies_page(movies)