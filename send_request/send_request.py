#!/home/tops/bin/python
# -*- coding:utf-8 -*-

import argparse
import random
import time
import urllib2


def send_request(endpoints):
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
        if endpoints_r % 2 == 0:
            req = urllib2.Request(url=url)
        else:
            req = urllib2.Request(url=url, data="xxx")
        try:
            urllib2.urlopen(req)
        except Exception as e:
            print e
        time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description="Send request.")
    parser.add_argument(
        "-e",
        "--endpoints",
        default=["tomcat1:8080", "tomcat2:8080", "tomcat3:8080"],
        type=str,
        nargs="+",
        help="Specify the endpoints.")

    args = parser.parse_args()
    print "The args are %s" % args
    send_request(args.endpoints)


if __name__ == '__main__':
    main()
