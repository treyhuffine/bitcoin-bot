from numpy import *
from pandas import *

class TradingStrategies(object):
    # have separate variables for current value and time series
    def __init__(self, cash, trade_frequency, strategy):
        self.strategy = strategy
        self.cash = cash
        self.trade_frequency = trade_frequency

    def print_strategy(self):
        print self.strategy + "\n"

    def number_shares(self):
        # Track the number of shares/bitcoins owned
        pass

    def calculate_profit(self):
        # calculate running value and current value
        pass

    def calculate_cumulative_return(self):
        pass

    def calculate_trade(self):
        pass


class MovingAverage(TradingStrategies):
    spread = .025
    def __init__(self, cash, trade_frequency, ma_days):
        self.ma_days = ma_days
        TradingStrategies.__init__(self, cash, trade_frequency, "Moving Average")

    def calculate_trade(self):
        pass

    def calc_moving_average(price_series, ndays):
        return sum(price_series)/float(ndays)

    def moving_average_strategy(self, price_series, share0, spread, transaction_costs):
        N = 1
        ndays = size(price_series,1)
        P_0 = price_series[-1]
        moving_avg = self.calc_moving_average(price_series, ndays)

        # Calculate number of shares for MA
        if price_series[-1] > (moving_avg + spread*P_0):
            share_new = -1
        elif price_series[-1] < (moving_avg - spread*P_0):
            share_new = +1
        else:
            share_new = share0

        return share_new

