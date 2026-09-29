def factorial(n):
    if n>=0:
        fact = 1
        otvet = 1
        for i in range(n):
            otvet *= fact
            fact +=1
        return otvet
    else:
        return 0
def arrangements(n, k):
    if n>=k and n>=0 and k>=0:
        n1 = factorial(n)
        nk = factorial(n-k)
        return n1/nk
    else:
        return 0
def combinations(n, k):
    if n>=k and n>=0 and k>=0:
        n1 = factorial(n)
        k1 = factorial(k)
        nk = factorial(n-k)
        return n1/(k1*nk)
    else:
        return 0