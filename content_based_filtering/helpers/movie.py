# Stock one movie, not used
class Movie():
    
    def __init__(self, title, index=None, year=None):
        if index:
            self.index = index
        if year:
            self.year = year
        self.title = title
        