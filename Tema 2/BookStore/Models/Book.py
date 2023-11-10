class Book:
    title: str
    author: str
    isbn: str
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def obj_dict(obj):
        return obj.__dict__
    
