from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def add_book(book):
    sql = "INSERT INTO books (title, author, completed, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.full_name, book.completed, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author.full_name, result['completed'], result['id'])
        return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['completed'], row['id'])
        books.append(book)
    return books

def select_books_by_author(id):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['completed'], row['id'])
        books.append(book)
    return books


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)