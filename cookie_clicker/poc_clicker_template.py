"""
Cookie Clicker Simulator
"""

# import simpleplot

# Used to increase the _timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

import math
import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_number = 0.0
        self._current_number = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return ("Total Number: {:.3e}\r\nCurrent Number: {:.3e}\r\n" + \
            "Time: {:.3e}\r\nCPS: {:.3e}")\
            .format(self._total_number, self._current_number, \
            self._time, self._cps)

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_number

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_number >= cookies:
            return 0.0
        return math.ceil((cookies - self._current_number) / self._cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time <= 0:
            return
        self._total_number += self._cps * time
        self._current_number += self._cps * time
        self._time += time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_number < cost:
            return
        self._current_number -= cost
        self._cps += additional_cps
        self._history.append((self._time, item_name, cost, self._total_number))


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    build_info = build_info.clone()
    clicker = ClickerState()
    while clicker.get_time() <= duration:
        item = strategy(clicker.get_cookies(), clicker.get_cps(), \
            duration - clicker.get_time(), build_info)
        if item == None:
            break
        cost = build_info.get_cost(item)
        time = clicker.time_until(cost)
        if clicker.get_time() + time > duration:
            break
        clicker.wait(time)
        clicker.buy_item(item, cost, build_info.get_cps(item))
        build_info.update_item(item)
    clicker.wait(duration - clicker.get_time())
    return clicker


def strategy_cursor(dummy_cookies, dummy_cps, dummy_time_left, \
    dummy_build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(dummy_cookies, dummy_cps, dummy_time_left, dummy_build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    This strategy should always select the cheapest item.
    """
    cheapest_item = None
    cheapest_cost = 0.0
    affordable_cost = cookies + cps * time_left
    for item in build_info.build_items():
        if (cheapest_item == None \
            or build_info.get_cost(item) < cheapest_cost) \
            and build_info.get_cost(item) <= affordable_cost:
            cheapest_item = item
            cheapest_cost = build_info.get_cost(item)
    return cheapest_item

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    This strategy should always select the most expensive item
    you can afford in the time left.
    """
    most_expensive_item = None
    most_expensive_cost = 0.0
    affordable_cost = cookies + cps * time_left
    for item in build_info.build_items():
        if (most_expensive_item == None \
            or build_info.get_cost(item) > most_expensive_cost) \
            and build_info.get_cost(item) <= affordable_cost:
            most_expensive_item = item
            most_expensive_cost = build_info.get_cost(item)
    return most_expensive_item

def strategy_best(cookies, cps, time_left, build_info):
    """
    This is the best strategy that you can come up with.
    """
    # return "Antimatter Condenser"
    my_choice = None
    max_rate = 0.0
    for item in build_info.build_items():
        if build_info.get_cost(item) <= cookies:
            my_choice = item
            break
        time_cost = math.ceil((build_info.get_cost(item) - cookies) / cps)
        if time_cost > time_left:
            continue
        cps_rate = build_info.get_cps(item) / cps
        time_rate = time_cost / time_left
        rate = cps_rate / time_rate
        if rate > max_rate:
            my_choice = item
            max_rate = rate
    return my_choice

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', \
    #    'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

# run()
