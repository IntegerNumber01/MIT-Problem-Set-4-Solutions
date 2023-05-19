# Problem 2

# This first model is pretty simple. Clearly, the market does not grow at a
# constant rate. So a better model would be to account for variations in
# growth percentage each year.

# Write a function, called nestEggVariable, which takes three arguments:
# a salary (salary), a percentage of your salary to save (save), and a list of
# annual growth percentages on investments (growthRates). The length of the
# last argument defines the number of years you plan to work; growthRates[0]
# is the growth rate of the first year, growthRates[1] is the growth rate of
# the second year, etc. (Note that because the retirement fund’s initial value
# is 0, growthRates[0] is, in fact, irrelevant.) This function should return a
# list, whose values are the size of your retirement account at the end of
# each year.

# EQUATIONS

# End of year 1: F[0] = savings * (1 + 0.01 * growthRates[0]) - expenses
# End of year 2: F[1] = F[0] * (1 + 0.01 * growthRates[1]) - expenses
# End of year 3: F[2] = F[1] * (1 + 0.01 * growthRates[2]) - expense

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    storage = [(salary * save * 0.01)]
    for i in range(1, len(growthRates)):
        new = storage[i - 1] * (1 + 0.01 * growthRates[i]) + salary * save * 0.01
        storage.append(new)

    return storage


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.


testNestEggVariable()
