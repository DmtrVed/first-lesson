def tetration(x, n):
    result = 1
    for _ in range(n):
        result = x ** result
    return result
print(tetration(5, 2))