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

    tango_test = DeviceProxy("sys/tg_test/1")
    event_id = tango_test.subscribe_event("Status", EventType.CHANGE_EVENT, callback, [], True)

    while 1:
        pass