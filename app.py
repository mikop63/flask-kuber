from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        author = request.form['author']
        text = request.form['text']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Notes (author, text, create_at) VALUES (%s, %s, %s)",
                    (author, text, datetime.now()))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('show_notes'))
    return render_template('create_note.html')

@app.route('/notes')
def show_notes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Notes ORDER BY create_at DESC")
    notes = cur.fetchall()
    cur.close()
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
