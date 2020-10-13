from states import States
from led_states import LedStates
import br_timer

class Robot(object):
    def __init__(self, ticker_number, main_frequency):
        self.ticker_number = ticker_number
        self.main_frequency = main_frequency
        self.main_ticker = None
        self.led_states = LedStates()
        self.last_state = None
        self.state = States.RED
        self.state_machine = {States.OFF : self.led_states.off, States.RED : self.led_states.red, States.ORANGE : self.led_states.orange, States.GREEN : self.led_states.green}
        return

    def run(self):
        self.last_state, self.state = self.state_machine[self.state](self.last_state, self.state)
        return

    def start(self):
        self.main_ticker = br_timer.ticker(self.ticker_number, self.main_frequency, self.run, True)
        self.main_ticker.start()
        return

    def stop(self):
        self.main_ticker.stop()
        return



