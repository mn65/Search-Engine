# This file is used to store our result 

# 1 we dont want to keep query in api if we have already
# 2 Build batter filter

import sqlite3 # Storing our all data in sqlite3
import pandas as pd # save data to database and use to manupulates with the datas 

class Database_storage(): # When we call this class this creates a table if it is not exists.

    # Use to make a connection to the database..?
    def __init__(self) -> None:
        self.con = sqlite3.connect("links.db")
        self.create_tables()

    # Use to create a tables in our database..
    def create_tables(self) -> None:
        cur = self.con.cursor() # Track what query runs on the database
        results_tables = r'''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                query TEXT,
                rank INTEGER,
                link TEXT,
                title TEXT,
                snippet TEXT,
                html TEXT,
                create DATETIME,
                relevance INTEGER,
                UNIQUE(query, link)
                
            )
        '''


        cur.execute(results_tables) # To create our database.
        self.con.commit() # Commits our changes to the database.
        cur.close()

    # Read data from the database.
    # when we pass query to this class it show all the data present in our database.
    def query_result(self, query): 
        df = pd.read_sql(f"select * from results where query= '{query}' order by rank asc;", self.con)
        return df
    
    # Insert a row and data to our database.
    def insert_row(self, values):
        # when we get results it store this to the database.
        cur = self.con.cursor() # here cursor is an object used to inetract with the querys on database.
        try:
            # used to execute sql
            # All the datas are inserted into the database after fromating by sqlite3 using VALUES(?,?,?,?,?,?,?) formate.
            cur.execute('INSERT INTO result (query, rank, link, snippet, html, created) VALUES(?,?,?,?,?,?,?)', values)
            self.con.commit() # Commits our changes to the database.

        except sqlite3.IntegrityError:
            pass

        cur.close()



    
