"""**********************************************************************************
    This project uses a RESTful API and JSON to implement Bitcoin trading strategies
    It is currently only meant for simulation and all purchases and PnL is performed
    using the program.  **Assuming ability to short Bitcoins.

Author: Trey Huffine
*************************************************************************************"""

from tradingstrategies import *
import sys

# Initialize the program
strategy = None
# use blockchain url that has daily historical prices in JSON
asset_url = "https://blockchain.info/charts/market-price?showDataPoints=false&timespan=all&show_header=true&daysAverageString=1&scale=0&format=json&address="

print "Welcome to the Bitcoin trading bot (simulation only)\n"

while True:
    print "What strategy would you like to use:"
    print "  1. Moving Average"
    print "  2. Exponential Moving Average"
    print "  Type 'all' to run all strats for comparison"
    print "  Typing 'end' will terminate program"
    strategy = raw_input("Strategy: ")
    if strategy == "1":
        print "Using moving average\n"
        strategy = int(strategy)
        break
    elif strategy == "end":
        sys.exit("\n** Program terminated! **\n")
    else:
        print "\nNot a currently available strategy. Try again or type 'end'.\n"

original_cash = 1000000 # $100,000 starting cash initially
cash = original_cash
trade_frequency = 60 * 60 * 24 # daily frequency initially
ma_days = 5
optimization_fit = 30 # currently unused

if strategy == 1:
    bot_ma = MovingAverage(cash, trade_frequency, ma_days)
    bot_ma.print_strategy()
else:
    sys.exit("\n** Strategy not yet available. Reload program.\n")

while True:
    break

"""
Append current time and return value to a ts of portfolio value
"""