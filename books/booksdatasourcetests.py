'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books.csv')
 
    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_tiny_length(self):
        tiny_data_source = BooksDataSource('tiny_books.csv')
        tiny_books_none = tiny_data_source.books('wajwndjandjasjfuif')
        tiny_books_all = tiny_data_source.books()
        tiny_authors_none = tiny_data_source.authors('Aaron Bronstone')
        tiny_authors_all = tiny_data_source.authors()
        tiny_years_none = tiny_data_source.books_between_years(3000,3001)
        tiny_years_all = tiny_data_source.books_between_years(0000,3000)
        self.assertTrue(len(tiny_books_none)==0 and len(tiny_authors_none)==0 and len(tiny_years_none)==0)
        self.assertTrue(len(tiny_books_all)==5 and len(tiny_authors_all)==5 and len(tiny_years_all)==5)

    def test_book_titles(self, name, order):
        books = self.data_source.books(name)
        for b in books:
            self.assertTrue(b.title.find(name)!=-1)
        if order in ['-t','--title','']:
            self.assertEqual(books.sort(key=title),books)
        if order in ['-y','--year']:
            self.assertEqual(books.sort(key=publication_year),books)
        self.assertEqual(books(name),books(name.upper()))
        self.assertEqual(books(name),books(name.lower()))
            
    def test_authors(self, name):
        authors = self.booksdatasource.authors(name)
        for b in books:
            self.assertTrue(b.author.find(name)!=-1)
        self.assertEqual(authors(name),authors(name.upper()))
        self.assertEqual(authors(name),authors(name.lower()))
        self.assertEqual(authors.sort(key=name.substring(find(' '))),authors)


    def test_years(self, start, end):
        self.assertTrue(start<=end)
        years = self.booksdatasource.books_between_years('1930','1940')
        self.assertEqual(years, [And_Then_There_Were_None,Murder_on_the_Orient_Express,The_Code_of_the_Woosters])
        self.assertEqual(years.sort(key=publication_year),years)

        

if __name__ == '__main__':
    unittest.main()

