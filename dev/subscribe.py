#to test run sudo sh setup.sh ; docker exec -it dev bash to close run sudo sh setdown.sh
#check that the particular attribute is set to poll

from PyTango import DeviceProxy
from PyTango import EventType
from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


if __name__ == "__main__":


    def callback(event):
        print("callback called:"+str(datetime.now()))
        if (event.err != "False"):
            print(event.attr_value.value)

    def subscribe(deviceName):
        pass
      #  proxy = DeviceProxy(deviceName)
     #   event_id = proxy.subscribe_event('Status', EventType.CHANGE_EVENT, callback, [], True)
       ## attr_list = proxy.get_attribute_list()
       ## for attr in attr_list:
       #     polling = proxy.get_attribute_poll_period(attr)#checks if attribute is subscribable
       #     if (polling > 0):
       #         event_id = proxy.subscribe_event(attr, EventType.CHANGE_EVENT, callback, [], True)

    #subscribe("sys/tg_test/1")
    app = Flask(__name__)  # create the application instance :)
    app.config.from_object(__name__)  # load config from this file , flaskr.py

    # Load default config and override config from an environment variable
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    tango_test = DeviceProxy("sys/tg_test/1")
    threadCount = 0
    event_id = tango_test.subscribe_event("Status", EventType.CHANGE_EVENT, callback, [], True)

    while 1:
        pass