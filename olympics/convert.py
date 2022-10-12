'''
    convert.py
    Author: Aaron Bronstone
    
    Link for Kaggle source data: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results
    Place csv files {athlete_events.csv && noc_regions.csv} in the same directory as convert.py before running
'''

import csv

def main():
    with open('athlete_events.csv') as athletes_read_file, open('noc_regions.csv') as noc_read_file:
        with open('athletes.csv','w',newline='') as athletes_file, open('sports.csv','w',newline='') as sports_file, open('nocs.csv','w',newline='') as noc_file, open('games.csv','w',newline='') as games_file, open('results.csv','w',newline='') as results_file:
            sport_reader = csv.reader(athletes_read_file,delimiter=',',quotechar='"')
            athlete_reader = csv.reader(athletes_read_file,delimiter=',',quotechar='"')
            sport_reader = csv.reader(athletes_read_file,delimiter=',',quotechar='"')
            games_reader = csv.reader(athletes_read_file,delimiter=',',quotechar='"')
            noc_reader = csv.reader(noc_read_file,delimiter=',',quotechar='"')

            athlete_writer = csv.writer(athletes_file)
            sport_writer = csv.writer(sports_file)
            games_writer = csv.writer(games_file)
            noc_writer =  csv.writer(noc_file)
            results_writer = csv.writer(results_file)

            athletes_visited = []
            games_visited = []
            sports_visited = []
            nocs_visited = []
            results=[]

            athlete_id=1
            sport_id=1
            game_id=1
            noc_id=1

            counter=0

            for row in noc_reader:
                if row[0] != 'NOC' and row[0] not in nocs_visited:
                    nocs_visited.append(row[0])
                    row.insert(0,noc_id)
                    noc_id+=1
                    noc_writer.writerow(row[0:3])

            for row in athlete_reader:
                if row[0]!='ID' and int(row[0]) not in athletes_visited:
                    id=int(row[0])
                    athletes_visited.append(id)
                    myrow=row[0:8]
                    complete_name = myrow[1].split(" ")
                    #print(full_name)
                    first_name = complete_name[0]
                    surname = 'NA'
                    if len(complete_name)>=2:
                        surname=complete_name[-1]
                    fullsurname=' '.join(complete_name[1:])
                    #print(fullsurname)
                    #print(first_name,' ',surname)
                    del myrow[1]
                    myrow.insert(1,fullsurname)
                    myrow.insert(1,surname)
                    myrow.insert(1,first_name)
                    myrow.insert(10,row[12])
                    
                    #myrow.insert(0,athlete_id)
                    #athlete_id+=1
                    athlete_writer.writerow(myrow)
                if row[13]!='Event' and row[13] not in sports_visited:
                    sports_visited.append(row[13])
                    myrow=row[12:14]
                    myrow.insert(0,sport_id)
                    sport_id+=1
                    sport_writer.writerow(myrow)
                if row[8]!='Games' and row[8] not in games_visited:
                    games_visited.append(row[8])
                    myrow=row[8:12]
                    myrow.insert(0,game_id)
                    game_id+=1
                    games_writer.writerow(myrow)
                if counter>0:
                    result=[row[0],games_visited.index(row[8])+1,sports_visited.index(row[13])+1,row[14]]
                    results_writer.writerow(result)
                counter+=1

main()