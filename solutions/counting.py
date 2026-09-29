def factorial(n):
    if n>=0:
        fact = 1
        otvet = 1
        for i in range(n):
            otvet *= fact
            fact +=1
        return otvet
    else: return None
def arrangements(n, k):
    if n<k or n<0 or k<0: return 0
    n1 = factorial(n)
    nk = factorial(n-k)
    return n1/nk
def combinations(n, k):
    if n<k or n<0 or k<0: return 0
    n1 = factorial(n)
    k1 = factorial(k)
    nk = factorial(n-k)
    return n1/(k1*nk)
print(arrangements(-1, 2))
