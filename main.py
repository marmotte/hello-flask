# -*- coding: utf-8 -*-
import logging
import os
from flask import Flask, render_template, after_this_request
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime


HELLO_MESSAGE = os.environ.get('HELLO_MESSAGE')

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route('/')
def hello():
    message = 'Hello Flask World' if not HELLO_MESSAGE else HELLO_MESSAGE
    app.logger.error("output error level message")
    app.logger.info("ENV Val=%s" % message)

    @after_this_request
    def add_header(response):
        stamp = mktime(datetime.now().timetuple())
        response.headers['Last-Modified'] = format_date_time(stamp)
        response.cache_control.max_age = 300
        return response
    return render_template('index.html', message=message)


@app.route('/health')
def health():
    return 'Health Check OK!!'
