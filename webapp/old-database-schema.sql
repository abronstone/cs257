CREATE TABLE movie_metadata(
    id INTEGER,
    title TEXT,
    imdb_id TEXT,
    homepage TEXT,
    collection_id INTEGER,
    genres INTEGER[],
    language_id INTEGER,
    countries INTEGER[],
    release_date DATE,
    runtime DECIMAL);

CREATE TABLE movie_credits(
    id INTEGER,
    production_company_ids INTEGER[],
    director_id INTEGER,
    actors INTEGER[],
    crew INTEGER[]);

CREATE TABLE movie_social(
    id INTEGER,
    popularity DECIMAL,
    revenue DECIMAL,
    budget DECIMAL,
    keywords INTEGER[]);

CREATE TABLE collections(
    id INTEGER,
    name TEXT);

CREATE TABLE overviews(
    movie_id INTEGER,
    tagline TEXT,
    overview TEXT);

CREATE TABLE ratings(
    movie_id INTEGER,
    rating DECIMAL);

CREATE TABLE keywords(
    id INTEGER,
    word TEXT);

CREATE TABLE directors(
    id INTEGER,
    name TEXT,
    number_of_movies INTEGER,
    average_popularity DECIMAL,
    average_rating DECIMAL);

CREATE TABLE actors(
    id INTEGER,
    name TEXT);

CREATE TABLE crew(
    id INTEGER,
    name TEXT);

CREATE TABLE genres(
    id INTEGER,
    name TEXT);

CREATE TABLE languages(
    id INTEGER,
    name TEXT);

CREATE TABLE production_companies(
    id INTEGER,
    name TEXT);

CREATE TABLE countries(
    id INTEGER,
    name TEXT);