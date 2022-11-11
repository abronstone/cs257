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
    title=flask.request.args.get('title',default='')
    director=flask.request.args.get('director',default='')
    keyword=flask.request.args.get('keyword',default='')
    collection=flask.request.args.get('collection',default='')
    cast=flask.request.args.get('cast',default='')
    crew=flask.request.args.get('crew',default='')
    productioncompany=flask.request.args.get('productioncompany',default='')
    genre=flask.request.args.get('genre',default='')
    language=flask.request.args.get('language',default='')
    rating=flask.request.args.get('rating',default='')
    country=flask.request.args.get('country',default='')
    releasedate=flask.request.args.get('releasedate',default='')
    released=flask.request.args.get('released',default='')
    adult=flask.request.args.get('adult',default='')
    numParameters = 0
    #Add all other tables after converted
    query = '''SELECT movie_metadata.id,movie_metadata.title,movie_metadata.imdb_id,movie_metadata.release_date from movie_metadata'''
    where_clause = ''''''
    arguments = []
    if title != '':
        where_clause = where_clause + ''' WHERE title ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(title)
    if director != '':
        where_clause = where_clause + ''' AND director ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(director)
    #NOT FUNCTIONAL
    if keyword != '':
        where_clause = where_clause + ''' AND movie_social.keywords && '{9715}'::int[]'''
        arguments.append(keyword)
    if collection != '':
        where_clause = where_clause + ''' AND movie_metadata.id=collections.movie_id AND collection.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(collection)
    #NOT FUNCTIONAL
    if cast != '':
        where_clause = where_clause + ''' AND movie_'''
        arguments.append(cast)
    #NOT FUNCTIONAL
    if crew != '':
        where_clause = where_clause + ''' AND '''
        arguments.append(crew)
    #NOT FUNCTIONAL
    if productioncompany != '':
        where_clause = where_clause + ''' AND '''
        arguments.append(productioncompany)
    #NOT FUNCTIONAL
    if genre != '':
        where_clause = where_clause + ''' AND movie_metadata.genres && '{9715}'::int[] '''
        arguments.append(genre)
    #NOT FUNCTIONAL
    if language != '':
        where_clause = where_clause + ''' AND '''
        arguments.append(language)
    #NOT FUNCTIONAL
    #if rating != '':
        #where_clause = where_clause + ''' AND movie_metadata.id=ratings.movie_id and ratings.rating > %s'''
        #arguments.append(rating)
    #NOT FUNCTIONAL
    if country != '':
        where_clause = where_clause + ''' and movie_metadata.countries && '{9715}'::int[] '''
        arguments.append(country)
    if releasedate != '':
        where_clause = where_clause + ''' AND release_date > %s'''
        arguments.append(releasedate)
    #NOT FUNCTIONAL
    if adult != False:
        where_clause = where_clause + ''''''
    #NOT FUNCTIONAL
    if released != False:
        where_clause = where_clause + ''''''
    query = query + where_clause + ''';'''
    

        
    #if title!='':
        #query='''SELECT id,title,imdb_id,release from movie_metadata where title ILIKE CONCAT('%%', %s, '%%');'''
    #elif keyword!='':
        #print(keyword)
        #query='''select movie_metadata.id,movie_metadata.title,keywords.word from movie_metadata,movie_social,keywords where movie_metadata.id=movie_social.id and movie_social.keywords && '{9715}'::int[];'''
        #query='''SELECT movie_metadata.id,title,imdb_id FROM movie_metadata,movie_social WHERE movie_social.id=movie_metadata.id AND movie_social.keywords ILIKE CONCAT('%%', %s, '%%');'''
    #else:
        #query='''SELECT id,title,imdb_id from movies_metadata;'''
    #query='''SELECT id,title,imdb_id,release_date from movie_metadata where title ILIKE CONCAT('%%', %s, '%%');'''
    #arguments=[title]
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,arguments)
        print(cursor.query)
        for row in cursor:
            #print(row[3])
            movie = {'id':row[0], 'title':row[1], 'link':row[2], 'release_date':str(row[3])[0:4]}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)


@api.route('/overviewresults/')
def get_overview():
    search_text = flask.request.args.get('search_text',default='')
    print(type(search_text))
    selector = flask.request.args.get('selector',default='')
    randomizer = flask.request.args.get('randomizer',default=False)
    arguments=[]
    if not randomizer:
        query='''SELECT movie_metadata.id,movie_metadata.title FROM movie_metadata'''
        if search_text != '':
            query = query + ''' WHERE %s ILIKE CONCAT('%%',%s,'%%');'''
            arguments=[selector,search_text]
    else:
        query='''SELECT movie_metadata.id,movie_metadata.title,overviews.tagline,overviews.overview,movie_social.popularity FROM movie_metadata,movie_social,overviews where movie_metadata.id=movie_social.id AND movie_metadata.id=overviews.movie_id AND movie_metadata.title ILIKE CONCAT('%%',%s,'%%') ORDER BY movie_social.popularity DESC;'''
        arguments=[search_text]
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,arguments)
        print(cursor.query)
        for row in cursor:
            movie = {'id':row[0], 'title':row[1], 'tagline':row[2], 'overview':row[3], 'popularity':row[4]}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/popularityresults/')
def get_popularity():
    query=''''''

@api.route('/comparisonresults/')
def get_comparison():
    query=''''''