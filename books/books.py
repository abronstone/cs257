#book.py: parses command line arguments

from booksdatasource import Author, Book, BooksDataSource
import sys
#Displays the usage message and exits the program
def print_usage():
    print('usage: python3 books.py [-h] [-u] [-ts \'search_text\' \'sorting_order\'] [-as \'search_text\'] [-yrs year1 year2]')
    exit()

#Displays an error message, refers to the usage command line argument, and exits the program
def print_error():
    print('Invalid command line syntax, please refer to usage statement for proper syntax: [python3 books.py -u]')
    exit()

data_source = BooksDataSource('books.csv')
arguments = sys.argv
counter = 0

#Prints the usage statement if the only input is 'python3 books.py'
if(len(arguments)==1):
    print_usage()

#takes in first argument
first = arguments[1].lower()

if first in ['-h','--help']:
    #Help
    #Opens 'books_usage.txt' as a file and prints the contents
    f = open('books_usage.txt','r')
    content = f.read()
    print(content)
elif first in ['-u','--usage']:
    #USAGE
    #Calls to 'print_usage()'
    print_usage()
elif first in ['-ts','--titlesearch']:
    #BOOK/TITLE SEARCH
    """
    Calls to 'BookDataSource.books()' to obtain and print a list of books, including the title, publication year and authors.
    The input to 'BookDataSource.books()' varies depending on the number of arguments after '-ts' or '--titlesearch':

    -0 ARGS: displays all books
    -1 ARG: displays all books whose titles contain the argumented string
    -2 ARGS: displays all books whose titles contain the argumented string, sorted in order by the second argument

    If none of the arguments follow the usage syntax, the 'print_error()' method is called
    """
    search_text = None
    order_by = None
    if len(arguments) > 4:
        print_error()
    if len(arguments) > 2:
        search_text = arguments[2]
        if len(arguments) == 4:
            order_by = arguments[3]
            if(order_by not in ['title','year']):
                print_error()
                exit()
    books = data_source.books(search_text,order_by)
    for book in books:
        print(book.title,'(',book.publication_year,') by ',book.authors)
elif first in ['-as','--authorsearch']:
    #AUTHOR SEARCH
    '''
    Calls to 'BookDataSource.authors()' to obtain and print a list of authors, along with their birth/death years
    The input to 'BookDataSource.authors()' varies depending on the number of arguments after '-as' or '--authorsearch':

    -0 ARGS: displays all authors
    -1 ARG: displays all authors whose given name or surname contain the argumented text
    
    If none of the arguments follow the usage syntax, the 'print_error()' method is called
    '''
    search_text = None
    if(len(arguments)<=3):
        if(len(arguments)==3):
            search_text = arguments[2]
    else:
        print_error()
    authors = data_source.authors(search_text)
    for author in authors:
        print(author.surname,', ',author.given_name,' (',author.birth_year,'-',author.death_year,')')
elif first in ['-ys','--yearsearch']:
    #BOOKS BETWEEN YEARS SEARCH
    '''
    Calls to 'BookDataSource.books_between_years()' to obtain and print a list of books that were published between two specific dates
    The input to 'BookDataSource.authors()' varies depending on the number of arguments after '-as' or '--authorsearch':

    -0 ARGS: displays all authors
    -1 ARG: displays all authors whose given name or surname contain the argumented text
    
    If none of the arguments follow the usage syntax, the 'print_error()' method is called
    '''
    year1 = None
    year2 = None
    if len(arguments) > 4:
        print_error()
    if len(arguments)>2:
        year1 = arguments[2].strip()
        if year1.isnumeric():
            year1 = int(year1)
        else:
            print_error()
    if len(arguments)==4:
        year2 = arguments[3].strip()
        if year2.isnumeric():
            year2 = int(year2)
        else:
            print_error()
    print('START: ',year1)
    print('END: ',year2)
    books_between_years = data_source.books_between_years(year1,year2)
    for book in books_between_years:
        print(book.title,'(',book.publication_year,') by ',book.authors)
else:
    print_error()