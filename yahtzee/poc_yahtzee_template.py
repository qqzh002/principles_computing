"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    scores = [0] * max(hand)
    for value in hand:
        scores[value - 1] += value
    return max(scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = range(1, num_die_sides + 1)
    all_sequences = gen_all_sequences(outcomes, num_free_dice)
    scores_sum = 0.0
    for sequence in all_sequences:
        scores_sum += score(held_dice + sequence)
    return scores_sum / len(all_sequences)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    return gen_all_holds_bigger_than(hand, 0)


def gen_all_holds_bigger_than(hand, base_value):
    """
    Helper for gen_all_holds.
    """
    values = set(hand)
    result = set([()])
    for value in values:
        if value < base_value:
            continue
        hand_list = list(hand)
        hand_list.remove(value)
        remain_hand = tuple(hand_list)
        for hold in gen_all_holds_bigger_than(remain_hand, value):
            result.add((value,) + hold)
    return result


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_value = 0.0
    max_hold = ()
    for hold in gen_all_holds(hand):
        expect = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if expect > max_value:
            max_value = expect
            max_hold = hold
    return (max_value, max_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, \
        "with expected score", hand_score


run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
