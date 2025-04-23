def plus_grand_nombre(liste):
    max_nombre = liste[0]
    for i in liste:
        if i > max_nombre:
            max_nombre = i
    return max_nombre 

print(plus_grand_nombre([3, 57, 23, 56])) #hfhfgh

