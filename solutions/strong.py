import math
def is_strong(n):
    cnt = 1
    a = n
    n1 = n
    sum = 0
    while a>=10:
        a //=10
        cnt+=1
    for i in range(cnt):
        sum += math.factorial(n1%10)
        n1 //= 10
    if sum == n:
        return True
    else:
        return False