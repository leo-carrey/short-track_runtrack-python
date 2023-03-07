def positif(nombre):
    if nombre < 0:
        return "negatif"
    elif nombre > 0:
        return "positif"
    
print(positif(5))
print(positif(-5))