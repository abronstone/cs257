CREATE TABLE movie_metadata(id INTEGER,title TEXT,original_title TEXT,genres TEXT[],original_language TEXT,release_date DATE,runtime INTEGER);
CREATE TABLE movie_credits(id INTEGER,director_id INTEGER,actors JSON,crew JSON);
CREATE TABLE movie_social(id INTEGER,popularity DECIMAL,average_rating DECIMAL,revenue DECIMAL,budget DECIMAL,keywords JSON);
CREATE TABLE collections(id INTEGER,name TEXT);
CREATE TABLE overviews(movie_id INTEGER,overview TEXT);
CREATE TABLE ratings(user_id INTEGER,movie_id INTEGER,rating DECIMAL);
CREATE TABLE keywords(id INTEGER,word TEXT);
CREATE TABLE directors(id INTEGER,name TEXT,number_of_movies INTEGER,average_popularity DECIMAL,average_rating DECIMAL);
CREATE TABLE actors(id INTEGER,name TEXT);
CREATE TABLE crew(id INTEGER,name TEXT);
CREATE TABLE genres(id INTEGER,name TEXT);
CREATE TABLE languages(id INTEGER,name TEXT);
CREATE TABLE production_companies(id INTEGER,name TEXT);
CREATE TABLE production_countries(id INTEGER,name TEXT);





CREATE TABLE movies_metadata(adult BOOLEAN,belongs_to_collection JSON,budget INTEGER,genres JSON[],homepage TEXT,id INTEGER,imdb_id INTEGER,original_language TEXT,original_title TEXT,overview TEXT,popularity DECIMAL,poster_path TEXT,production_company JSON[],production_country JSON[],release_date DATE,revenue DECIMAL,runtime INTEGER,spoken_language TEXT,status TEXT,tagline TEXT,title TEXT,video BOOLEAN,vote_average DECIMAL,vote_count INTEGER);