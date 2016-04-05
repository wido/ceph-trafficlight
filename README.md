# Ceph Traffic Light
This is a small piece of Python code which switches a real
traffic light based on the Ceph status:

* HEALTH_OK: Green
* HEALTH_WARN: Orange
* HEALTH_ERR: Red

It uses a Raspberry Pi and a Solid State Relais board from
Bitwizard: http://www.bitwizard.nl/wiki/index.php/Raspberry_Relay

## Dashboard
It fetches the information from the Ceph Dashboard project: https://github.com/Crapworks/ceph-dash
