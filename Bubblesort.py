def bubbleSort(my_array):
    n = len(my_array)
    print(n)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if my_array[j] >= my_array[j+1]:
                my_array[j] ,my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped :
            break


my_array = [5,6,3,7,2,4]
bubbleSort(my_array)
print("Bubble sorted ",my_array)
        