def two_sum_sorted(arr, target):
    for j in range(len(arr)-1,0,-1):
        for i in range(len(arr)-1):
            if arr[i] == arr[j]:
                return arr[i], arr[j]