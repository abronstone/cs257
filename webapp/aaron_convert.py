import csv
import json
import sys
import re

def get_metadata_as_python(read_file,write_file):
    dict = []
    with open(read_file) as read:
        with open(write_file,'w',newline='') as write:
            keyword_reader = csv.reader(read,delimiter=',',quotechar='"')
            keyword_writer = csv.writer(write)
            next(keyword_reader)
            for row in keyword_reader:
                words=row[1]
                python_words=eval(words)
                for word in python_words:
                    if word not in dict:
                        dict.append(word)
                        keyword_writer.writerow([word['id'],word['name']])
        write.close()
    read.close()
    return dict

def convert_collections(read_file,write_file):
    dict = []
    with open(read_file) as read:
        with open(write_file,'w',newline='') as write:
            collection_reader = csv.reader(read,delimiter=',',quotechar='"')
            collection_writer = csv.writer(write)
            next(collection_reader)
            for row in collection_reader:
                words=row[7]
                python_words=eval(words)
                for word in python_words:
                    if word not in dict:
                        dict.append(word)
                        collection_writer.writerow([word['id'],word['name']])
        write.close()
    read.close()
    return dict

def convert_list_for_sql(list):
    output = '{'
    for item in list:
        output+=item+','
    output+='}'
    return output
    
def write_unique_list(list,file):
    with open(file,'w',newline='') as write_file:
        writer=csv.writer(write_file)
        for dict in list:
            writer.writerow([dict['id'],dict['name']])
        write_file.close()



