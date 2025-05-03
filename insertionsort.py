def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:  # ✅ Only swap when needed
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [7,3,2,1]
selection_sort(arr)
print(arr)
