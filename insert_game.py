import sqlite3

conn = sqlite3.connect("league_results.db")
cursor = conn.cursor()

home_team = 'POLSKA'
away_team = 'NIEMCY'
home_goals = 4.
away_goals = 2.
result = 'H'
season = '2018/2019'
query = "INSERT INTO league_results(home_team, away_team, home_goals, away_goals, result, season) VALUES ( ? , ? , ? , ? , ?, ? )"
ret = cursor.execute(query, (home_team, away_team, home_goals, away_goals, result, season))
print(ret.lastrowid)

conn.commit()
conn.close()
