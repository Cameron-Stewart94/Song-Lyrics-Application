import os
import re
import requests
from bs4 import BeautifulSoup
from gtts import gTTS


class Lyrics:
# Class to generate song lyrics from user input

    def __init__(self, artist_name, song_name):
        # Function initialises lyrics class
        self.artist_name = artist_name
        self.song_name = song_name
        self.song_lyrics = ''
        self.song_description = ''

    def __repr__(self):
        # Function returns chosen song name and artist name when printed
        return 'You chose {song}, by {artist}...'.format(song=self.song_name, artist=self.artist_name)

    def fetch_data(self):
        #Function fetches song information from the web

        def format_song_to_url(artist_name, song_name):
            # Function takes user song choice and formats strings to genius url
            artist_name = artist_name.lower()
            artist_name = artist_name[0].upper() + artist_name[1:]
            artist_name = artist_name.split()
            artist_name = '-'.join(artist_name)
            # Takes artist input and formats string as needed in genius url

            song_name = song_name.split()
            song_name = '-'.join(song_name)
            # Takes song input and formats as needed in genius url

            title = artist_name + '-' + song_name + '-lyrics'
            website = 'http://genius.com/{title}'.format(title = title)
            # Creates full web address using formated user inputs
            return website

        def fetch_web(website):
            source = requests.get(website).text
            soup = BeautifulSoup(source, 'lxml')
            html_lyrics = soup.find('div', class_ = 'lyrics').text
            song_info = soup.find('div', class_ = 'header_with_cover_art-primary_info').text
            return {'Lyrics' : html_lyrics, 'Song Information' : song_info}

        def remove_whitespace(string):
            #Funtion removes blank lines from scraped song information
            song_info_lst = string.split('\n')
            song_info_lst = [i for i in song_info_lst if len(i) > 0]
            return song_info_lst

        def save_song_data(web_scrape, song_info):
            self.song_lyrics += web_scrape['Lyrics']
            self.song_lyrics = self.song_lyrics.lstrip()
            self.song_name = song_info[0]
            self.artist_name = song_info[1]
            self.song_description += '\n'.join(song_info[2 : ])
            return {'song' : song_info[0], 'artist' : song_info[1], 'description' : '\n'.join(song_info[2 : ]) }


        song_url = format_song_to_url(self.artist_name, self.song_name)
        web_scrape = fetch_web(song_url)
        song_info = remove_whitespace(web_scrape['Song Information'])
        save_data = save_song_data(web_scrape, song_info)
        # Calls four fetch data functions and stores results in song_lyrics and song_description variables

        return save_data

    
