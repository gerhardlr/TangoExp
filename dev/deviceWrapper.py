from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import click
from PyTango import DeviceProxy
from PyTango import EventType
from datetime import datetime

app = Flask(__name__) # create the application instance :)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.cli.command('setDevice')
@click.argument('devname')
def setdevice(devname):
    print("setting device Name as: "+ devname)
    g.devName = devname

@app.route('/')
def getRoot():
    print("in getRoot (devname = "+g.devname+")")


