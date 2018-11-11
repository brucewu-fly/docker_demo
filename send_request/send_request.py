#!/home/tops/bin/python
# -*- coding:utf-8 -*-

import urllib2
import time
import random


def send_request():
    endpoints = [
        "http://39.105.198.254:8088",
        "http://39.105.198.254:8089",
        "http://39.105.198.254:8090",
    ]
    path = [
        "/",
        "/examples",
        "/examples/servlets/servlet/HelloWorldExample",
        "/examples/servlets/servlet/RequestInfoExample",
        "/examples/servlets/servlet/RequestHeaderExample",
        "/examples/jsp/dates/date.jsp",
        "/manager/status",
        "/manager/html",
        "/host-manager/html",
        "/examples/jsp/jsp2/el/basic-arithmetic.jsp",
        "/not/found1",
        "/not/found2",
        "/not/found3",
        "/not/found4",
    ]
    while True:
        endpoints_r = random.randint(0, len(endpoints) - 1)
        path_r = random.randint(0, len(path) - 1)
        url = endpoints[endpoints_r] + path[path_r]
        req = urllib2.Request(url=url)
        try:
            urllib2.urlopen(req)
        except Exception as e:
            print e
        time.sleep(1)


send_request()
