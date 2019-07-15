from flask import render_template, request

from . import app
from .process_data import process, process_coins


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return request.form['cointype']
    return render_template('index.html', data=process(), process_coins=process_coins())
