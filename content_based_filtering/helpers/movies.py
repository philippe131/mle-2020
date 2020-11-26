
# Stock all the movies
class Movies():

    def __init__(self, movies):
        self.movies = movies

    # Get id of a movie
    def get_movie_id(self, title, year=None):
        
        res = self.movies[self.movies['title'] == title]
        if year:
            res = res[res['year'] == year]

        if len(res) > 1:
            print("Ambiguous: found")
            print({res['title']}, {res['year']})
        elif len(res) == 0:
            print('not found')
        else:
            return res.index[0]

    # Get title of a movie
    def get_movie_name(self, index):
        return self.movies.iloc[index].title

    # Get year of a movie
    def get_movie_year(self, index):
        return self.movies.iloc[index].year
