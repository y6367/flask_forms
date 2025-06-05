# Importing flask, request, render_template library
from flask import Flask, request, render_template
import sqlite3

# Creating flask
app = Flask(__name__)

# Initalize the SQL database
def init_db():

# Connect to data.db database file
    with sqlite3.connect('data.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit()

# Define route for the homepage that supports both GET and POST requests
@app.route('/', methods=['GET','POST'])
def index():
# If form is submitted as a POST request
    if request.method == 'POST':

        name = request.form['name']

# Append the name into the database file
        with sqlite3.connect('data.db') as conn:
            conn.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit()

    return render_template('index.html')

# Run the file
if __name__ == '__main__':
    init_db()
    app.run(debug=True)