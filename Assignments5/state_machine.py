from states import States
from led_states import LedStates
import br_timer

class Robot(object):
    def __init__(self, ticker_number, main_frequency):
        self.ticker_number = ticker_number
        self.main_frequency = main_frequency
        self.main_ticker = None
        
        return

