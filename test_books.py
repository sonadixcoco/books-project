import unittest
from books import search_by_isbn

class TestBooks(unittest.TestCase):
    def test_isbn(self):
        books = [{"title": "Книга", "author": "Автор", "isbn": "123"}]
        self.assertEqual(len(search_by_isbn(books, "123")), 1)

if __name__ == '__main__':
    unittest.main()