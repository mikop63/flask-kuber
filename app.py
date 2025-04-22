import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder=None)
app.config['UPLOAD_FOLDER'] = '/resource'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 МБ

# MySQL из config.py
import config
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
        filename = None

        file = request.files.get('file')
        if file and file.filename:
            ext = os.path.splitext(file.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
            file.save(path)

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Notes (author, text, file_name, create_at) VALUES (%s, %s, %s, %s)",
            (author, text, filename, datetime.now())
        )
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

@app.route('/resource/<filename>')
def uploaded_file(filename):
    return send_from_directory('/resource', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
