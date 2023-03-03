class Review:
    
    def __init__(self, viewer, movie, rating, username):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        self.username = username

    # rating property goes here!
    def get_rating(self):
        print("Retrieving rating:")
        return self._rating

    # @title.setter
    def set_rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5 :
            self._rating = rating
        else:
            print("The rating must be between 0 and 5")
            raise Exception("The rating must be between 0 and 5")
        
    rating = property(get_rating, set_rating)        

    # viewer property goes here!
    def get_username(self):
        print("Retrieving username:")
        return self._username

    def set_username(self, username):
        if hasattr(username, username == str):
            self.username = username
        else:
            print("Username must be a unique")
            raise Exception("Username must be a unique")
        
    username = property(get_username, set_username)     


    # movie property goes here!
