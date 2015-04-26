class TradingStrategies(object):
    strategy = 1
    def __init__(self, strategy):
        self.strategy = int(strategy)

    def print_strategy(self):
        if self.strategy == 1:
            print "Moving average."