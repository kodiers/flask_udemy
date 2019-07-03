from flask import render_template, request

from . import app
from .process_data import process


@app.route('/example', methods=['GET'])
def index():
    return render_template('index.html', data=process())
