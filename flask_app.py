import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)

@app.route('/league_results')
def get_results():
    conn = sqlite3.connect('league_results.db')
    cursor = conn.cursor()
    query = "SELECT * FROM league_results"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()

    return render_template('league_results.html', data=data)


@app.route('/update_league_results/<int:id>', methods=["GET"])
def update_results(id):
    try:
         conn = sqlite3.connect('league_results.db')
         cursor = conn.cursor()
         query = "SELECT * FROM league_results where game_id=?"
         cursor.execute(query, (id, ))
         data = cursor.fetchall()
         conn.commit()
         conn.close()
         return render_template('league_results_update.html', data=data[0])
    except Exception as err:
        return "Error! " + str(err), 500

@app.route('/update_league_results', methods=["POST"])
def update_results_db():
    try:
         game_id = int(request.form['game_id'])
         home_team = request.form['home_team']
         away_team = request.form['away_team']
         home_goals = float(request.form['home_goals'])
         away_goals = float(request.form['away_goals'])
         result = request.form['result']
         season = request.form['season']

         conn = sqlite3.connect('league_results.db')
         cursor = conn.cursor()
         query = "UPDATE league_results SET home_team=?, " + \
         "away_team=?," + \
         "home_goals=?," + \
         "away_goals=?," + \
         "result=?," + \
         "season=? WHERE game_id=?"
         cursor.execute(query, (home_team, away_team, home_goals, away_goals, result, season, game_id))
         conn.commit()
         conn.close()
         return redirect(url_for('get_results'))
    except Exception as err:
            return "Error! " + str(err), 500






if __name__ == '__main__':
    app.run()