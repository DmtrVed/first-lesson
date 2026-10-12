def max_gap(numbers):
    if len(numbers) < 2:
        return 0
    numbers.sort()
    mx = 0
    for i in range(len(numbers)-1):
        mx1 = numbers[i+1]-numbers[i]
        if mx1>mx:
            mx = mx1            
    return mx