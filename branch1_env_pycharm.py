import requests
import os

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
    def __init__(self):
        self.movie_id: int = None

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
        # title = title.replace(' ', '+')

        results = API_queries().search(title)
        if len(results) > 1:
            year = self.ask_year()
            for r in results:
                if r['release_date'][:4] == year:
                    self.movie_id = r['id']
        else:
            self.movie_id = results[0]['id']
        return

    def update_dp(self):
        '''

        :return:
        '''
        # TODO

m = API_queries().get_details('12444')
# print(type(os.environ['movie_db_api_key']))
# print(os.environ['movie_db_api_key'])
print(m)

# m = Movie()
# m.ask_title()
# id_ = m.movie_id
# print(id_)

