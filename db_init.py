import sqlite3

with open('league_results.csv', 'r') as file:
    conn = sqlite3.connect('league_results.db')
    conn.execute("DROP TABLE IF EXISTS league_results")
    conn.execute("CREATE TABLE league_results(" +\
    "[game_id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," +\
    "[home_team] TEXT NOT NULL, " +\
    "[away_team] TEXT NOT NULL, " +\
    "[home_goals] REAL NOT NULL, " +\
    "[away_goals] REAL NOT NULL, " +\
    "[result] VARCHAR(32) NOT NULL, " +\
    "[season] VARCHAR(32) NOT NULL)")

    first_row = True
    for row in file:
        if first_row:
            columns = row.rstrip().split(',')
            first_row = False
            columns[0] = 'home_team'
        else:
            values = row.rstrip().split(',')
            query = "INSERT INTO league_results(" + ",".join(columns) + ") VALUES(?, ?, ?, ?, ?, ?)"
            conn.execute(query, tuple(values))

conn.commit()
conn.close()
