from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import click
from PyTango import DeviceProxy
from PyTango import EventType
from datetime import datetime


def callback(event):
    print("callback called:"+str(datetime.now()))
    if (event.err != "False"):
        print(event.attr_value.value)


app = Flask(__name__) # create the application instance :)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
tango_test = DeviceProxy("sys/tg_test/1")
event_id = tango_test.subscribe_event("Status", EventType.CHANGE_EVENT, callback, [], True)

@app.route('/')
def getRoot():
    print("in getRoot ")
    return "hello world"





