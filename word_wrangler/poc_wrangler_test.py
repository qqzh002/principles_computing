"""
Test suite for Word Wrangler game
"""

import poc_wrangler as wrangler
from poc_simpletest import TestSuite

def run_test():
    """
    Run test suite for Word Wrangler game
    """

    suite = TestSuite()

    suite.run_test(wrangler.remove_duplicates([1, 2, 2, 3, 4, 5]), \
        [1, 2, 3, 4, 5], "Test #1: remove_duplicates")

    suite.run_test(wrangler.intersect([1, 2, 3], [3, 4, 5]), [3], \
        "Test #2a: intersect")
    suite.run_test(wrangler.intersect([3, 4, 5], [3, 4, 5]), [3, 4, 5], \
        "Test #2b: intersect")

    suite.run_test(wrangler.merge([1, 2, 3], [3, 4, 5]), [1, 2, 3, 3, 4, 5], \
        "Test #3: merge")

    suite.run_test(wrangler.merge_sort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5], \
        "Test #4: merge_sort")

    suite.run_test(wrangler.merge_sort(wrangler.gen_all_strings("aab")), \
        wrangler.merge_sort(["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", \
            "aa", "aab", "aab", "aba", "aba", "baa", "baa"]), \
        "Test #5: gen_all_string")

    # print wrangler.load_words(wrangler.WORDFILE)

    suite.report_results()

run_test()
