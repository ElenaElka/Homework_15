import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/animals/<x>')
def animals(x):
    with sqlite3.connect('animal.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
            SELECT *
            FROM data_animal_result
            LEFT JOIN data_outcomes ON data_outcomes.animal_id=data_animal_result.animal_id  
            WHERE data_animal_result.id  = {x}
        """

        cur.execute(sqlite_query)
        for row in cur.fetchall():
            row = {
              "animal_id": row[0],
              "animal_type": row[1],
              "name": row[2],
              "date_of_birth": row[3],
              "breed": row[4],
              "age_upon_outcome": row[5],
              "outcome_type": row[6],
              "outcome_month": row[7],
              "outcome_year": row[8],
              "outcome_subtype": row[9]
            }
        return jsonify(row)

app.run(debug=True)