import sqlite3

conn = sqlite3.connect("league_results.db")
cursor = conn.cursor()

game_id = 382
query = "DELETE FROM league_results WHERE game_id=?"
cursor.execute(query,(game_id, ))

conn.commit()
conn.close()