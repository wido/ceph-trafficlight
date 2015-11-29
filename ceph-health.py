#!/usr/bin/env python3

from trafficlight import TrafficLight
from enum import Enum
import urllib.request
import time
import json

#
# https://github.com/Crapworks/ceph-dash
#
dashboard_url = "http://url.to.my.ceph-dash/"

healthmap = {
    'HEALTH_OK': TrafficLight.Color.green,
    'HEALTH_WARN': TrafficLight.Color.orange,
    'HEALTH_ERR': TrafficLight.Color.red
}

def get_ceph_health(url):
    try:
        req = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
        resp = urllib.request.urlopen(req)
        body = resp.read()
        status = json.loads(body.decode("utf-8"))
        return status['health']['overall_status']
    except:
        return False

def main(url):
    curr = None
    try:
        light = TrafficLight()

        print("{0}: Starting up. Blinking lights".format(time.time()))

        for i in range(5):
            light.switch(TrafficLight.Color.green)
            time.sleep(0.2)
            light.switch(TrafficLight.Color.orange)
            time.sleep(0.2)
            light.switch(TrafficLight.Color.red)
            time.sleep(0.2)

        light.dark()

        while True:
            health = get_ceph_health(url)
            if health is not False:
                if curr != health:
                    print("{0}: {1}".format(time.time(), health))
                    color = healthmap.get(health)
                    light.switch(color)

            curr = health

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        light.dark()

if __name__ == '__main__':
    main(dashboard_url)
