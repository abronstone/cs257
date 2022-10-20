'''
    olympics.py
    Author: Aaron Bronstone
'''

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL) 

import sys
import argparse
import psycopg2
import config


def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def main():
    #connection = get_connection()
    #cursor = connection.cursor()

    parser = argparse.ArgumentParser()
    parser.add_argument("-aa","--allathletes",default=None,help="Displays all athletes from the specified three-lettered NOC, case insensitive",type=str)
    parser.add_argument("-ng","--nocgolds",action='store_true',default=None,help="Lists all the NOC's and the number of gold medals each has won, in decreasing order of gold medals")
    parser.add_argument("-tt","--toptwenty",default=None,help="Shows the top twenty athletes based on number of gold medals earned for a specific year",type=str)
    args=parser.parse_args()
    #rint(args)
    #print()
    #print('------------------')

    if args.allathletes:
        noc = args.allathletes.lower()
        athletes = get_athletes_in_noc(noc)
        for a in athletes:
            print(a)
    elif args.nocgolds:
        #noc = args.athnoc
        golds = get_number_of_golds()
        for key in golds:
            print(str(key)+": "+str(golds[key]))
            
    elif args.toptwenty:
        year = args.toptwenty
        tty = get_top_twenty(year)
        for key in tty:
            print(key+": "+str(tty[key]))

    #print()
    #print('------------------')

def get_athletes_in_noc(search_text):
    athletes=[]
    #print('in here')
    try:
        #print(0)
        query='''SELECT surname,firstname FROM athletes WHERE noc=%s'''
        #print(6)
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,(search_text,))
        #print(1)
        for row in cursor:
            #print(2)
            first_name = row[1]
            surname = row[0]
            athletes.append(f'{first_name} {surname}')
    except Exception as e:
        #print(5)
        print(e, file=sys.stderr)
    #print(4)
    connection.close()
    return athletes

def get_number_of_golds():
    noc_golds = {}
    #print(3)
    try:
        query = '''SELECT athletes.noc,count(medal) AS golds FROM athletes,results WHERE athletes.id=results.athlete_id AND medal='Gold' GROUP BY athletes.noc ORDER BY golds desc'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            noc = row[0]
            number = row[1]
            noc_golds[noc]=number
    except Exception as e:
        print(e, file=sys.stderr)
    connection.close()
    return noc_golds

def get_top_twenty(search_text):
    toptwenty={}
    try:
        query = '''SELECT athletes.fullsurname,athletes.firstname,count(medal) AS golds FROM games,athletes,results WHERE athletes.id=results.athlete_id AND games.id=results.games_id AND games.year=%s AND medal='Gold' GROUP BY athletes.fullsurname,athletes.firstname ORDER BY golds desc LIMIT 20'''
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute(query,(search_text,))
        for row in cursor:
            surname=row[0]
            firstname=row[1]
            full_name = firstname+" "+surname
            golds=row[2]
            toptwenty[full_name]=golds
    except Exception as e:
        print(e,file=sys.stderr)
    connection.close()
    return toptwenty


main()

