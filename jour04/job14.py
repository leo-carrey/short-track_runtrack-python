def my_append(arr,i):
    return arr+[i]

def my_split(string,n):
    new_arr=['']
    index=0
    for i in string:
        if i != n:
            new_arr[index]+=i
        else:
            index+=1
            new_arr=my_append(new_arr,"")
    return new_arr

def my_join(arr,n):
    new_string = ""
    for i in arr:
        new_string += i + n
    return new_string

def my_len(string):
    count = 0
    for _ in string:
        count+=1
    return count

def my_long_word(n,string):
    ArrForString = []
    new_arr = my_split(string, " ")
    for i in new_arr:
        if my_len(i) > n:
            ArrForString = my_append(ArrForString,i)
    return my_join(ArrForString, " ")[:-1]

print(my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))