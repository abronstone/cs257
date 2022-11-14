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

def add_where_clauses(where_clause,num_params):
    if num_params>=1:
        where_clause = where_clause + ''' AND '''
    elif num_params==0:
        where_clause = where_clause + ''' WHERE '''
    return where_clause

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
    language=flask.request.args.get('languagedroplist',default='')
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
    if title != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''title ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(title)
        num_params+=1
    if director != '':
        sources = sources + ''',movies_directors,directors'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_directors.movie_id AND movies_directors.director_id=directors.id AND directors.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(director)
        num_params+=1
    if keyword != '':
        sources = sources + ''',movies_keywords,keywords'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_keywords.movie_id AND movies_keywords.keyword_id=keywords.id AND keywords.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(keyword)
        num_params+=1
    if collection != '':
        sources = sources + ''',collections'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.collection_id=collections.collection_id AND collections.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(collection)
        num_params+=1
    if cast != '':
        sources = sources + ''',movies_actors,actors'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_actors.movie_id AND movies_actors.actor_id=actors.id AND actors.name ILIKE CONCAT('%%',%s,'%%')'''
        arguments.append(cast)
        num_params+=1
    if crew != '':
        sources = sources + ''',movies_crew,crew'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_crew.movie_id AND movies_crew.crew_id=crew.id AND crew.name ILIKE CONCAT('%%',%s,'%%')'''
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
        where_clause = where_clause + '''movies.id=movies_languages.movie_id AND movies_languages.language_id=languages.id AND languages.id=%s'''
        arguments.append(language)
        num_params+=1
    if rating != '':
        sources = sources + ''',movies_ratings'''
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.id=movies_ratings.movie_id AND (movies_ratings.average_rating>%s OR movies_ratings.average_rating IS NULL)'''
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
    if releasedate != '':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE '''
        where_clause = where_clause + '''movies.release_date>%s'''
        arguments.append(releasedate)
        num_params+=1
    if released!='on':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE ''' 
        where_clause = where_clause + '''movies.released=\'Released\''''
    if adult!='on':
        if num_params>=1:
            where_clause = where_clause + ''' AND '''
        elif num_params==0:
            where_clause = where_clause + ''' WHERE ''' 
        where_clause = where_clause + '''movies.adult=\'False\''''
    query = selections + sources + where_clause + group_by_clause + ''' ORDER BY movies.title;'''
    
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

@api.route('/searchlanguageload/')
def get_languages():
    #print('loading languages')
    query = '''SELECT id,name from languages;'''
    language_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            language = {'id':row[0],'name':row[1]}
            language_list.append(language)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    print(language_list)
    return json.dumps(language_list)

