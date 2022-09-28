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
        #print('UNIQUE AUTHOR TEST')
        self.assertTrue(len(authors) == 1)
        #print('AUTHORS[0]:||',authors[0].given_name,'||',authors[0].surname,'||',authors[0].birth_year,'||',type(authors[0].death_year))
        terry = Author('Pratchett', 'Terry')
        #print('TERRY:',terry.given_name,'||',terry.surname,'||',type(terry.birth_year),'||',type(terry.death_year))
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
    def test_book_titles(self):
        name = 'the'
        #books = self.data_source.books(name)
        defaultTest = self.data_source.books('the')
        titleTest = self.data_source.books('the','title')
        yearTest = self.data_source.books('the','year')
        for book in defaultTest:
            self.assertTrue('the' in book.title.lower())
            
    def test_authors(self):
        authors = self.data_source.authors()
        #print('test_authors_TESTING:')
        for i in range(len(authors)-1):
            #print('Current author: ',authors[i].surname,' ',authors[i].given_name)
            #print('Next author: ',authors[i+1].surname,' ',authors[i+1].given_name)
            self.assertTrue(authors[i].surname<=authors[i+1].surname or authors[i].given_name<=authors[i+1].surname)   

        name='lL'
        authorsLower = self.data_source.authors('lL')
        authorsUpper = self.data_source.authors('LL')
        counter = 0
        for author in authorsLower:
            self.assertEqual(author,authorsUpper[counter])
            counter+=1


    def test_years(self):
        #self.assertTrue(start<=end)
        years = self.data_source.books_between_years(1800,1900)
        correctTitles = ['Pride and Prejudice','Sense and Sensibility','Emma','Jane Eyre','Omoo','Wuthering Heights','The Tenant of Wildfell Hall','Moby Dick','Villette']
        counter = 0
        for year in years:
            self.assertEqual(year.title, correctTitles[counter])
            counter+=1

        

if __name__ == '__main__':
    unittest.main()

