from enum import Enum
import RPi.GPIO as GPIO

class TrafficLight(object):
    """
    Traffic light control for a traffic Light connected to
    a RaspBerry Pi with GPIO board.

    This code is written for a Solid State Relais board
    from BitWizard from the Netherlands.

    Website: http://www.bitwizard.nl/
    Product Code: RPi-solid-state-relay

    This board has 4 SSRs and three are used for controlling
    a traffic light.
    """
    class Color(Enum):
        green = 1
        orange = 2
        red = 3

    relaymap = {
        Color.green: 11,
        Color.orange: 12,
        Color.red: 13
    }

    def __init__(self):
        self.prev = None
        GPIO.setmode(GPIO.BOARD)
        for light, id in self.relaymap.items():
            GPIO.setup(id, GPIO.OUT)

    def switch(self, color):
        try:
            relay = self.relaymap.get(color)

            if self.prev is not None and self.prev != relay:
                self.off(self.prev)

            if self.prev != relay:
                self.on(relay)

            self.prev = relay
        except:
            raise

    def on(self, relay):
        GPIO.output(relay, True)

    def off(self, relay):
        GPIO.output(relay, False)

    def dark(self):
        for light, id in self.relaymap.items():
            self.off(id)

    def __del__(self):
        GPIO.cleanup()
