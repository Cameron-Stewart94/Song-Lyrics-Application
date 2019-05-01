import os
import re
import requests
from bs4 import BeautifulSoup

class Lyrics:
# Class to generate song lyrics from user inputs, using the BeautifulSoup library

    def __init__(self, artist_name, song_name):
        # Function initialises lyrics class with four song information variables
        self.artist_name = artist_name
        self.song_name = song_name
        self.song_lyrics = ''
        self.song_description = ''

    def __repr__(self):
        # Function returns chosen song name and artist name when printed
        return 'You chose {song}, by {artist}...'.format(song=self.song_name, artist=self.artist_name)

    def fetch_data(self):
        # Function scrapes song information from the web using a series of sub-functions

        def format_song_to_url(artist_name, song_name):
            # Function takes user artist choice and song choice and formats strings to fit genius url style
            artist_name = artist_name.lower()
            artist_name = artist_name[0].upper() + artist_name[1:]
            artist_name = artist_name.split()
            artist_name = '-'.join(artist_name)
            # The four steps take artist input and formats string as needed in genius url

            song_name = song_name.split()
            song_name = '-'.join(song_name)
            # These two steps take song input and formats as needed in genius url

            song_title = artist_name + '-' + song_name + '-lyrics'
            song_url = 'http://genius.com/{song_title}'.format(song_title = song_title)
            # Creates, and returns full song_url using formated user inputs
            return song_url

        def web_scraper(website):
            # Function uses BeautifulSoup Library with lxml parser to fetch song information from genius.com
            source = requests.get(website).text
            soup = BeautifulSoup(source, 'lxml')

            html_lyrics = soup.find('div', class_ = 'lyrics').text
            # Finds song lyrics in html code and stores them as text
            song_information = soup.find('div', class_ = 'header_with_cover_art-primary_info').text
            # Finds information about the song, i.e title, and stores as text
            return {'Lyrics' : html_lyrics, 'Song Information' : song_information}

        def remove_whitespace(song_information):
            # Funtion removes blank lines from scraped song information
            song_information_lst = song_information.split('\n')
            song_information_lst = [i for i in song_information_lst if len(i) > 0]
            # Comprehension stores artist, name of song, and description in a list
            return song_information_lst

        def save_song_data(web_scrape, song_information):
            # Function saves song information data to corresponding variable in the class
            self.song_lyrics += web_scrape['Lyrics']
            self.song_lyrics = self.song_lyrics.lstrip()
            self.song_name = song_information[0]
            self.artist_name = song_information[1]
            # Class's song_name and artist_name vairables are overridden with correctly fomratted strings
            self.song_description += '\n'.join(song_information[2 : ])

        song_url = format_song_to_url(self.artist_name, self.song_name)
        web_scrape = web_scraper(song_url)
        song_information = remove_whitespace(web_scrape['Song Information'])
        save_data = save_song_data(web_scrape, song_information)
        # Calls four fetch data functions and stores results in corresponding variables

        return save_data
