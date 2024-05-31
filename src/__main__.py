import os

from src import *
from src import azlyrics, csv_parser


def scrape():
    """
    Processes the main function of the scraper.
    :return: All AZLyrics scraped.
    """
    for artist_letter in AZ_LYRICS_ARTIST_LETTER_LIST:
        # Logging stuff
        print(f'[1] Processing [{artist_letter}] letter...')

        # Iterates over all artists with the given letter.
        print('[1] Scraping artists URLs...')
        artist_url_list = azlyrics.get_artist_url_list(artist_letter)
        print(f'[1] ---> {len(artist_url_list)} artists found with letter [{artist_letter}]')
        for artist_name, artist_url in artist_url_list:
            
            print(f'[2] Scraping song URLs for {artist_name}...')
            song_url_list = azlyrics.get_song_url_list(artist_url)
            print(f'[2] ---> {len(song_url_list)} songs found with artist [{artist_name}]')
            for song_name, song_url in song_url_list:
                print(f'[3] Scraping lyrics for song: [{song_name}]')
                if not csv_parser.exists_song(artist_letter, artist_url, song_url):
                    song_lyrics = azlyrics.get_song_lyrics(song_url)
                    lines = song_lyrics.split('\n')
                    line_lengths = [len(l) for l in lines]
                    print(f'[3] ---> [{song_name}] {len(lines)} lines and {len(song_lyrics)} characters')
                    print(f'[3] ---> [{song_name}] longest line: {lines[line_lengths.index(max(line_lengths))]}')
                    csv_parser.append_to_csv(artist_name, artist_url, song_name, song_url, song_lyrics, artist_letter)


if __name__ == '__main__':
    iteration = 1
    while True:
        print(f'Starting iteration number {iteration}...')
        scrape()
        iteration += 1

