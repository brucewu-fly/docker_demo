#!/home/tops/bin/python
# -*- coding:utf-8 -*-

import argparse
import random
import time
import urllib2


def send_request(endpoints):
    paths = [
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
    user_agents = [
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "Chrome",
        "FireFox",
        "FireFox",
        "FireFox",
        "Safari",
        "Safari",
        "Safari",
        "IE",
        "IE",
        "IE",
        "IE",
        "IE",
        "IE",
        "IE",
        "IE",
        "IE",
        "UC",
        "UC",
        "UC",
        "UC",
        "Dolphin",
        "Dolphin",
        "Dolphin",
        "Dolphin",
        "360",
        "360",
        "QQ",
        "QQ",
        "QQ",
        "QQ",
        "Sogou",
        "Sogou",
        "Sogou",
        "Sogou",
    ]
    referers = [
        "referer1",
        "referer1",
        "referer2",
        "referer2",
        "referer2",
        "referer2",
        "referer2",
        "referer2",
        "referer3",
        "referer3",
        "referer3",
        "referer3",
        "referer3",
        "referer4",
        "referer5",
        "referer6",
        "referer7",
        "referer7",
        "referer7",
        "referer8",
        "referer8",
        "referer8",
        "referer8",
        "referer9",
        "referer9",
    ]
    while True:
        endpoints_r = random.randint(0, len(endpoints) - 1)
        path_r = random.randint(0, len(paths) - 1)
        url = endpoints[endpoints_r] + paths[path_r]
        user_agent_r = random.randint(0, len(user_agents) - 1)
        referer_r = random.randint(0, len(referers) - 1)
        if endpoints_r % 2 == 0:
            req = urllib2.Request(url=url)
        else:
            req = urllib2.Request(url=url, data="xxx")
        req.add_header("User-Agent", user_agents[user_agent_r])
        req.add_header("Referer", referers[referer_r])
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
        default=["http://tomcat1:8080", "http://tomcat2:8080", "http://tomcat3:8080"],
        type=str,
        nargs="+",
        help="Specify the endpoints.")

    args = parser.parse_args()
    print "The args are %s" % args
    send_request(args.endpoints)


if __name__ == '__main__':
    main()
