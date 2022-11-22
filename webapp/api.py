'''
    api.py for Vidinfo
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


#Returns a psycopg2 connection, using PostgreSQL database login info found in config.py
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

@api.route('/help/')
def help():
    '''
        RETURNS THE 'api-design/txt' FILE IN TOP DIRECTORY
    '''
    return flask.send_file('api-design.txt', mimetype='text/plain')

@api.route('/searchresults/')
def get_search():
    '''
        Returns a list of JSON objects, each with a movie title, movie idm imdb_link, and release date

        This API endpoint goes through the following steps:
            1.) Uses Flask to get the query parameters from the API url
            2.) Adds the query parameters to a 'WHERE' clause
            3.) Formulates an SQL query to select the required data stated above
            4.) Returns a JSON formatted list of movie objects using json.dumps()
        
        CALLER:
            search.js > 'onButtonSubmit'
    '''
    keyword = flask.request.args.get('keyword',default='')
    collection = flask.request.args.get('collection',default='')
    cast = flask.request.args.get('cast',default='')
    crew = flask.request.args.get('crew',default='')
    productioncompany = flask.request.args.get('productioncompany',default='')
    genre = flask.request.args.get('genre',default='')
    language = flask.request.args.get('languagedroplist',default='')
    rating_box = flask.request.args.get('ratingbox',default='')
    rating = flask.request.args.get('rating',default='')
    country = flask.request.args.get('country',default='')
    releasedatebefore = flask.request.args.get('release-date-before',default='')
    releasedateafter = flask.request.args.get('release-date-after',default='')
    released = flask.request.args.get('released',default='')
    adult = flask.request.args.get('adult',default='')

    sources = ['''movies''']
    where_clause = []
    arguments = []

    title = flask.request.args.get('title',default='')
    if title != '':
        where_clause.append('''title ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(title)
         
    director = flask.request.args.get('director',default='')
    if director != '':
        sources.append('''movies_directors,directors''')
        where_clause.append('''movies.id=movies_directors.movie_id AND movies_directors.director_id=directors.id AND directors.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(director)
    if keyword != '':
        sources.append('''movies_keywords,keywords''')
        where_clause.append('''movies.id=movies_keywords.movie_id AND movies_keywords.keyword_id=keywords.id AND keywords.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(keyword)
    if collection != '':
        sources.append('''collections''')
        where_clause.append('''movies.collection_id=collections.collection_id AND collections.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(collection)
    if cast != '':
        sources.append('''movies_actors,actors''')
        where_clause.append('''movies.id=movies_actors.movie_id AND movies_actors.actor_id=actors.id AND actors.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(cast)
    if crew != '':
        sources.append('''movies_crew,crew''')
        where_clause.append('''movies.id=movies_crew.movie_id AND movies_crew.crew_id=crew.id AND crew.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(crew)
    if productioncompany != '':
        sources.append('''movies_companies,production_companies''')
        where_clause.append('''movies.id=movies_companies.movie_id AND movies_companies.production_company_id=production_companies.id AND production_companies.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(productioncompany)
    if genre != '':
        sources.append('''movies_genres,genres''')
        where_clause.append('''movies.id=movies_genres.movie_id AND movies_genres.genre_id=genres.id AND genres.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(genre)
    if language != '':
        sources.append('''movies_languages,languages''')
        where_clause.append('''movies.id=movies_languages.movie_id AND movies_languages.language_id=languages.id AND languages.name=%s''')
        arguments.append(language)
    if rating_box != '':
        sources.append('''movies_ratings''')
        where_clause.append('''movies.id=movies_ratings.movie_id AND movies_ratings.average_rating>%s''')
        arguments.append(rating)
    if country != '':
        sources.append('''movies_countries,countries''')
        where_clause.append('''movies.id=movies_countries.movie_id AND movies_countries.country_id=countries.id AND countries.name ILIKE CONCAT('%%',%s,'%%')''')
        arguments.append(country)
    if releasedatebefore != '':
        where_clause.append('''movies.release_date<=%s''')
        arguments.append(releasedatebefore)
    if releasedateafter != '':
        where_clause.append('''movies.release_date>=%s''')
        arguments.append(releasedateafter)
    if released != 'on':
        where_clause.append('''movies.released=\'Released\'''')
    if adult != 'on':
        where_clause.append('''movies.adult=\'False\'''')

    all_sources = ''
    all_where_clauses = ''
    for source in sources:
        all_sources = all_sources + source + ','
    all_sources = all_sources[:-1]
    num_clauses = 0
    for clause in where_clause:
        if num_clauses>=1:
            all_where_clauses = all_where_clauses + ''' AND ''' + clause
        elif num_clauses==0:
            all_where_clauses = all_where_clauses + ''' WHERE ''' + clause
        num_clauses+=1
    query = '''SELECT distinct(movies.id),movies.title,movies.imdb_link,movies.release_date,movies.collection_id FROM ''' + all_sources + all_where_clauses + '''ORDER BY movies.collection_id,movies.release_date;'''
    
    movie_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,arguments)
        for row in cursor:
            movie = {'id':row[0], 'title':row[1], 'imdb_link':row[2], 'release_date':str(row[3])[0:4]}
            movie_list.append(movie)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/searchlanguageload/')
def get_languages():
    '''
        Returns a list of all movie languages in the PSQL server

        Used to make the 'language' datalist in 'mockup2.html':SEARCH easier to use

        CALLER: 
            search.js > 'initialize'
    '''
    query = '''SELECT id,name from languages;'''
    language_list=[]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            language = {'id':row[0],'name':row[1]}
            language_list.append(language)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(language_list)

@api.route('/overviewresults/')
def get_overview():
    '''
        Returns a JSON object with data to create a complete overview of a specific movie

        This API endpoint performs the following steps:
            1.) Creates an SQL query that returns most metadata from the selected movie id
            2.) Formats each metadata to be represented in string format (json.dumps() compatible) and puts it into a movie object
            2.) Returns the movie object in JSON format

        CALLER:
            overviews.js > 'onButtonPress'
    '''
    id=flask.request.args.get('id',default='')
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
    movies.released,
    collections.name
    FROM movies LEFT JOIN overviews ON movies.id=overviews.movie_id 
    LEFT JOIN movies_ratings ON movies.id=movies_ratings.movie_id 
    LEFT JOIN movies_directors ON movies.id=movies_directors.movie_id
    LEFT JOIN directors ON directors.id=movies_directors.director_id
    LEFT JOIN movies_languages ON movies_languages.movie_id=movies.id
    LEFT JOIN languages ON languages.id=movies_languages.language_id
    LEFT JOIN collections ON movies.collection_id=collections.collection_id 
    WHERE movies.id=%s ORDER BY title,release_date DESC;'''
    genres_query = '''SELECT genres.name from movies_genres
    LEFT JOIN genres ON movies_genres.genre_id=genres.id
    WHERE movies_genres.movie_id=%s;'''
    actors_query = '''SELECT actors.name,movies_actors.character from movies_actors
    LEFT JOIN actors ON movies_actors.actor_id=actors.id
    WHERE movies_actors.movie_id=%s ORDER BY movies_actors.character;'''
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
        for row in main_cursor:

            genres=''
            for genre in genres_cursor:
                if genre[0]!=None:
                    genres+=genre[0]+','
            genres=genres[:-1]

            actors=''
            characters = {}
            for actor in actors_cursor:
                if actor[0]!=None and actor[1]!=None:
                    name = actor[0]
                    character = actor[1]
                    if character not in characters:
                        new_list = []
                        new_list.append(name)
                        characters[character] = new_list
                    else:
                        current_list = characters[character]
                        current_list.append(name)
                        characters[character] = current_list
            for character in characters:
                names_string = ''
                all_credits = characters[character]
                names_string += all_credits[0]
                if len(all_credits)>=2:
                    names_string+=", "+all_credits[1]
                    if len(all_credits)>2:
                        names_string+=',...{+'+str(len(all_credits)-2)+'}'
                actors+='<strong>"'+character+'</strong> : '+names_string+'<br>'
            actors=actors[:-2]

            keywords=''
            for keyword in keywords_cursor:
                if keyword[0]!=None:
                    keywords+=keyword[0]+', '
            keywords=keywords[:-2]

            crew=''
            crew_roles={}
            for crewmate in crew_cursor:
                name = crewmate[0]
                role = crewmate[1]
                if name!=None:
                    if role not in crew_roles:

                        new_list = []
                        new_list.append(name)
                        crew_roles[role]=new_list
                    else:
                        current_list = crew_roles[role]
                        current_list.append(name)
                        crew_roles[role] = current_list
            for role in crew_roles:
                names_string = ''
                all_credits = crew_roles[role]
                names_string += all_credits[0]
                if len(all_credits)>=2:
                    names_string+=", "+all_credits[1]
                    if len(all_credits)>2:
                        names_string+=',...{+'+str(len(all_credits)-2)+'}'
                crew+="<strong>"+role+"</strong> : "+names_string+"<br>"

            companies=''
            for company in companies_cursor:
                if company[0]!=None:
                    companies+=company[0]+', '
            companies=companies[:-2]

            countries=''
            for country in countries_cursor:
                if country[0]!=None:
                    countries+=country[0]+', '
            countries=countries[:-2]

            rating = row[5]
            if rating!=None:
                rating=round(rating,2)

            movie = {'id':row[0], 'title':row[1], 'tagline':row[2], 'overview':row[3], 'popularity':str(row[4]), 'rating':str(rating), 'director':str(row[6]), 'genres':genres, 'link':row[7], 'language':row[8], 'release_date':str(row[9]), 'revenue':row[10], 'budget':row[11], 'status':row[12], 'collection':row[13], 'actors':actors, 'keywords':keywords, 'companies':companies, 'countries':countries, 'crew':crew}
            movie_list.append(movie)
        main_cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

@api.route('/listload/')
def overview_list_load():
    '''
        This API is called every time a character is entered into these datalists.
        Returns a list of JSON objects containing movie id's and titles from the PSQL database to be used in the datalists in 'mockup3.html' OVERVIEW and 'mockup5.html': COMPARISON.

        Three queries are executed in this order to load the list, based on a current value 'str' that is in the input (case insensitive):
            1.) All movies that match 'str' exactly
            2.) All movies that start with 'str'
            3.) All movies that contain 'str' 
    '''
    title=flask.request.args.get('title',default='')
    args=[]
    query_exact = '''SELECT title,release_date,id FROM movies WHERE title ILIKE %s ORDER BY popularity DESC;'''
    query_first_like = '''SELECT title,release_date,id FROM movies WHERE title ILIKE CONCAT(%s,'%%') AND title NOT ILIKE CONCAT('%%',%s,'%%') AND title NOT ILIKE %s ORDER BY popularity DESC;'''
    query_all_like = '''SELECT title,release_date,id FROM movies WHERE title ILIKE CONCAT('%%',%s,'%%') AND title NOT LIKE CONCAT(%s,'%%') AND title NOT ILIKE %s ORDER BY popularity DESC;'''
    movie_list=[]
    try:
        connection = get_connection()
        cursor_exact = connection.cursor()
        args.append(title)
        cursor_exact.execute(query_exact,args)
        cursor_first_like = connection.cursor()
        args.append(title)
        args.append(title)
        cursor_first_like.execute(query_first_like,args)
        cursor_all_like = connection.cursor()
        cursor_all_like.execute(query_all_like,args)
        for row in cursor_exact:
            movie = {'title':row[0],'release_date':str(row[1])[0:4],'id':row[2]}
            movie_list.append(movie)
        for row in cursor_first_like:
            movie = {'title':row[0],'release_date':str(row[1])[0:4],'id':row[2]}
            movie_list.append(movie)
        for row in cursor_all_like:
            movie = {'title':row[0],'release_date':str(row[1])[0:4],'id':row[2]}
            movie_list.append(movie)
        cursor_exact.close()
        cursor_first_like.close()
        cursor_all_like.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)

def create_random_id(previous_title,filters,inputs):
    '''
        HELPER METHOD FOR '/get_generator/'

        This method creates a query that gets a random movie id based on three OPTIONAL filters from the 'Random Movie Generator' API endpoint
    '''
    #This dictionary links table names and their corresponding 'movies_[table].[table]_id' names
    table_linking_id_name = {
        'directors':'director_id',
        'languages':'language_id',
        'genres':'genre_id',
        'production_companies':'production_company_id',
        'countries':'country_id',
        'actors':'actor_id',
        'crew':'crew_id',
        'keywords':'keyword_id',
        'collections':'collection_id'}
    selector_clause = '''movies'''
    where_clause = ''' WHERE movies.title!=%s'''
    arguments=[previous_title]

    num_clauses = 0
    for f in filters:
        x=f
        if f=='production_companies':
            x='companies'
        else:
            x='movies_'+f
        if f!='':
            if f=='collections':
                selector_clause = selector_clause + ''','''+f
                where_clause = where_clause + ''' AND movies.collection_id=collections.collection_id AND collections.name ILIKE CONCAT('%%',%s,'%%')'''
            else:
                selector_clause = selector_clause + ''','''+x+''','''+f
                where_clause = where_clause + ''' AND movies.id='''+x+'''.movie_id AND '''+x+'''.''' + table_linking_id_name[f] + '''='''+f+'''.id AND '''+f+'''.name ILIKE CONCAT('%%',%s,'%%')'''
            arguments.append(inputs[num_clauses])
            num_clauses+=1
    query = '''SELECT movies.id FROM ''' + selector_clause + where_clause + ''' ORDER BY random() LIMIT 1;'''
    id=None
    try:
        connection = get_connection()
        random_id_cursor = connection.cursor()
        random_id_cursor.execute(query,arguments)
        for row in random_id_cursor:
            id = row[0]
    except Exception as e:
        print(e, file=sys.stderr)
    return id
    
@api.route('/generatorresults/')
def get_generator():
    '''
        Returns a JSON object containing data to make a complete overview of a random movie, based on three optional filters provided to the user
        
        This API endpoint performs the following steps:
            1.) Calls 'create_random_id' to get a random movie id
            2.) Creates an SQL query that returns most metadata from the randomized movie id
            3.) Formats each metadata to be represented in string format (json.dumps() compatible) and puts it into a movie object
            4.) Returns the movie object in JSON format

        CALLER:
            overviews.js > 'onButtonPress'
    '''
    previous_title = flask.request.args.get('previoustitle',default=None)
    filter_one = flask.request.args.get('filterOne',default=None)
    input_one = flask.request.args.get('inputOne',default=None)
    filter_two = flask.request.args.get('filterTwo',default=None)
    input_two = flask.request.args.get('inputTwo',default=None)
    filter_three = flask.request.args.get('filterThree',default=None)
    input_three = flask.request.args.get('inputThree',default=None)

    random_id = create_random_id(previous_title,[filter_one,filter_two,filter_three],[input_one,input_two,input_three])
    arguments=[random_id]

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
    movies.released,
    collections.name
    FROM movies LEFT JOIN overviews ON movies.id=overviews.movie_id 
    LEFT JOIN movies_ratings ON movies.id=movies_ratings.movie_id 
    LEFT JOIN movies_directors ON movies.id=movies_directors.movie_id
    LEFT JOIN directors ON directors.id=movies_directors.director_id
    LEFT JOIN movies_languages ON movies_languages.movie_id=movies.id
    LEFT JOIN languages ON languages.id=movies_languages.language_id 
    LEFT JOIN collections ON movies.collection_id=collections.collection_id 
    WHERE movies.id=%s ORDER BY title,release_date DESC;'''
    genres_query = '''SELECT genres.name from movies_genres
    LEFT JOIN genres ON movies_genres.genre_id=genres.id
    WHERE movies_genres.movie_id=%s;'''
    actors_query = '''SELECT actors.name,movies_actors.character from movies_actors
    LEFT JOIN actors ON movies_actors.actor_id=actors.id
    WHERE movies_actors.movie_id=%s ORDER BY movies_actors.character;'''
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

    movie_list=[]
    try:
        connection = get_connection()
        '''random_id_cursor = connection.cursor()
        random_id_cursor.execute(random_id_query)
        for row in random_id_cursor:
            id = row[0]
        arguments=[id]
        '''
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

        for row in main_cursor:
            genres=''
            for genre in genres_cursor:
                if genre[0]!=None:
                    genres+=genre[0]+','
            genres=genres[:-1]

            actors=''
            for actor in actors_cursor:
                if actor[0]!=None and actor[1]!=None:
                    actors+=actor[0]+' as <strong>"'+actor[1]+'"</strong><br>'
            actors=actors[:-2]

            keywords=''
            for keyword in keywords_cursor:
                if keyword[0]!=None:
                    keywords+=keyword[0]+', '
            keywords=keywords[:-2]

            crew=''
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
            
            companies=''
            for company in companies_cursor:
                if company[0]!=None:
                    companies+=company[0]+', '
            companies=companies[:-2]

            countries=''
            for country in countries_cursor:
                if country[0]!=None:
                    countries+=country[0]+', '
            countries=countries[:-2]
            rating = row[5]
            if rating!=None:
                rating=round(rating,2)
            else:
                rating="[no rating available]"
            movie = {'id':row[0], 'title':row[1], 'tagline':row[2], 'overview':row[3], 'popularity':str(row[4]), 'rating':str(rating), 'director':str(row[6]), 'genres':genres, 'link':row[7], 'language':row[8], 'release_date':str(row[9]), 'revenue':row[10], 'budget':row[11], 'status':row[12], 'actors':actors, 'keywords':keywords, 'companies':companies, 'countries':countries, 'crew':crew, 'collection':row[13]}
            movie_list.append(movie)
        main_cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)


