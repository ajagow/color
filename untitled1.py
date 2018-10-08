import os
from _curses import flash

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from requests import Session
from werkzeug.utils import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'userUploads/')

print('upload', UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['jpg', 'txt'])

print('hdere: ', UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    user = {'username': 'Miguel'}
    return render_template('colorpicker.html', title='Home', user=user)

@app.route('/word')
def word():
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
            Session['photo'] = filename
            return redirect(url_for('uploadPhoto',
                                    filename=filename))
    return render_template('pickFile.html')

@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = '../uploads/' + filename
    return render_template('pickFile.html', filename=filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
