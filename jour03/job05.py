def Check_Number(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def First_Number(n):
    for i in range(2,n):
        if Check_Number(i) == True:
            print(i)
    pass

First_Number(1000)