@api.route('/comparisonresults/')
def get_comparison():
    '''
        Returns two JSON objects representing movies that match the inputted id's, each with the following data:
        {id, title, popularity, average rating, revenue, budget, runtime, director, release date}
    '''
    first_movie = flask.request.args.get('firstmovie',default='')
    second_movie = flask.request.args.get('secondmovie',default='')

    query='''SELECT movies.id,movies.title,movies.popularity,movies_ratings.average_rating,movies.revenue,movies.budget,movies.runtime,directors.name,movies.release_date 
    FROM movies
    LEFT JOIN movies_ratings ON movies.id=movies_ratings.movie_id 
    LEFT JOIN movies_directors ON movies.id=movies_directors.movie_id
    LEFT JOIN directors ON movies_directors.director_id=directors.id 
    WHERE movies.id=%s LIMIT 1;'''

    movie_list=[]
    try:
        connection = get_connection()
        arguments = [first_movie]
        cursor1 = connection.cursor()
        cursor1.execute(query,arguments)
        arguments = [second_movie]
        cursor2 = connection.cursor()
        cursor2.execute(query,arguments)
        for row in cursor1:
            movieOne = {'title':row[1], 'popularity':str(row[2]), 'rating':str(row[3]), 'revenue':row[4], 'budget':row[5], 'runtime':str(int(row[6])), 'director':row[7], 'release-date':str(row[8])}
            movie_list.append(movieOne)
        for row in cursor2:
            movieTwo = {'title':row[1], 'popularity':str(row[2]), 'rating':str(row[3]), 'revenue':row[4], 'budget':row[5], 'runtime':str(int(row[6])), 'director':row[7], 'release-date':str(row[8])}
            movie_list.append(movieTwo)
        cursor1.close()
        cursor2.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(movie_list)