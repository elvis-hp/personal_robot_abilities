#!/usr/bin/env python

import zmq
import time


def send_zmq(json):
    c = zmq.Context()
    s = c.socket(zmq.PUSH)
    s.connect("tcp://localhost:1112")
    s.send_string(json)
    time.sleep(1)