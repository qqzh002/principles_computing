"""
Test suite for Zombie class.
"""

from poc_simpletest import TestSuite
import poc_zombie_template

def run_test():
    """
    Run tests for Zombie class
    """

    suite = TestSuite()

    zombie = poc_zombie_template.Zombie(4, 6, None, [(1, 5), (3, 2)])
    suite.run_test(zombie.compute_distance_field(poc_zombie_template.ZOMBIE), \
        [[5, 4, 3, 3, 2, 1], [4, 3, 2, 2, 1, 0], \
        [3, 2, 1, 2, 2, 1], [2, 1, 0, 1, 2, 2]], \
        "#Test 1a: compute_distance_field")

    zombie = poc_zombie_template.Zombie(4, 6, [(1, 2)], [(1, 5), (3, 2)])
    suite.run_test(zombie.compute_distance_field(poc_zombie_template.ZOMBIE), \
        [[5, 4, 4, 3, 2, 1], [4, 3, 2, 2, 1, 0], \
        [3, 2, 1, 2, 2, 1], [2, 1, 0, 1, 2, 2]], \
        "#Test 1b: compute_distance_field")

    suite.report_results()

run_test()
