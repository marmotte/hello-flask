# -*- coding: utf-8 -*-
import logging
from flask import Flask


app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route('/')
def hello():
    app.logger.error("output error level message")
    app.logger.info("output info level message")
    return 'Hello Flask World'


@app.route('/health')
def health():
    return 'Health Check OK!!'
