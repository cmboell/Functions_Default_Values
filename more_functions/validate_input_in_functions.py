"""
Assignment: Functions Default Values Assignment
Program: validate_input_in_functions.py
Author: Colby Boell
Last date modified: 02/20/2022

The purpose of this program is to use a function score_input() that takes parameters test_name, test_score,
and invalid_message that validates the test_score, then returns a string. Validates test score as well.i
"""


# function to validate score input where test_score is set to -1 as default
def score_input(test_name, test_score=-1):
    # sets test score as a string
    test_score = str(test_score)
    # if it starts with - then returns statement
    if test_score[0] == '-':
        return f'{test_name}: Invalid test score!'
    # or else if the score is numeric run this statement and return proper string
    elif test_score.isnumeric():
        if int(test_score) < 0 or int(test_score) > 100:
            return f'{test_name}: Invalid test score!'
        else:
            return f'{test_name}: {test_score}'
    # or else return error message
    else:
        return f'{test_name}: ValueError encountered!'


# main where we call function and print results
if __name__ == '__main__':
    # test for proper input
    display_string = score_input('Test 1', 70)
    print(display_string)
    # test for a numeric value below range
    display_string = score_input('Test 2', -70)
    print(display_string)
    # test for numeric value above range
    display_string = score_input('Test 3',  190)
    print(display_string)
    # test for a string instead of a number
    display_string = score_input('Test 4', 'hello')
    print(display_string)

"""
Test output:
Test 1: 70
Test 2: Invalid test score!
Test 3: Invalid test score!
Test 4: ValueError encountered!
"""