def main():
    #OPENING SOURCE CSV FILES
    with open('movies_metadata.csv') as metadata_file, open('credits.csv') as credits_file,open('keywords.csv') as keywords_file, open('links.csv') as links_file, open('links_small.csv') as links_small_file, open('ratings.csv') as ratings_file, open('ratings_small.csv') as ratings_small_file:
        #OPENING SOURCE CSV FILES
        #OPENING CONVERT CSV FILES
        with open('movie_metadata_convert.csv','w',newline='') as metadata_convert_file,open('movie_social_convert.csv','w',newline='') as social_convert_file:
            ''' open('movie_credits.csv','w',newline='') as movie_credits_convert_file, open('movie_social','w',newline='') as movie_social_convert_file, open('collections.csv','w',newline='') as collections_convert_file, open('directors.csv','w',newline='') as directors_convert_file, open('overviews.csv','w',newline='') as overviews_convert_file, open('ratings.csv','w',newline='') as ratings_convert_file, open('keywords.csv','w',newline='') as keywords_convert_file, open('actors.csv','w',newline='') as actors_convert_file, open('crew.csv','w',newline='') as crew_convert_file, open('genres.csv','w',newline='') as genres_convert_file, open('languages.csv','w',newline='') as languages_convert_file, open('production_companies.csv','w',newline='') as production_companies_convert_file, open('production_countries.csv','w',newline='') as production_countries_convert_file:
            #OPENING CONVERT CSV FILES
        '''
            metadata_reader = csv.reader(metadata_file,delimiter=',',quotechar='"')
            links_reader = csv.reader(links_file,delimiter=',',quotechar='"')
            links_small_reader = csv.reader(links_small_file,delimiter=',',quotechar='"')
            ratings_small_reader = csv.reader(ratings_small_file,delimiter=',',quotechar='"')

            metadata_writer = csv.writer(metadata_convert_file)
            social_writer = csv.writer(social_convert_file)
            '''
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
            '''
            '''
            all_keywords=[]
            headings=next(keywords_reader)
            line_number=1
            for row in keywords_reader:
                line_number+=1
                item_id,keywords_string=row[0],row[1]
                keywords_as_python=eval(keywords_string)
                for dict in keywords_as_python:
                    if dict['name'] not in all_keywords:
                        all_keywords.append(dict['name'])
            for word in all_keywords:
                print(word)
            '''

            movie_keywords_dictionary={}
            unique_keywords=[]
            keyword_names=[]   
            keywords_reader = csv.reader(keywords_file,delimiter=',',quotechar='"')
            next(keywords_reader)
            for row in keywords_reader:
                if row[1]!='':
                    current_words = eval(row[1])
                    current_word_id_list=[]
                    for word in current_words:
                        current_word_id_list.append(word['id'])
                        if word['name'] not in keyword_names:
                            keyword_names.append(word['name'])
                            unique_keywords.append(word)
                    movie_keywords_dictionary[row[0]]=current_word_id_list
            write_unique_list(sorted(unique_keywords,key=lambda d: d['id']),'keywords_convert.csv')

            # A list of dictionaries: {'id','name'} of unique keywords
            #keywords=sorted(get_metadata_as_python('keywords.csv','keywords_convert.csv'),key=lambda d: d['id']) 
            unique_collections=[]

            unique_genres=[]

            unique_languages=[]
            language_names=[]
            language_id=1

            unique_countries=[]
            country_names=[]
            country_id=1

            overviews=[]

            #Code to create CSV files for the values in the main movies_metadata.csv file that only have an id and a name (unique values)
            next(metadata_reader)
            for row in metadata_reader:
                if len(row)==24: #There exists a row that is only 10 long? We are opting to ignore this movie
                    movie_id,collection,genres,language,overview,countries = row[5],row[1],row[3],row[7],row[9],row[13]
                    if collection!='':
                        evaluated_collection=eval(collection)
                        formatted_collection={'id':evaluated_collection['id'],'name':evaluated_collection['name']}
                        if formatted_collection not in unique_collections:
                            unique_collections.append(formatted_collection)
                    if genres!='':
                        formatted_genres=eval(genres)
                        #print(formatted_genres)
                        for dict in formatted_genres:
                            if dict not in unique_genres:
                                unique_genres.append(dict)
                    if countries!='':
                        formatted_countries=eval(countries)
                        for dict in formatted_countries:
                            current={'id':country_id,'name':dict['iso_3166_1']}
                            if current['name'] not in country_names:
                                unique_countries.append(current)
                                country_names.append(current['name'])
                                country_id+=1
                    if language!='':
                        current={'id':language_id,'name':language}
                        if current['name'] not in language_names:
                            unique_languages.append(current)
                            language_names.append(current['name'])
                            language_id+=1
                    if overview!='':
                        current={'movie_id':movie_id,'overview':overview}
                        overviews.append(current)
                    
                     
            write_unique_list(sorted(unique_languages,key=lambda d: d['id']),'languages_convert.csv')
            write_unique_list(sorted(unique_countries,key=lambda d: d['id']),'countries_convert.csv')
            write_unique_list(sorted(unique_genres,key=lambda d: d['id']),'genres_convert.csv')
            write_unique_list(sorted(unique_collections,key=lambda d: d['id']),'collections_convert.csv')
            '''
            unique_keywords=[]
            keyword_names=[]
            with open('keywords_convert.csv','w',newline='') as keywords_convert_file:
                keywords_reader = csv.reader(keywords_file,delimiter=',',quotechar='"')
                keywords_writer = csv.writer(keywords_convert_file)
                next(keywords_reader)
                for row in keywords_reader:
                    if row[1]!='':
                        current_words = eval(row[1])
                        for word in current_words:
                            if word['name'] not in keyword_names[]:
                                keyword_names.append(word['name'])
                                unique_keywords.append(word)
            '''                
                    


            with open('overviews_convert.csv','w',newline='') as overviews_convert_file:
                overviews_writer = csv.writer(overviews_convert_file)
                for row in overviews:
                    overviews_writer.writerow([row['movie_id'],row['overview']])
                overviews_convert_file.close()

            #Creates a reformatted ratings csv file with only the movie id and the rating (timestamp seems irrelevant, and we are assuming 
            #there is only one rating per user per movie)
            with open('ratings_convert.csv','w',newline='') as ratings_convert_file:
                ratings_reader = csv.reader(ratings_file,delimiter=',',quotechar='"')
                ratings_writer = csv.writer(ratings_convert_file)
                next(ratings_reader)
                for row in ratings_reader:
                    ratings_writer.writerow([row[1],row[2]])
                ratings_convert_file.close()

            #id,popularity,revenue,budget,keywords
            print('writing social csv...')
            with open('movies_social_convert.csv','w',newline='') as social_convert_file:
                metadata_read = csv.reader(metadata_file,delimiter=',',quotechar='"')
                social_writer = csv.writer(social_convert_file)
                for movie in metadata_read:
                    id,popularity,revenue,budget=movie[5],movie[10],movie[15],movie[2]
                    keywords=convert_list_for_sql(movie_keywords_dictionary[id])
                    social_writer.writerow([id,popularity,revenue,budget])
                social_convert_file.close()
                    




            

            
            




            

                    





            


                
                

        
if __name__=='__main__':
    main()