def inverser_chaine(chaine):
    chaine_inversee = ''
    for i in range(len(chaine)):
        chaine_inversee = chaine[i] + chaine_inversee
    return chaine_inversee

print(inverser_chaine("Bonjour")) # Affiche "ruojnoB"