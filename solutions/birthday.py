import random
def factorial(n):
    if n>=0:
        fact = 1
        otvet = 1
        for i in range(n):
            otvet *= fact
            fact +=1
        return otvet
    else:
        return None
def arrangements(n, k):
    if n>=k and n>=0 and k>=0:
        n1 = factorial(n)
        nk = factorial(n-k)
        return n1/nk
    else:
        return None

def birthday_probability(people):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
    prob_all_different = 1.0
    for i in range(people):
        prob_all_different *= (365 - i) / 365.0
    return 1.0 - prob_all_different
def simulate_birthday(people, trials=10000):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
    cnt = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            cnt += 1
    return cnt / trials

