def my_append(arr,i):
    return arr+[i]

def my_min(arr):
    nb_min = arr[0]
    for i in arr:
        if nb_min > i:
            nb_min = i
    return nb_min

def my_remove(arr,n):
    new_arr = []
    for i in arr:
        if i != n:
            new_arr = my_append(new_arr,i)
    return new_arr

def my_sort(arr):
    new_arr = []
    for _ in arr:
        new_arr = my_append(new_arr,my_min(arr))
        arr = my_remove(arr,my_min(arr))
    return new_arr

def my_int(arr):
    new_arr = []
    for i in arr:
        new_arr = my_append(new_arr,int(i))
        new_arr = my_sort(new_arr)
    return new_arr

arr = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(my_int(arr))