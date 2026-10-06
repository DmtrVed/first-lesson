def two_sum_sorted(arr, target):
    for j in range(len(arr)-1,0,-1):
        for i in range(len(arr)-1):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
            else:
                return None
print(two_sum_sorted([1, 2, 3, 4, 5], 10))