
#
from flask import Flask, request, render_template
import sqlite3

#
app = Flask(__name__)

#
def init_db():

#
    with sqlite3.connect('data.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit()

#
@app.route('/', methods=['GET','POST'])
def index():
#
    if request.method == 'POST':

        name = request.form['name']

#
        with sqlite3.connect('data.db') as conn:
            conn.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit()

    return render_template('index.html')

#
if __name__ == '__main__':
    init_db()
    app.run(debug=True)