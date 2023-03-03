# import sys

# sys.setrecursionlimit(1500)

class Movie:
    
    def __init__(self, title):
        self.title = title
        self.reviews = []
        self.reviewers = []

    def get_title(self):
        print("Retrieving title:")
        return self._title

    # @title.setter
    def set_title(self, title):
        if type(title) == str and 0 < len(title):
            self._title = title
        else:
            print("The movie title should be at least 1 character")
            raise Exception("The movie title should be at least 1 character")
        
    title = property(get_title, set_title)
        
    def get_reviewers(self):   
        return self.reviewers
    
    def reviewers(self, reviewers=[]):
        if type(reviewers) == []:
            self.reviewers = reviewers

    def average_rating(self):
        return sum(self.reviews) / len(self.reviews)

    # @classmethod
    # def highest_rated(cls):

    #     highest_rated = 0
    #     for review in reviews:
    #         if review >= highest_rated:
    #             highest_rated = review
    #             return highest_rated.title

