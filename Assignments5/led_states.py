from states import States
from machine import Pin

class LedStates(object):
    def __init__(self):
        self.leds = {"red" : Pin("B0", Pin.OUT),"orange" : Pin("E1", Pin.OUT), "green" : Pin("B14", Pin.OUT)}
        return

    def all_off(self):
        return

    def toggle_led(self):
        return

    def off(self):
        return
    
    def red(self):
        return

    def orange(self):
        return

    def green(self):        
        return

