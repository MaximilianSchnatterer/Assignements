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
    # Entry action       
        if last_state is not state:
            self.all_off()
            last_state = state
        return last_state, state
    
    def red(self, last_state, state):
        # Entry action       
        if last_state is not state:
            self.all_off()
            last_state = state
            index = 0

        # Action: toggle. Leads to blink in same state
        self.toggle_led("red")
        index += 1

        # State guard
        if index == 10:
            state = States.ORANGE

        return last_state, state

    def orange(self, last_state, state):
            # Entry action       
        if last_state is not state:
            self.all_off()
            last_state = state
            index = 0

        # Action: toggle. Leads to blink in same state
        self.toggle_led("orange")
        index += 1

        # State guard
        if index == 10:
            state = States.GREEN
        
        return last_state, state

    def green(self, last_state, state):   
            # Entry action       
        if last_state is not state:
            self.all_off()
            last_state = state
            index = 0

        # Action: toggle. Leads to blink in same state
        self.toggle_led("green")
        index += 1

        # State guard
        if index == 10:
            state = States.RED

        return last_state, state

