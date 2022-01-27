from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/add", methods=['GET'])
def new_book():
    return render_template("/books/add.html")

@books_blueprint.route("/books", methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.add_book(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')