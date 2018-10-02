from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    user = {'username': 'Miguel'}
    return render_template('colorpicker.html', title='Home', user=user)


if __name__ == '__main__':
    app.run()
