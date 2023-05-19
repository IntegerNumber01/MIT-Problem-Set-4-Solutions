# Problem 4

# Write a function, called findMaxExpenses, which takes five arguments:
# a salary (salary), a percentage of your salary to save (save), a list of
# annual growth percentages on investments while you are still working
# (preRetireGrowthRates), a list of annual growth percentages on investments
# while you are retired (postRetireGrowthRates), and a
# value for epsilon (epsilon). As with problems 2 and 3, the lengths of and
# postRetireGrowthRates determine the number of years you plan to be working
# and retired, respectively. Use the idea of binary search to find a value for
# the amount of expenses you can withdraw each year from your retirement fund,
# such that at the end of your retirement, the absolute value of the amount
# remaining in your retirement fund is less than epsilon (note that you can
# overdraw by a small amount). Start with a range of possible values for your
# annual expenses between 0 and your savings at the start of your retirement.
# Your function should print out the current estimate for the amount of
# expenses on each iteration through the binary search, and should return the
# estimate for the amount of expenses to withdraw.

# HINT 1: Start with a range of possible values for your annual expenses
# between 0 and your savings at the start of your retirement this can be
# determined by utilizing your solution to problem 2

# HINT 2:  your binary search should make use of your solutions to problem 3

# HINT 3: the answer should lie between zero and the initial value of the
# savings + epsilon.

import problem2 as p2
import problem3 as p3


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.

    savings = p2.nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    low = 0
    high = savings
    while abs(high - low) > epsilon:
        expenses = (low + high) / 2
        new_savings = p3.postRetirement(savings, postRetireGrowthRates, expenses)[-1]
        if new_savings < 0:
            high = expenses
        else:
            low = expenses

        expenses = (low + high) / 2

    return expenses


def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.


testFindMaxExpenses()
