#!/bin/bash
#
# Add to /etc/rc.local
#
# screen -dmS ceph /opt/ceph-trafficlight/run.sh
#
cd `dirname $0`

while [ true ]; do
    ./ceph-health.py
    sleep 60
done
