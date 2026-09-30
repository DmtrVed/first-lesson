def tetration(x, n):
    step = 1
    for i in range(n):
        step = x ** step
    return x
print(tetration(2, 3))