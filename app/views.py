from flask import render_template, request

from . import app
from .process_data import process, process_coins


@app.route('/', methods=['GET', 'POST'])
def index():
    entered_coin = 'bitcoin'
    if request.method == 'POST':
        entered_coin = request.form['cointype']
    return render_template('index.html', data=process(entered_coin), process_coins=process_coins(),
                           entered_coin=entered_coin)
