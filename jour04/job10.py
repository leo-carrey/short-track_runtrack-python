def produit():
    produit = 1
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    for i in L:
        if 25 <= i <= 90:
            produit *= i
    return produit

print(produit())