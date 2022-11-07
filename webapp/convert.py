import csv

def main():
    #OPENING SOURCE CSV FILES
    with open('movies_metadata.csv') as metadata_file, open('credits.csv') as credits_file,open('keywords.csv') as keywords_file, open('links.csv') as links_file, open('links_small.csv') as links_small_file, open('ratings.csv') as ratings_file, open('ratings_small.csv') as ratings_small_file:
        #OPENING SOURCE CSV FILES
        #OPENING CONVERT CSV FILES
        with open('movie_metadata.csv','w',newline='') as metadata_convert_file, open('movie_credits.csv','w',newline='') as movie_credits_convert_file, open('movie_social','w',newline='') as movie_social_convert_file, open('collections.csv','w',newline='') as collections_convert_file, open('directors.csv','w',newline='') as directors_convert_file, open('overviews.csv','w',newline='') as overviews_convert_file, open('ratings_converted.csv','w',newline='') as ratings_convert_file, open('keywords_converted.csv','w',newline='') as keywords_convert_file, open('actors.csv','w',newline='') as actors_convert_file, open('crew.csv','w',newline='') as crew_convert_file, open('genres.csv','w',newline='') as genres_convert_file, open('languages.csv','w',newline='') as languages_convert_file, open('production_companies.csv','w',newline='') as production_companies_convert_file, open('production_countries.csv','w',newline='') as production_countries_convert_file:
        #OPENING CONVERT CSV FILES
            metadata_reader = csv.reader(metadata_file,delimiter=',',quotechar='"')
            credits_reader = csv.reader(credits_file,delimiter=',',quotechar='"')
            keywords_reader = csv.reader(keywords_file,delimiter=',',quotechar='"')
            links_reader = csv.reader(links_file,delimiter=',',quotechar='"')
            links_small_reader = csv.reader(links_small_file,delimiter=',',quotechar='"')
            ratings_reader = csv.reader(ratings_file,delimiter=',',quotechar='"')
            ratings_small_reader = csv.reader(ratings_small_file,delimiter=',',quotechar='"')

            metadata_writer = csv.writer(metadata_convert_file)
            credits_writer = csv.writer(movie_credits_convert_file)
            social_writer = csv.writer(movie_social_convert_file)
            collections_writer = csv.writer(collections_convert_file)
            directors_writer = csv.writer(directors_convert_file)
            overviews_writer = csv.writer(overviews_convert_file)
            ratings_writer = csv.writer(ratings_convert_file)
            keywords_writer = csv.writer(keywords_convert_file)
            actors_writer = csv.writer(actors_convert_file)
            crew_writer = csv.writer(crew_convert_file)
            genres_writer = csv.writer(genres_convert_file)
            languages_writer = csv.writer(languages_convert_file)
            production_companies_writer = csv.writer(production_companies_convert_file)
            prodcution_countries_writer = csv.writer(production_countries_convert_file)

            all_genres=[]

            for row in metadata_reader:
                new_row=[]
                current_genres=row[3]
                for genre in current_genres:
                    if genre not in all_genres:
                        all_genres.append(genre)

        
if __name__=='__main__':
    main()