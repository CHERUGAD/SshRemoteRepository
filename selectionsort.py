def selectionsort(my_array) :
    n = len(my_array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n ):
            if my_array[j] < my_array[min_index] :
                min_index = j
        if min_index != i:
                my_array[i],my_array[min_index] = my_array[min_index], my_array[i]

my_array = [ 7, 12, 9, 11, 3]
selectionsort(my_array)
print("Using Selection sort  ",my_array)