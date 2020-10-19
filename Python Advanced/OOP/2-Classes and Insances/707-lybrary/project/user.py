class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self,author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author]
            library.rented_books[self.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        
        for username, data in library.rented_books.items():
            for b_n , days in data.items():
                if b_n == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name)


    00:49:36
