alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def Pyramide(n):
    new_arr=[]
    for i in n:
        new_arr.append(i)
        finish_str = "".join(new_arr)
        print(finish_str)

Pyramide(alphabet)