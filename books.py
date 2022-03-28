class Book():

    favourites = []
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def is_long(self): #method to check if book is too voluminous
        if self.pages > 100:
            return True
        else:
            return False
    def __str__(self): #manage when object is passed to print
        return f"{self.title} has {self.pages} pages \n"
    
    def __eq__(self, other): #overides default equality to suit this use case
        if self.title == other.title and self.pages == other.pages:
            return True
        else:
            return False
    __hash__ = None
    def __repr__(self): #helps make list of items return str
        return self.__str__()

