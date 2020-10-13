from states import States
from led_states import LedStates
from button_control import ButtonControl

# Micropython specific modules
import br_timer


class Robot(object):

    def __init__(self, ticker_number, main_frequency):
        self.ticker_number = ticker_number
        self.main_frequency = main_frequency
        self.main_ticker = None

        self.led_states = LedStates()
        self.button_control = ButtonControl()

        self.last_state = None
        self.state = States.OFF
        self.state_machine = {
            States.OFF: self.led_states.off,
            States.RED: self.led_states.red,
            States.ORANGE: self.led_states.orange,
            States.GREEN: self.led_states.green
        }
        return


    def run(self):
        # Check if the button was invoked for a state update
        self.state = self.button_control.button_state_change(self.state)

        # Run the active state from the state machine
        self.last_state, self.state = self.state_machine[self.state](
            self.last_state, self.state)
        return


    def start(self):
        self.main_ticker = br_timer.ticker(self.ticker_number, self.main_frequency, self.run, True)
        self.main_ticker.start()
        return


    def stop(self):
        self.main_ticker.stop()
        return

