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
    query = ''''''
    selections = '''SELECT movies.id,movies.title,movies.imdb_link,movies.release_date'''
    sources = ''' FROM movies'''
    where_clause = ''''''
    group_by_clause = ''''''
    arguments = []
    num_params=0
    print('[',title,']')
    if title != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''title ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(title)
        num_params+=1
    #NEED TO IMPLEMENT
    if director != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''[insert sql query here]'''
        arguments.append(director)
        num_params+=1
    #NEED TO IMPLEMENT
    if keyword != '':
        sources = sources + ''',movies_keywords,keywords'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_keywords.movie_id AND movies_keywords.keyword_id=keywords.id AND keywords.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(keyword)
        num_params+=1
    #NEED TO IMPLEMENT
    if collection != '':
        sources = sources + ''',collections'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.collection_id=collections.collection_id AND collections.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(collection)
        num_params+=1
    #NEED TO IMPLEMENT
    if cast != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''[insert sql query here]'''
        arguments.append(cast)
        num_params+=1
    #NEED TO IMPLEMENT
    if crew != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''[insert sql query here]'''
        arguments.append(crew)
        num_params+=1
    if productioncompany != '':
        sources = sources + ''',movies_companies,production_companies'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_companies.movie_id AND movies_companies.production_company_id=production_companies.id AND production_companies.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(productioncompany)
        num_params+=1
    if genre != '':
        sources = sources+''',movies_genres,genres'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_genres.movie_id AND movies_genres.genre_id=genres.id AND genres.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(genre)
        num_params+=1
    if language != '':
        sources = sources+''',movies_languages,languages'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_languages.movie_id AND movies_languages.language_id=languages.id AND languages.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(language)
        num_params+=1
    #NEED TO IMPLEMENT
    if rating == 'test':
        selections = selections + ''',AVG(ratings.rating) as average_rating'''
        sources = sources + ''',ratings'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=ratings.movie_id AND average_rating>%s'''
        group_by_clause = group_by_clause + ''' GROUP BY title'''
        arguments.append(rating)
        num_params+=1
    if country != '':
        sources = sources + ''',movies_countries,countries'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_countries.movie_id AND movies_countries.country_id=countries.id AND countries.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(country)
        num_params+=1
    #NEED TO IMPLEMENT
    if releasedate != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''[insert sql query here]'''
        arguments.append(releasedate)
        num_params+=1
    query = selections + sources + where_clause + group_by_clause + ''' ORDER BY movies.title;'''
    print(arguments)
    

        
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
            movie = {'id':row[0], 'title':row[1], 'imdb_link':row[2], 'release_date':str(row[3])[0:4]}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)


@api.route('/overviewresults/')
def get_overview():
    print('results')
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
        #query='''SELECT movies.id,movies.title,overviews.tagline,overviews.overview,movies.popularity,movies_ratings.average_rating FROM movies,overviews,movies_ratings where movies.id=movies_ratings.movie_id AND movies.id=overviews.movie_id AND movies.title ILIKE CONCAT('%%',%s,'%%') ORDER BY char_length(title),popularity;'''
        query = '''SELECT movies.id,movies.title,overviews.tagline,overviews.overview,movies.popularity,movies_ratings.average_rating FROM movies LEFT JOIN overviews ON movies.id=overviews.movie_id LEFT JOIN movies_ratings ON movies.id=movies_ratings.movie_id WHERE movies.title ILIKE CONCAT('%%',%s,'%%') ORDER BY average_rating DESC;'''
        arguments=[search_text]
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,arguments)
        print(cursor.query)
        for row in cursor:
            movie = {'id':row[0], 'title':row[1], 'tagline':row[2], 'overview':row[3], 'popularity':str(row[4]), 'rating':str(row[5])}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/overviewlistload/')
def overview_list_load():
    print('list load')
    query = '''SELECT title from movies ORDER by title;'''
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            movie = {'title':row[0]}
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