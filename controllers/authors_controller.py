from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import author_repository

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("authors/index.html", all_authors = authors)

@authors_blueprint.route("/<id>/books", methods=['GET'])
def books(id):
    books = book_repository.select_books_by_author(id)
    return render_template("authors/books.html", all_books = books)