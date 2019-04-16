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

    def print_lyrics(self):
        return self.song_lyrics

    def print_song_information(self):
        return(self.song_description)

    def write_to_txt_file(self):
        # Funtion writes song lyrics to txt file and saves on PC

        txt_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'song_lyrics.txt')
        # Creates path to save .txt file(c://Ellie/Desktop/songs)

        with open(txt_file_location, 'w', encoding= 'utf-8') as text_file:
            text_file.write(self.song_lyrics)
            # Writes lyrics to a text file

        return

    def write_to_mp3_file(self):
        # Function writes song lyrics to mp3 file and saves on PC
        mp3_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'song_lyrics.mp3')
        # Creates path to save .txt file(c://Ellie/Desktop/songs)

        remove_verse_headings = self.song_lyrics
        remove_verse_headings = re.sub("\[[^]]+\]", "", remove_verse_headings)
        # Uses re to remove words in [] brackets - this removes verse heading so tts doesn't read them

        tts = gTTS(remove_verse_headings)
        tts.save(mp3_file_location)
        # Creates mp3 file of song

        return

    def print_lyrics_backwards(self):
        return self.song_lyrics[::-1]

    def most_used_word(self):
        remove_verse_headings = self.song_lyrics
        remove_verse_headings = re.sub("\[[^]]+\]", "", remove_verse_headings)
        title_case = remove_verse_headings.title()

        punctuation = '?!,.()"[]'

        for i in punctuation:
            title_case = title_case.replace(i, '')

        lyrics_lst = title_case.split()
        lyrics_set = set(lyrics_lst)


        count_dict = {}

        for word in lyrics_set:
            count = 0
            for matching_word in lyrics_lst:
                if word == matching_word:
                    count += 1
            count_dict[word] = count

        sorted_dic = sorted(count_dict.items(), key = lambda t: t[1], reverse=True)

        return 'The Most used word is {word}, which was used {times} times'.format(word=sorted_dic[0][0], times=sorted_dic[0][1])
