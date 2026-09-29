from itertools import product
def truth_table(n):
    return list(product([0, 1], repeat=n))