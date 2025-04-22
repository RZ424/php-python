def somme_liste(liste):
    somme = 0
    for i in liste:
        somme = i + somme
    return somme

print(somme_liste([1, 2, 3, 4]))