from itertools import product

def are_equivalent(f, g, n):
    for row in product([0, 1], repeat=n):
        if f(*row) != g(*row):
            return False
    return True

def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def de_morgan2_right(a,b):
    return (not a) and (not b)

def de_morgan2_left(a,b):
    return not(a or b)

def wrong(a, b):
    return (not a) and (not b)

def implies(a,b):
    return (not a) or b

def impl_left(a,b):
    return implies(a,b)

def impl_right(a,b):
    return (not a) or b

def contrap_right(a,b):
    return implies(not b, not a)

def contrap_left(a,b):
    return implies(a,b)

def dist_left(a, b, c):
    return a or (b and c)

def dist_right(a, b, c):
    return (a or b) and (a or c)

if __name__ == "__main__":
    print(are_equivalent(de_morgan_left, de_morgan_right, 2))
    print(are_equivalent(de_morgan2_left, de_morgan2_right, 2))
    print(are_equivalent(impl_left, impl_right, 2))
    print(are_equivalent(contrap_left, contrap_right, 2))
    print(are_equivalent(dist_left, dist_right, 3))