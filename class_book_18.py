class Book: 
    def __init__(self, title: str, author: str, pages: int): 
        self.title = title 
        self.author = author 
        self.pages = pages 
 
    def __str__(self) -> str: 
        return f"'{self.title}' by {self.author}, {self.pages} pages" 
book = Book("1910", "Rabindranath Tagore", 63) 
print(book)