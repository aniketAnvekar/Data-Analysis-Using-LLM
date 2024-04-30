import sqlite3
import pandas as pd

# Import the dataframe
data = pd.read_csv('Final_data.csv')
data = data.drop(columns=['Unnamed: 0'])
print(data.info())

## Connect to sqlite
connection = sqlite3.connect("movies.db")


# ## Creata cursor object to execute sql queries
cursor = connection.cursor()


# ## Deisgning the schema by creating movies table
table_schema = """
CREATE TABLE Movies (
    Movie_Name TEXT,
    Release_Yr INTEGER,
    Movie_Rating TEXT,
    Duration TEXT,
    IMDb_Rating REAL,
    Popularity INTEGER,
    Genre TEXT,
    Movie_Desc TEXT,
    Director TEXT,
    Writers TEXT,
    Movie_stars TEXT,
    Oscars_Won INTEGER,
    Awards_Won INTEGER,
    Nominations INTEGER
);
"""

cursor.execute(table_schema)

# Store the DataFrame in the SQLite database
data.to_sql('Movies', connection, if_exists='append', index=False)

# Commit changes
connection.commit()

#Displaying all the records in movies.db
data = cursor.execute('''Select Writers from Movies''')

for row in data:
    print(row)
    
connection.close()