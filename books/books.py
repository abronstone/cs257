'''
    books.py
    Aaron Bronstone and Tom Pree, September 30th 2020
'''

from booksdatasource import Author, Book, BooksDataSource
import sys
import argparse
#Displays the usage message and exits the program
def print_usage():
    print('USAGE: python3 books.py [-h] [-u] [-ts \'search_text\' \'sorting_order\'] [-as \'search_text\'] [-yrs year1 year2]')
    print()
    print()
    exit()

#Displays an error message, refers to the usage command line argument, and exits the program
def print_error():
    print('Invalid command line syntax, please refer to usage statement for proper syntax: [python3 books.py -u]')
    print()
    print()
    exit()

def print_space():
    print()
    print()
data_source = BooksDataSource('books.csv')

parser = argparse.ArgumentParser()
parser.add_argument("-t","--titles", help="Displays book titles that contain the inputted search text, case insensitive",type=str)
parser.add_argument("-a","--authors",help="Displays authors whose names contain the inputted search texg, case insensitive",type=str)
parser.add_argument("-y","--years",nargs=2,action='store',help="Displays book titles whose publication dates fall within the range of the inputted years, inclusive",type=str,default=None)
parser.add_argument("-s","--sort",help="FOR TITLE SEARCH",type=str)
args=parser.parse_args()
#print(args.titles)
#print(args.authors)
#print(args.years)
#print(type(args.years))
print('-------------------------------------------------------')
print_space()
if args.titles:
    search_text = args.titles
    order_by = None
    if args.sort:
        order_by=args.sort.lower()
        #print(order_by)
        if order_by!='title' and order_by!='year':
            raise Exception('Invalid sort type: '+order_by)
    books = data_source.books(search_text,order_by)
    for book in books:
        print('-',book.title,'(',book.publication_year,') by ',book.authors)
elif args.authors:
    search_text = args.authors
    authors=data_source.authors(search_text)
    for author in authors:
        print('-',author.surname,', ',author.given_name,' (',author.birth_year,'-',author.death_year,')')
elif args.years:
    year1 = None
    year2 = None
    if args.years[0].isnumeric():
        year1=int(args.years[0])
    if args.years[1].isnumeric():
        year2=int(args.years[1])
    books_between_years = data_source.books_between_years(year1,year2)
    for book in books_between_years:
        print('-',book.title,'(',book.publication_year,') by ',book.authors)
else:
    search_text=None
    order_by=None
    if args.sort:
        order_by=args.sort
    all=data_source.books(search_text,order_by)
    for book in all:
        print('-',book.title,'(',book.publication_year,') by ',book.authors)
#print('Here')
print_space()
print('-------------------------------------------------------')
exit()


##################################################################################################################################################################
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
        if search_text in ['-y','--year']:
            search_text = None
            order_by = arguments[2]
        if len(arguments) == 4:
            order_by = arguments[3]
            if(order_by not in ['-t','--title','-y','--year']):
                print_error()
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
            year1=None
    if len(arguments)==4:
        year2 = arguments[3].strip()
        if year2.isnumeric():
            year2 = int(year2)
        else:
            year2=None
    books_between_years = data_source.books_between_years(year1,year2)
    for book in books_between_years:
        print(book.title,'(',book.publication_year,') by ',book.authors)
else:
    print_error()

print()
print()