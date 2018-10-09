import os
from _curses import flash

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from werkzeug.utils import secure_filename
import sqlite3 as sql

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'userUploads/')

print('upload', UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['jpg', 'txt'])

print('hdere: ', UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

@app.route('/')
def hello_world():
    path = session['path']
    print('path: ', path)
    return render_template('colorpicker.html', filename=path)

@app.route('/word', methods=['GET', 'POST'])
def word():
    if request.method == 'POST':
        word = request.form['word']
        session['word'] = word
        return redirect('/')
    return render_template('wordselect.html')


@app.route('/wordPick', methods=['POST'])
def wordPick():
    word = request.form['word']
    return render_template('wordselect.html', word=word)

@app.route('/uploadPhoto', methods=['GET', 'POST'])
def uploadPhoto():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print('requests: ', request.files['file'])
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('path: ', os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['photo'] = filename
            return redirect(url_for('uploadPhoto',
                                    filename=filename))
    return render_template('pickFile.html')

@app.route('/wordcolor')
def wordColor():
    print(request.args)
    print(request.query_string)
    val1 = '#' + request.args.get('val1')
    print(val1)
    val2 = '#' + request.args.get('val2')
    val3 = '#' + request.args.get('val3')
    val4 = '#' + request.args.get('val4')
    val5 = '#' + request.args.get('val5')
    colors = [val1, val2, val3, val4, val5]
    print(colors)
    word = session['word']
    return render_template('wordcolor.html', colors=colors, word=word)


@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = '../uploads/' + filename
    session['path'] = filename
    print(filename)
    images = os.listdir(os.path.join(app.static_folder, "images"))
    print(images)
    return render_template('pickFile.html', filename=filename, images=images)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/list')
def list():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "new_file")
    con = sql.connect(db_path)
    path = session['path']

    print('print: ', path)

    print('connection: ', con)

    con.execute("select * from information")

    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("insert into information(photopath, word, hexColor) VALUES ('../uploads/IMG_4574.jpg', 'beautiful', '#ffffff')")
    cur.execute("select * from information")


    rows = cur.fetchall();
    print('rows', rows)
    # print(len(rows))
    # print(rows[0]["photopath"])
    return render_template("userPhoto.html", rows=rows)


@app.route('/addPhoto', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


if __name__ == '__main__':
    app.run()
