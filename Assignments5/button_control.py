from machine import Pin
from states import States


class ButtonControl(object):

    def __init__(self):
        self.is_pressed = False
        self.button = Pin('C13', Pin.IN)
        self.button.irq(self.callback, Pin.IRQ_FALLING)
        return


    def callback(self, pin):
        self.is_pressed = True
        print('Button Press')
        return


    def button_state_change(self, state):
   
        # Return RED if OFF and button was pressed. Return OFF otherwise.
        if self.is_pressed:
            self.is_pressed = False
            if state is States.OFF:
                return States.RED
            else:
                return States.OFF

        return state
