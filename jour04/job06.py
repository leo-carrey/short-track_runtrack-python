def create_liste():
    L = [1, 2, 3, 4, 5]
    first = L[0]
    last = L[-1]
    L[0] = last
    L[-1] = first
    return L

print(create_liste())