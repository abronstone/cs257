CREATE TABLE movies(
    id INTEGER,
    title TEXT,
    imdb_link TEXT,
    homepage TEXT,
    collection_id INTEGER,
    release_date DATE,
    runtime DECIMAL,
    popularity DECIMAL,
    revenue BIGINT,
    budget BIGINT,
    released TEXT
    adult TEXT);

CREATE TABLE movies_directors(
    movie_id INTEGER,
    director_id INTEGER
);

CREATE TABLE directors(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_actors(
    movie_id INTEGER,
    actor_id INTEGER,
    character TEXT
);

CREATE TABLE actors(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_crew(
    movie_id INTEGER,
    crew_id INTEGER
    role TEXT
);

CREATE TABLE crew(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_genres(
    movie_id INTEGER,
    genre_id INTEGER
);

CREATE TABLE genres(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_languages(
    movie_id INTEGER,
    language_id INTEGER
);

CREATE TABLE languages(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_companies(
    movie_id INTEGER,
    production_company_id INTEGER
);

CREATE TABLE production_companies(
    id INTEGER,
    name TEXT
);

CREATE TABLE movies_countries(
    movie_id INTEGER,
    country_id INTEGER
);

CREATE TABLE countries(
    id INTEGER,
    abrev TEXT,
    name TEXT
);

CREATE TABLE ratings(
    movie_id INTEGER,
    rating DECIMAL
);

CREATE TABLE movies_ratings(
    movie_id INTEGER,
    average_rating DECIMAL
);

CREATE TABLE movies_keywords(
    movie_id INTEGER,
    keyword_id INTEGER
);

CREATE TABLE keywords(
    id INTEGER,
    name TEXT
);

CREATE TABLE collections(
    collection_id INTEGER,
    name TEXT
);

CREATE TABLE overviews(
    movie_id INTEGER,
    tagline TEXT,
    overview TEXT
);