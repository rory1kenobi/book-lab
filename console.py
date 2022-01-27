import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("George", "Lucus")
author_repository.add_author(author1)
author2 = Author("John", "Tolkien")
author_repository.add_author(author2)
author3 = Author("Clive", "Lewis")
author_repository.add_author(author3)

author_repository.select_all()

book_1 = Book("A New Hope", author1, True)
book_repository.add_book(book_1)
book_2 = Book("Lord Of The Rings", author2, True)
book_repository.add_book(book_2)
book_3 = Book("The Chronicles of Narnia", author3)
book_repository.add_book(book_3)

pdb.set_trace()