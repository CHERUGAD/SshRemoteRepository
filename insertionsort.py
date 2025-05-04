def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]      
        j = i - 1

        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key    

        # Print the array after each iteration
        print(f"After inserting {key}, array is: {arr}")

arr = [7, 3, 2, 1]
insertion_sort(arr)
print("Final sorted array:", arr)
