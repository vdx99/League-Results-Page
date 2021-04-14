import sqlite3

conn = sqlite3.connect("league_results.db")
cursor = conn.cursor()

game_id = 2
home_team = 'Watford'
query = "UPDATE league_results SET home_team=? WHERE game_id = ?"
ret = cursor.execute(query, (home_team, game_id))
print(ret.lastrowid)

conn.commit()
conn.close()
