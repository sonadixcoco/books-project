import json

def load_books(filename="books.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_book(books, title, author, isbn):
    books.append({"title": title, "author": author, "isbn": isbn})#kfvjekr
    return books

def find_by_author(books, author_name):
    return [b for b in books if author_name.lower() in b["author"].lower()]

def export_books(books, filename="export.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for b in books:
            f.write(f"{b['title']} | {b['author']} | {b['isbn']}\n")

def search_by_isbn(books, isbn):
    isbn = isbn.strip()
    return [b for b in books if b["isbn"] == isbn]

MAX_BOOKS = 1000