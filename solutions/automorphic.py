def is_automorphic(n):
    a = n
    cnt = 1
    n1 = n
    cout = 1
    while a>=10:
            a //=10
            cnt+=1
    n1 **= 2
    for i in range(cnt):
          cout *= 10
    if n == n1 % cout:
        return True
    else:
        return False
