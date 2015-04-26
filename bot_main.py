"""**********************************************************************************
    This project uses a RESTful API and JSON to implement Bitcoin trading strategies
    It is currently only meant for simulation and all purchases and PnL is performed
    using the program.

Author: Trey Huffine
*************************************************************************************"""

from TradingStrategies import *

# Initialize the program
print "Welcome to the Bitcoin trading bot (simulation only)\n"

while True:
    print "What strategy would you like to use:"
    print "  1. Moving Average"
    print "  2. Exponential Moving Average"
    print "  'Typing end' will terminate program"
    strategy = raw_input("Strategy: ")
    if strategy == "1":
        print "Using moving average"
        break
    elif strategy == "end":
        print "Program terminated"
        break
    else:
        print "\nNot a strategy. Try again or type 'end'.\n"

bot = TradingStrategies(strategy)

while True:
    break