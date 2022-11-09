--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.actors (
    id integer,
    name text
);


--
-- Name: collections; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.collections (
    id integer,
    name text
);


--
-- Name: countries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.countries (
    id integer,
    name text
);


--
-- Name: crew; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.crew (
    id integer,
    name text
);


--
-- Name: directors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.directors (
    id integer,
    name text
);


--
-- Name: genres; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.genres (
    id integer,
    name text
);


--
-- Name: keywords; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.keywords (
    id integer,
    word text
);


--
-- Name: languages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.languages (
    id integer,
    name text
);


--
-- Name: movie_credits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movie_credits (
    id integer,
    production_company_ids integer[],
    director_id integer,
    actors integer[],
    crew integer[]
);


--
-- Name: movie_social; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movie_social (
    id integer,
    popularity numeric,
    average_rating numeric,
    revenue numeric,
    budget numeric,
    keywords integer[]
);


--
-- Name: movies_metadata; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movies_metadata (
    id integer,
    title text,
    original_title text,
    collection_id integer,
    genres integer[],
    language_id integer,
    release_date date,
    runtime integer
);


--
-- Name: overviews; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.overviews (
    movie_id integer,
    tagline text,
    overview text
);


--
-- Name: production_companies; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.production_companies (
    id integer,
    name text
);


--
-- Name: ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ratings (
    movie_id integer,
    rating numeric
);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.actors (id, name) FROM stdin;
\.


--
-- Data for Name: collections; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.collections (id, name) FROM stdin;
\.


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.countries (id, name) FROM stdin;
\.


--
-- Data for Name: crew; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.crew (id, name) FROM stdin;
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.directors (id, name, number_of_movies, average_popularity, average_rating) FROM stdin;
\.


--
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.genres (id, name) FROM stdin;
\.


--
-- Data for Name: keywords; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.keywords (id, word) FROM stdin;
\.


--
-- Data for Name: languages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.languages (id, name) FROM stdin;
\.


--
-- Data for Name: movie_credits; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.movie_credits (id, production_company_ids, director_id, actors, crew) FROM stdin;
\.


--
-- Data for Name: movie_social; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.movie_social (id, popularity, average_rating, revenue, budget, keywords) FROM stdin;
\.


--
-- Data for Name: movies_metadata; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.movies_metadata (id, title, original_title, collection_id, genres, language_id, release_date, runtime) FROM stdin;
1	Toy Story	Toy Story	8	{8,10,4}	5	1995-11-22	180
2	Captain America: Civil War	Civil War	1	{2,3,4}	5	2016-05-06	200
3	Captain America: The Winter Soldier	Winter Soldier	1	{2,3,4}	5	2014-12-15	190
4	Jurrasic World	Jurrasic World	2	{3,4,7}	5	2010-06-10	150
\.


--
-- Data for Name: overviews; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.overviews (movie_id, tagline, overview) FROM stdin;
\.


--
-- Data for Name: production_companies; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.production_companies (id, name) FROM stdin;
\.


--
-- Data for Name: ratings; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ratings (movie_id, rating) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

