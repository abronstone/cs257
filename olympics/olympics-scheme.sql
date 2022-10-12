CREATE TABLE athletes(id INTEGER, firstname TEXT,surname TEXT,fullsurname TEXT,sex TEXT,age INTEGER,height DECIMAL,weight DECIMAL,team TEXT,NOC TEXT,sport TEXT);
CREATE TABLE games(id serial,name text,year integer,season text,city text);
CREATE TABLE sport(id serial,name text,event text);
CREATE TABLE nocs(id serial,name text,country text);
CREATE TABLE results(athlete_id integer,games_id integer,event_id integer,medal text);
