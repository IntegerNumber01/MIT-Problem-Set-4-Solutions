# Problem 3

# Write a function, called postRetirement, which takes three arguments: an
# initial amount of money in your retirement fund (savings), a list of annual
# growth percentages on investments while you are retired (growthRates), and
# your annual expenses (expenses).  Assume that the increase in the investment
# account savings is calculated before subtracting the annual expenditures
# (as shown in the above table). Your function should return a list of fund
# sizes after each year of retirement, accounting for annual expenses and the
# growth of the retirement fund. Like problem 2, the length of the growthRates
# argument defines the number of years you plan to be retired.

# EQUATIONS:

# End of year 1: F[0] = savings * (1 + 0.01 * growthRates[0]) - expenses
# End of year 2: F[1] = F[0] * (1 + 0.01 * growthRates[1]) - expenses
# End of year 3: F[2] = F[1] * (1 + 0.01 * growthRates[2]) - expense

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.

    storage = [savings * (1 + 0.01 * growthRates[0]) - expenses]
    for i in range(1, len(growthRates)):
        new = storage[i - 1] * (1 + 0.01 * growthRates[i]) - expenses
        storage.append(new)

    return storage


def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.


testPostRetirement()
