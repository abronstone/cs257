VIDINFO is a movie database full stack web application created by Aaron Bronstone and Jack Owens. 

In order to set up this application on your local machine, run through the following steps:

--------------------------------------------------------------------------

1.) Download the CSV files from Kaggle: 
	https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=links.csv

2.) Put the extracted CSV files into the 'convert' directory, and run both the following commands in the directory:
	python3 social_convert.py
	python3 credits_convert.py

3.) Create a new PSQL Database called 'webapp', and load the tables into the database using the following command:
	psql -U YOUR_USERNAME webapp < database-schema.sql

4.) Load each table with its corresponding '___convert.csv' file in PSQL:
	\copy TABLE_NAME from 'CONVERT_FILE.csv' CSV delimiter ',' quote '"';

5.) In the webapp directory, run the following command:
	python3 app.py

6.) Visit http://127.0.0.1:5000/ to view the website from your local machine. Enjoy!