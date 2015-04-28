from numpy import *
from trade_helper import *
import matplotlib
import matplotlib.pyplot as plt

"""
    Parent class all strategies will inherit from. Performs main rebalancing and tracks portoflio value.
"""
class TradingStrategies(object):
    # have separate variables for current value and time series
    def __init__(self, cash, trade_frequency, strategy):
        self.strategy = strategy
        self.cash = cash
        self.portfolio_val = None
        self.trade_frequency = trade_frequency
        self.current_shares = 0
        self.trade = 0
        self.num_shares = array([0])
        self.portfolio_series = array([cash])

    def print_strategy(self):
        print self.strategy + "\n"

    def number_shares(self, curr_price):
        total_to_own = self.portfolio_val * self.trade # in dollars
        change_shares = (total_to_own / curr_price) - self.current_shares
        self.cash = self.cash - (change_shares * curr_price)
        self.current_shares = (self.portfolio_val - self.cash) / curr_price
        self.num_shares = append(self.num_shares, self.current_shares)

    def portfolio_value(self, curr_price):
        self.portfolio_val = (self.current_shares * curr_price) + self.cash

    def value_series(self):
        self.portfolio_series = append(self.portfolio_series, self.portfolio_val)

    def cumulative_return(self, original_cash, current_value):
        return (current_value/original_cash) - 1

    def calculate_shares(self):
        pass

    def print_portfolio(self):
        print "Current value: ", self.portfolio_val

    def save_portfolio_to_file(self):
        fd = open('portfolio_values.csv','a')
        fd.write('%s,' % self.portfolio_val)
        fd.close()

    def plot_portfolio_value(self):
        print self.portfolio_series
        plt.plot(self.portfolio_series, 'b')
        plt.xlabel("Trade")
        plt.ylabel("Value ($)")
        plt.title("Portfolio Value")
        plt.savefig('portfolio_values')

"""
    For children, make purpose is to calculate number of shares to purchase given that strategy
    with all idiosincrecies involved with it

    execute_trade and calculate_shares is overwritten in each strategy
"""


class MovingAverage(TradingStrategies):
    spread = 0.01
    def __init__(self, cash, trade_frequency, ma_days):
        self.ma_days = ma_days
        TradingStrategies.__init__(self, cash, trade_frequency, "Moving Average")

    def execute_trade(self, price_series,curr_price):
        # perform all steps for the trade and calculating values
        self.portfolio_value(curr_price)
        self.value_series()
        self.calculate_shares(price_series)
        self.number_shares(curr_price)

    def calc_moving_average(self, price_series):
        return sum(price_series)/float(self.ma_days)

    # Calcutes shares to own for the moving average strategy
    def calculate_shares(self, price_series):
        N = 1
        P_0 = price_series[-1]
        moving_avg = self.calc_moving_average(price_series[-self.ma_days:])
        # Calculate number of shares for MA
        if price_series[-1] > (moving_avg + self.spread*P_0):
            share_new = -1
        elif price_series[-1] < (moving_avg - self.spread*P_0):
            share_new = +1
        else:
            share_new = self.trade

        self.trade = share_new


"""
    Implement the robust optimization technique via CVX
"""
class RobustOptimiztion(TradingStrategies):
    pass