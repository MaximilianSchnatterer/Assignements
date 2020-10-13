from states import States
from machine import Pin

class LedStates(object):
    def __init__(self):
        self.leds = {"red" : Pin("B0", Pin.OUT),"orange" : Pin("E1", Pin.OUT), "green" : Pin("B14", Pin.OUT)}
        return

    def all_off(self):
        for pin in self.leds.values():
            pin.value(0)
        return

    def toggle_led(self, key):
        if self.leds[key].value() == False:
            self.led[key].value(1)
        else:
            self.led[key].value(0)
        return

    def off(self, last_state, state):
        return last_state, state
    
    def red(self, last_state, state):
        return last_state, state

    def orange(self, last_state, state):
        return last_state, state

    def green(self, last_state, state):        
        return last_state, state