@api.route('/overviewresults/')
def get_overview():
    '''print('results')
    search_text = flask.request.args.get('search_text',default='')
    id=int(search_text[search_text.find('[id:')+4:-1])
    search_text=search_text[0:search_text.find('[id:')-8]
    print('[',search_text,']')
    print('[',id,']')
    print(type(search_text))
    '''
    id=flask.request.args.get('search_text',default='')
    selector = flask.request.args.get('selector',default='')
    randomizer = flask.request.args.get('randomizer',default=False)
    #if not randomizer:
        #query='''SELECT movie_metadata.id,movie_metadata.title FROM movie_metadata where release_date ILIKE %s'''
        #if id != '':
            #query = query + ''' WHERE %s ILIKE CONCAT('%%',%s,'%%');'''
            #arguments=[selector,id]
    #else:
        #query='''SELECT movies.id,movies.title,overviews.tagline,overviews.overview,movies.popularity,movies_ratings.average_rating FROM movies,overviews,movies_ratings where movies.id=movies_ratings.movie_id AND movies.id=overviews.movie_id AND movies.title ILIKE CONCAT('%%',%s,'%%') ORDER BY char_length(title),popularity;'''
    main_query = '''SELECT 
    movies.id,
    movies.title,
    overviews.tagline,
    overviews.overview,
    movies.popularity,
    movies_ratings.average_rating,
    directors.name,
    movies.imdb_link,
    languages.name,
    movies.release_date,
    movies.revenue,
    movies.budget,
    movies.released
    FROM movies LEFT JOIN overviews ON movies.id=overviews.movie_id 
    LEFT JOIN movies_ratings ON movies.id=movies_ratings.movie_id 
    LEFT JOIN movies_directors ON movies.id=movies_directors.movie_id
    LEFT JOIN directors ON directors.id=movies_directors.director_id
    LEFT JOIN movies_languages ON movies_languages.movie_id=movies.id
    LEFT JOIN languages ON languages.id=movies_languages.language_id
    WHERE movies.id=%s ORDER BY title,release_date DESC;'''
    genres_query = '''SELECT genres.name from movies_genres
    LEFT JOIN genres ON movies_genres.genre_id=genres.id
    WHERE movies_genres.movie_id=%s;'''
    actors_query = '''SELECT actors.name,movies_actors.character from movies_actors
    LEFT JOIN actors ON movies_actors.actor_id=actors.id
    WHERE movies_actors.movie_id=%s ORDER BY movies_actors.character;'''
    #actor_query = '''SELECT actors.name,movies_actors.character,AVG(popularity) as actor_popularity from movies
    #FULL OUTER JOIN movies_actors ON movies_actors.movie_id=movies.id
    #LEFT JOIN actors ON movies_actors.actor_id=actors.id
    #WHERE movies.id=%s GROUP BY actors.name,movies_actors.character ORDER by actor_popularity;'''
    crew_query = '''SELECT crew.name,movies_crew.role FROM movies_crew
    LEFT JOIN crew ON movies_crew.crew_id=crew.id
    WHERE movies_crew.movie_id=%s ORDER BY movies_crew.role'''
    keywords_query = '''SELECT keywords.name from movies_keywords
    LEFT JOIN keywords ON movies_keywords.keyword_id=keywords.id
    WHERE movies_keywords.movie_id=%s ORDER BY keywords.name;'''
    companies_query = '''SELECT production_companies.name from movies_companies
    LEFT JOIN production_companies ON movies_companies.production_company_id=production_companies.id
    WHERE movies_companies.movie_id=%s ORDER BY production_companies.name;'''
    countries_query = '''SELECT countries.name from movies_countries
    LEFT JOIN countries ON movies_countries.country_id=countries.id
    WHERE movies_countries.movie_id=%s ORDER BY countries.name;'''
    arguments=[id]
    movie_list=[]
    try:
        connection = get_connection()
        main_cursor = connection.cursor()
        main_cursor.execute(main_query,arguments)
        genres_cursor = connection.cursor()
        genres_cursor.execute(genres_query,arguments)
        actors_cursor = connection.cursor()
        actors_cursor.execute(actors_query,arguments)
        keywords_cursor = connection.cursor()
        keywords_cursor.execute(keywords_query,arguments)
        companies_cursor = connection.cursor()
        companies_cursor.execute(companies_query,arguments)
        countries_cursor = connection.cursor()
        countries_cursor.execute(countries_query,arguments)
        crew_cursor= connection.cursor()
        crew_cursor.execute(crew_query,arguments)
        #print(main_cursor.query)
        for row in main_cursor:
            genres=''
            actors=''
            keywords=''
            companies=''
            countries=''
            crew=''
            for genre in genres_cursor:
                if genre[0]!=None:
                    genres+=genre[0]+','
            genres=genres[:-1]
            for actor in actors_cursor:
                if actor[0]!=None and actor[1]!=None:
                    actors+=actor[0]+' as <strong>"'+actor[1]+'"</strong><br>'
            actors=actors[:-2]
            print('keywords:'+keywords)
            for keyword in keywords_cursor:
                if keyword[0]!=None:
                    keywords+=keyword[0]+', '
            keywords=keywords[:-2]
            print('keywords new:'+keywords)
            crew_roles={}
            all_roles=[]
            for crewmate in crew_cursor:
                if crewmate[0]!=None:
                    if crewmate[1] not in all_roles:
                        all_roles.append(crewmate[1])
                        crew_roles[crewmate[1]]=crewmate[0]
                    else:
                        crew_roles[crewmate[1]]='{multiple}'
            for crewmate in crew_roles:
                crew+=crew_roles[crewmate]+" : <strong>"+crewmate+"</strong><br>"
            for company in companies_cursor:
                if company[0]!=None:
                    companies+=company[0]+', '
            companies=companies[:-2]
            for country in countries_cursor:
                if country[0]!=None:
                    countries+=country[0]+', '
            countries=countries[:-2]
            rating = row[5]
            if rating!=None:
                rating=round(rating,2)
            else:
                rating="[no rating available]"
            print('keywordsl:'+keywords)
            movie = {'id':row[0], 'title':row[1], 'tagline':row[2], 'overview':row[3], 'popularity':str(row[4]), 'rating':str(rating), 'director':str(row[6]), 'genres':genres, 'link':row[7], 'language':row[8], 'release_date':str(row[9]), 'revenue':row[10], 'budget':row[11], 'status':row[12], 'actors':actors, 'keywords':keywords, 'companies':companies, 'countries':countries, 'crew':crew}
            movie_list.append(movie)
        main_cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/overviewlistload/')
def overview_list_load():
    query = '''SELECT title,release_date,id from movies ORDER by popularity DESC;'''
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            movie = {'title':row[0],'release_date':str(row[1])[0:4],'id':row[2]}
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