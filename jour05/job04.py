def secret_message(string):
    arr=[]
    for i in string:
        if i in 'xyz':
            arr.append(chr(ord(i)-23))
        else:
            arr.append(chr(ord(i)+3))
    return ''.join(arr)

print(secret_message('bruhzyx'))