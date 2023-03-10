def my_tapis(waist):
    count = 0
    print("+","-"*(waist+1),"+")
    for i in range(waist+1):
        print("|","#" * (waist - count),"#" * count,"|")
        count+=1
    print("+","-"*(waist+1),"+")

my_tapis(10)