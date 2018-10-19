from flask import render_template

from golovolomka import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blur/')
def blur():
    return render_template('blur.html')


@app.route('/battleships/')
def battleships():
    return render_template('battleships.html')
