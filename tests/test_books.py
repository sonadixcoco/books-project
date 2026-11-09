import unittest
from books import add_book, find_by_author, search_by_isbn

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.books = [{"title": "Книга 1", "author": "Иванов", "isbn": "111"}]

    def test_add_book(self):
        result = add_book(self.books, "Новая", "Петров", "222")
        self.assertEqual(len(result), 2)

    def test_find_by_author_exact(self):
        result = find_by_author(self.books, "Иванов")
        self.assertEqual(len(result), 1)

    
    def test_author_search_ignores_case(self):
        result = find_by_author(self.books, "иванов")
        self.assertEqual(len(result), 1)

    def test_find_by_author_not_found(self):
        result = find_by_author(self.books, "Сидоров")
        self.assertEqual(len(result), 0)

    def test_search_by_isbn(self):
        result = search_by_isbn(self.books, "111")
        self.assertEqual(len(result), 1)

    def test_search_by_isbn_with_spaces(self):
        result = search_by_isbn(self.books, " 111 ")
        self.assertEqual(len(result), 1)

    def test_search_by_isbn_not_found(self):
        result = search_by_isbn(self.books, "999")
        self.assertEqual(len(result), 0)

    def test_books_initially_empty(self):
        self.books = []
        self.assertEqual(len(self.books), 0)

    def test_add_multiple_books(self):
        add_book(self.books, "Книга 2", "Сидоров", "333")
        add_book(self.books, "Книга 3", "Петров", "444")
        self.assertEqual(len(self.books), 3)

    def test_search_empty_author(self):
        result = find_by_author(self.books, "")
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()