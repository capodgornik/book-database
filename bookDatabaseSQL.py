import sqlite3
import pandas as pd

def createTables(con, cur):
    
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS read (
            Title TEXT 
            Author TEXT 
            Series TEXT 
            Representation TEXT 
            Genre TEXT 
            Age TEXT 
            );
        """
    )
    
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tbr (
            Title TEXT 
            Author TEXT 
            Series TEXT 
            Representation TEXT 
            Genre TEXT 
            Age TEXT 
            );
        """
    )

    con.commit()
    
def sqlStuff():

    sqlDatabaseName = "books.db"
    con = sqlite3.connect(sqlDatabaseName)
    cur = con.cursor()
    cur.execute("DROP TABLE tbr;")
    
    excelFile = "Books.xlsx"
    dfRead = pd.read_excel(excelFile, sheet_name="Read", header=0)
    dfTBR = pd.read_excel(excelFile, sheet_name="TBR", header=0)
    dfRecommendations = pd.read_excel(excelFile, sheet_name="Recommendations", header=0)
    dfOwnedTBR = pd.read_excel(excelFile, sheet_name="Owned TBR", header=0)

    #print(dfTBR)
    
    createTables(con, cur)
    
    dfRead.to_sql('read', con, if_exists='replace', index=False)
    dfTBR.to_sql('tbr', con, if_exists='replace', index=False)
    
    #pd.read_sql("SELECT * FROM tbr LIMIT 5", con)
    
    cur.execute('''
        SELECT Author, Title FROM tbr LIMIT 5''')
    
    for row in cur.fetchall():
        print (row)    
        
    cur.execute('''
        SELECT Author, Title FROM read LIMIT 5''')    
    
    for row in cur.fetchall():
        print (row)  
    
    con.close()
    
def main():

    sqlStuff()
    
if __name__ == '__main__':
    main()