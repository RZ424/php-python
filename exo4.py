def factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat = i * resultat
    return resultat

print(factorielle(5)) # Affiche 120