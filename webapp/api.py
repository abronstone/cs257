'''
    api.py
    Jack Owens and Aaron Bronstone
    Created 11/07/22
'''
import sys
import flask
import json
import config
import psycopg2
import urllib.request

api=flask.Blueprint('api',__name__)

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

@api.route('/searchresults/')
def get_search():
    query='''SELECT id,title from movies_metadata;'''
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            movie = {'id':row[0], 'title':row[1]}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/overviewresults/')
def get_overview():
    query='''SELECT movies_metadata.id,movies_metadata.title,directors.name FROM movies_metadata,movies_credits,directors where movies_credits.director_id=director.id'''