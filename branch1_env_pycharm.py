import requests
import os
import pandas as pd


class API_queries:
    api_key = os.environ['movie_db_api_key']

    def get(self, url):
        '''
        :param url(str): link to API call
        :return: data from API (dict)
        '''
        x = requests.get(url)
        return x.json()

    def search(self, title):
        '''
        :param title(str): name of movie to search for
        :return: list of dictionaries, each dictionary is a movie
        '''
        url = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={title}"
        results = self.get(url)['results']
        return results

    def get_details(self, movie_id):
        '''
        movie_id(str): unique ID
        return FIGURE OUT WHAT ITS OUTPUTTING
        '''
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&language=en-US"
        details = self.get(url)
        return details

    def get_genres(self):
        '''
        gets list of all the genres available in the API
        genres: [{'id': int, 'name': str}]
        '''
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language=en-US"
        genres = self.get(url)['genres']
        return g


class Movie(API_queries):
    def __init__(self, movie_id=None):
        self.movie_id: int = movie_id

    def ask_year(self):
        '''
        get year of movie release
        :return: year (int)
        '''
        year = input("What year was the movie originally released? ")
        if len(str(year)) != 4:
            raise TypeError("should be a 4 digit year")
        return year

    def ask_title(self):
        '''
        search and find a new movie to add to database
        :return: None
        '''

        title = input("Please share the name of a movie you like: ")
        def search_loop(title):
            results = API_queries().search(title)
            # more than one movie result
            if len(results) > 1:
                year = self.ask_year()
                for r in results:
                    if r['release_date'][:4] == year:
                        self.movie_id = r['id']
                        break

            # no movie results
            elif not results:
                print(f'No results for {title}')
                new_title = input("Try searching for another movie or type 'exit' to quit program: ")
                if new_title == 'exit':
                    return
                else:
                    search_loop(new_title)

            # only one search result
            else:
                verify = input("Is this the movie you were looking for? (y/n) ")
                if verify == 'y':
                    self.movie_id = results[0]['id']
                else:
                    self.ask_title()
            return

        search_loop(title)

    def update(self):
        '''
        find and replace feature of movie
        :return:
        '''
        # TODO

    def add(self):
        # add a new movie and it's features to the db

        details = API_queries().get_details(self.movie_id)
        new_data = {'movie_id': self.movie_id,
                    'budget': details['budget'],
                    'genres': details['genres'],
                    'original_language': details['original_language'],
                    'release_date': details['release_date'][:4],
                    'revenue': details['revenue'],
                    'runtime': details['runtime'],
                    'spoken_languages': details['spoken_languages'],
                    'title': details['title']
        }

        # Make data frame of above data
        df = pd.DataFrame(new_data)

        # append data frame to CSV file
        df.to_csv('movie_directory.csv', index=False, header=False)

    # def drive(self):

a = API_queries()
m = Movie()
