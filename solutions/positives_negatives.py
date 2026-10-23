def count_positives_sum_negatives(numbers):
    posi = 0
    nega = 0
    if len(numbers) == 0:
        return []
    for i in range(len(numbers)):
        if numbers[i] > 0:
            posi += 1
        if numbers[i] < 0:
            nega += numbers[i]
    otvet = []
    otvet.append(posi)
    otvet.append(nega)
    return otvet