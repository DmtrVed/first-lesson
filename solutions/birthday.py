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
    return 1 - arrangements (365, people)/365 ** people
def simulate_birthday(people, trials):
    if people <= 1:
        return 0.0
    cnt = 0
    for _ in range(trials):
        birthdays = []
        for _ in range(people):
            birthdays.append(random.randint(1, 365))
        if len(birthdays) != len(set(birthdays)):
            cnt += 1
    return cnt / trials
'''& "C:\temp\my_venv\Scripts\python.exe" -m pytest "D:\univer python\first-lesson\tests" -v'''