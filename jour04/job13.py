def my_append(arr,i):
    return arr+[i]

def my_in(arr,n):
    for i in arr:
        if i == n:
            return True
    return False

def del_duplicate(arr):
    new_arr = []
    for i in arr:
        if not(my_in(new_arr,i)):
            new_arr = my_append(new_arr,i)
    return new_arr

arr = [1,2,7,8,1,9,8]
print(del_duplicate(arr))