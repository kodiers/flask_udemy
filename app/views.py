from flask import render_template, request

from . import app


@app.route('/example', methods=['GET'])
def index():
    return render_template('index.html', example='first batch')
