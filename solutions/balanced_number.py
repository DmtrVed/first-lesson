def is_balanced_number(n):
    a=n
    cnt = 1
    sumr = 0
    suml = 0
    while a>=10:
        a //=10
        cnt+=1
    if cnt%2==0:
        for i in range(cnt//2-1):
            sumr += n%10
            n //=10
        for i in range(2):
            n //=10
        for i in range(cnt//2-1):
            suml += n%10
    elif cnt%2!=0:
        for i in range(cnt//2-1):
            sumr += n%10
            n //=10
        n //=10
        for i in range(cnt//2-1):
            suml += n%10
    if suml==sumr:
        return "Balanced"
    if suml!=sumr:
        return "Not Balanced"
print(is_balanced_number(56239814))