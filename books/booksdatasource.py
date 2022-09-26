#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv
import sys

#print('Arguments',str(sys.argv))
#data = BooksDataSource('books.csv')

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None,books=[]):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        books=[]

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title, publication_year, authors):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = int(publication_year)
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        self.books_csv_file_name = books_csv_file_name
        #print('Hellar')
        self.bookList=[]
        self.authorList = []
        with open (books_csv_file_name) as csvfile:
            reader = csv.reader(csvfile,delimiter=',',quotechar='"')
            for row in reader:
                #print(row)
                book = Book(row[0],int(row[1]),row[2])
                self.bookList.append(Book(row[0],row[1],row[2]))
                #print('Book title: ',book.title)
                #print('Book year: ',book.publication_year)
                #print('Book author: ',book.authors)
                splitDescription = row[2].split('(',1)
                splitYear = splitDescription[1].split('-',1)
                #print(splitYear[0],' ',splitYear[1])
                death=None
                if splitYear[1][0]!=')':
                    #length = len(splitYear[1])
                    death=splitYear[1][0:-1]

                givenName = splitDescription[0].split(' ',1)
                author=Author(givenName[1],givenName[0],splitYear[0],death)
                self.authorList.append(author)
                #print('FIRST: ',author.given_name,' LAST: ',author.surname,' BIRTH: ',author.birth_year,' DEATH: ',author.death_year)
        #print(self.bookList)
        pass

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        results=[]
        for author in self.authorList:
            fullName = author.given_name + ' ' + author.surname
            if search_text.lower() in fullName.lower() and author not in results:
                results.append(author)
        #for author in results:
            #print(author.given_name,' ',author.surname)        
        results.sort(key=lambda author: author.surname + author.given_name)

        print('---------------------------------------')
        for author in results:
            print(author.given_name,' ',author.surname)
        return results

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        #print('books test')
        #print(self.bookList)
        results = []

        for book in self.bookList:
            if search_text.lower() in book.title.lower():
                results.append(book)
        if sort_by == 'year':
            results.sort(key=lambda book: book.publication_year)
        else:
            results.sort(key=lambda book: book.publication_year)
            results.sort(key=lambda book: book.title)
        print('RESULTS:')
        for book in results:
            print(book.title)

        
        return results

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        results = []

        for book in self.bookList:

            if book.publication_year>=start_year and book.publication_year<=end_year:
                results.append(book)
        results.sort(key=lambda book: book.title)
        results.sort(key=lambda book: book.publication_year)
        print('RESULTS:')
        for book in results:
            print(book.title)

        
        return results

#print('Hello from bottom')
data = BooksDataSource('books.csv')
#user = input('BOOKS user input: ')
#args = user.split(' ',1)
#data.books('the','title')
#data.authors('')
#data.books('the','year')
data.books_between_years(1800,1900)





