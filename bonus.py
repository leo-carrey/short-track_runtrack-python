n = "je suis une string"
def find(n):
    for i in n:
        if i == "e":
            return True
        
print(find(n))