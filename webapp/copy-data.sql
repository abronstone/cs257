\copy movies from 'movies.csv' CSV delimiter ',' quote '"';

\copy movies_genres from 'movies_genres.csv' CSV delimiter ',' quote '"';
\copy genres from 'unique_genres.csv' CSV delimiter ',' quote '"';

\copy movies_languages from 'movies_languages.csv' CSV delimiter ',' quote '"';
\copy languages from 'unique_languages.csv' CSV delimiter ',' quote '"';

\copy movies_companies from 'movie_companies_convert.csv' CSV delimiter ',' quote '"';
\copy production_companies from 'companies_convert.csv' CSV delimiter ',' quote '"';

\copy movies_countries from 'movies_countries.csv' CSV delimiter ',' quote '"';
\copy countries from 'unique_countries.csv' CSV delimiter ',' quote '"';

\copy ratings from 'ratings_converted.csv' CSV delimiter ',' quote '"';
\copy movies_ratings from 'movies_average_ratings.csv' CSV delimiter ',' quote '"';

\copy movies_keywords from 'movies_keywords.csv' CSV delimiter ',' quote '"';
\copy keywords from 'unique_keywords.csv' CSV delimiter ',' quote '"';

\copy collections from 'unique_collections.csv' CSV delimiter ',' quote '"';

\copy overviews from 'overviews.csv' CSV delimiter ',' quote '"';

\copy directors from 'directors_convert.csv' CSV delimiter ',' quote '"';
\copy movies_directors from 'movie_directors_convert.csv' CSV delimiter ',' quote '"';

\copy crew from 'crew_convert.csv' CSV delimiter ',' quote '"';
\copy movies_crew from 'movie_crew_convert.csv' CSV delimiter ',' quote '"';

\copy actors from 'actors_convert.csv' CSV delimiter ',' quote '"';
\copy movies_actors from 'movie_actors_convert.csv' CSV delimiter ',' quote '"';