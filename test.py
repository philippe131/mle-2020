import unittest
import pandas as pd

class TestStringMethods(unittest.TestCase):
    
    # Test if data/users.csv is empty
    def test_readUser(self):
        user = pd.read_csv("data/users.csv")
        isempty = user.empty
        self.assertFalse(isempty)

    # Test if data/ratings.csv is empty
    def test_readRating(self):
        rating = pd.read_csv("data/ratings.csv")
        isempty = rating.empty
        self.assertFalse(isempty)

    # Test if data/movies.csv is empty
    def test_readMovie(self):
        movie = pd.read_csv("data/movies.csv")
        isempty = movie.empty
        self.assertFalse(isempty)

if __name__ == '__main__':
    unittest.main()