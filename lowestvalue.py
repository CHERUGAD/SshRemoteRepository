My_array = [ 7,12,9,11,3 ]
min_value = My_array[0]
for i in My_array:
    if i < min_value:
        min_value = i
print("Minimum value is ",min_value)



#selection sort
My_array = [ 7,12,9,11,3 ]
n = len(My_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n) :
        if My_array[j] < My_array[min_index] :
            min_index = j
            min_value = My_array.pop(min_index)
            My_array.insert(i,min_value)

print("Minimum value sorting have been done by selection sort",My_array)