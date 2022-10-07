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
    '''
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
    '''
    def test_titles_order(self):
        #name = 'the'
        #books = self.data_source.books(name)
        defaultTest = self.data_source.books('oo')
        titleTest = self.data_source.books('oo','title')
        yearTest = self.data_source.books('oo','year')
        for book in defaultTest:
            self.assertTrue('oo' in book.title.lower())
        
        correct_title_list = [Book('Good Omens',1990,'Neil Gaiman (1960-) and Terry Pratchett (1948-2015)'),Book('Omoo',1847,'Herman Melville (1819-1891)'),Book('Schoolgirls',1994,'Peggy Orenstein (1961-)'),Book('The Code of the Woosters',1938,'Pelham Grenville Wodehouse (1881-1975)')]
        correct_year_list = [Book('Omoo',1847,'Herman Melville (1819-1891)'),Book('The Code of the Woosters',1938,'Pelham Grenville Wodehouse (1881-1975)'),Book('Good Omens',1990,'Neil Gaiman (1960-) and Terry Pratchett (1948-2015)'),Book('Schoolgirls',1994,'Peggy Orenstein (1961-)')]
        self.assertEqual(yearTest,correct_year_list)
        self.assertEqual(defaultTest,correct_title_list)

    def test_all_titles(self):
        tester = self.data_source.books()
        self.assertTrue(len(tester)==41)
    
    def test_no_titles(self):
        wrong = self.data_source.books("Charlotte Thomson's 'Head Full of Dreams'")
        self.assertEqual(wrong,[])
            
    def test_authors(self):
        #TEST 1: All author names
        authors = self.data_source.authors()
        for i in range(len(authors)-1):
            self.assertTrue(authors[i].surname<=authors[i+1].surname or authors[i].given_name<=authors[i+1].surname)   
        
        #TEST 2: Case sensitivity
    def test_author_case(self):
        name='lL'
        authorsLower = self.data_source.authors('lL')
        authorsUpper = self.data_source.authors('LL')
        counter = 0
        for author in authorsLower:
            self.assertEqual(author,authorsUpper[counter])
            counter+=1

        #TEST 3: Ordered by surname
    def test_author_surname(self):
        author_test = self.data_source.authors('st')
        correct_author_test = [Author('Austen','Jane',1775,1817),Author('Christie','Agatha',1890,1976),Author('McMaster Bujold','Lois',1949),Author('Orenstein','Peggy',1961),Author('Sterne','Laurence',1713,1768)]
        self.assertEqual(author_test,correct_author_test)

    def test_no_authors(self):
        wrong = self.data_source.books('Bronstone')
        self.assertEqual(wrong,[])

    def test_years_order(self):
        #TEST 1: Ordered by year
        years = self.data_source.books_between_years(1800,1900)
        correctTitles = ['Pride and Prejudice','Sense and Sensibility','Emma','Jane Eyre','Omoo','Wuthering Heights','The Tenant of Wildfell Hall','Moby Dick','Villette']
        counter = 0
        for year in years:
            self.assertEqual(year.title, correctTitles[counter])
            counter+=1
        
        #TEST 2: end>start year
    def test_years_input(self):
        wrong_years = self.data_source.books_between_years(1900,1899)
        self.assertEqual(wrong_years,[])

    def test_all_years(self):
        all_years_books = self.data_source.books_between_years()
        self.assertTrue(len(all_years_books),41)

        

if __name__ == '__main__':
    unittest.main()

