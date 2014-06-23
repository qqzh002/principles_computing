"""
Test suite for Cookie Clicker.
"""

import poc_simpletest as simpletest
import poc_clicker_template as clicker
from poc_clicker_provided import BuildInfo

def run_test():
    """
    Run test for ClickerState class.
    """

    suite = simpletest.TestSuite()

    a_clicker = clicker.ClickerState()
    suite.run_test(str(a_clicker), \
        "Total Number: 0.000e+00\r\nCurrent Number: 0.000e+00\r\n" + \
        "Time: 0.000e+00\r\nCPS: 1.000e+00", "Test #1a: __init__")
    suite.run_test(a_clicker.get_cookies(), 0.0, "Test #1b: __init__")
    suite.run_test(a_clicker.get_cps(), 1.0, "Test #1c: __init__")
    suite.run_test(a_clicker.get_time(), 0.0, "Test #1d: __init__")
    suite.run_test(len(a_clicker.get_history()), 1, "Test #1e: __init__")
    suite.run_test(a_clicker.get_history()[0], (0.0, None, 0.0, 0.0), \
        "Test #1f: __init__")

    suite.run_test(a_clicker.time_until(1.0), 1.0, "Test #2a: time_until")
    suite.run_test(a_clicker.time_until(2.5), 3.0, "Test #2b: time_until")

    a_clicker.wait(3)
    suite.run_test(str(a_clicker), \
        "Total Number: 3.000e+00\r\nCurrent Number: 3.000e+00\r\n" + \
        "Time: 3.000e+00\r\nCPS: 1.000e+00", "Test #3: wait")

    a_clicker.buy_item("Cursor", 15.0, 0.1)
    suite.run_test(str(a_clicker), \
        "Total Number: 3.000e+00\r\nCurrent Number: 3.000e+00\r\n" + \
        "Time: 3.000e+00\r\nCPS: 1.000e+00", "Test #4a: buy_item")
    suite.run_test(len(a_clicker.get_history()), 1, "Test #4b: buy_item")
    a_clicker.wait(12)
    a_clicker.buy_item("Cursor", 15.0, 0.1)
    suite.run_test(str(a_clicker), \
        "Total Number: 1.500e+01\r\nCurrent Number: 0.000e+00\r\n" + \
        "Time: 1.500e+01\r\nCPS: 1.100e+00", "Test #4c: buy_item")
    suite.run_test(a_clicker.get_history()[1], (15.0, "Cursor", 15.0, 15.0), \
        "Test #4d: buy_item")

    build_info = BuildInfo()
    a_clicker = clicker.simulate_clicker(build_info, clicker.SIM_TIME, \
        clicker.strategy_none)
    suite.run_test(str(a_clicker), \
        "Total Number: 1.000e+10\r\nCurrent Number: 1.000e+10\r\n" + \
        "Time: 1.000e+10\r\nCPS: 1.000e+00", "Test #5b: simulate_clicker")
    a_clicker = clicker.simulate_clicker(build_info, clicker.SIM_TIME, \
        clicker.strategy_cursor)
    suite.run_test(str(a_clicker), \
        "Total Number: 1.533e+11\r\nCurrent Number: 6.965e+09\r\n" + \
        "Time: 1.000e+10\r\nCPS: 1.610e+01", "Test #5b: simulate_clicker")

    a_clicker = clicker.simulate_clicker(\
        BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16, clicker.strategy_cursor)
    suite.run_test(str(a_clicker), \
        "Total Number: 6.600e+01\r\nCurrent Number: 1.391e+01\r\n" + \
        "Time: 1.600e+01\r\nCPS: 1.510e+02", "Test #5c: simulate_clicker")

    suite.run_test(clicker.strategy_cheap(2.0, 1.0, 1.0, \
        BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, \
            1.15)), None, "Test #6: strategy_cheap")

    suite.report_results()

    print type(a_clicker)

    # a_clicker = clicker.simulate_clicker(build_info, clicker.SIM_TIME, \
    #     clicker.strategy_cheap)
    # print a_clicker

    # a_clicker = clicker.simulate_clicker(build_info, clicker.SIM_TIME, \
    #     clicker.strategy_expensive)
    # print a_clicker

    # a_clicker = clicker.simulate_clicker(build_info, clicker.SIM_TIME, \
    #     clicker.strategy_best)
    # print a_clicker

run_test()
