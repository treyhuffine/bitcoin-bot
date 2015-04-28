"""**********************************************************************************
    This project uses a RESTful API and JSON to implement Bitcoin trading strategies
    It is currently only meant for simulation and all purchases and PnL is performed
    using the program.  **Assuming ability to short Bitcoins.

Author: Trey Huffine
*************************************************************************************"""

from numpy import *
from trade_helper import *
from tradingstrategies import *
import sys
import time

# Initialize the program
strategy = None
# use blockchain url that has daily historical prices in JSON
asset_url = "https://blockchain.info/charts/market-price?showDataPoints=false&timespan=all&show_header=true&daysAverageString=1&scale=0&format=json&address="

print "Welcome to the Bitcoin trading bot (simulation only)\n"


# Currently no partial share trading for moving average
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
    elif isinstance(strategy, basestring) and strategy.lower() == "__test":
        print "Entering test mode"
        break
    elif strategy == "end":
        sys.exit("\n** Program terminated! **\n")
    else:
        print "\nNot a currently available strategy. Try again or type 'end'.\n"

cash = 1000000 # $100,000 starting cash initially
trade_frequency = 60 * 60 * 24 # daily frequency initially
ma_days = 5
optimization_fit = 30 # currently unused

"""
    Initialize strategies
"""
if strategy == 1:
    bot_ma = MovingAverage(cash, trade_frequency, ma_days)
    bot_ma.print_strategy()
elif isinstance(strategy, basestring) and strategy.lower() == "__test":
    """
        Test scenario for debugging
    """
    bot_ma = MovingAverage(cash, trade_frequency, ma_days)
    bot_ma.print_strategy()
    price_series = array(random.normal(100, 10, ma_days))
    current_price = price_series[-1]
    while True:
        bot_ma.execute_trade(price_series, current_price)
        print "start sleep"
        time.sleep(1)
        print "end sleep"
        current_price = random.normal(100,10)
        price_series = append(price_series, current_price)
        print bot_ma.portfolio_val
        print bot_ma.current_shares
        print price_series
else:
    sys.exit("\n** Strategy not yet available. Reload program.\n")


"""*************************************************************************************************
    Main loop for bot trading.  Executes until canceled (currently daily trade frequency from init.
*************************************************************************************************"""

price_series = get_price_history(asset_url)
current_price = price_series[-1]
while True:
    price_series = get_price_history(asset_url)
    current_price = price_series[-1]
    bot_ma.execute_trade(price_series[0])
    time.sleep(1)
    current_price = get_current_price(asset_url)
    price_series = append_prices(price_series, current_price)
