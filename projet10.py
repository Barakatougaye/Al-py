#Question1
def recherche_binaire(A, l, h, k):
    if h >= l:
        mid = int(l + (h - l) / 2)
        
        if A[mid] == k:
            print("Vrai")  
            return 
        elif A[mid] > k:
            return recherche_binaire(A, l, mid - 1, k)  
        else:
            return recherche_binaire(A, mid + 1, h, k)  
    else:
        print("Faux")  

A = [1, 2, 3, 5, 8]
k1 = 6  
k2 = 5  

recherche_binaire(A, 0, len(A) - 1, k1)  
recherche_binaire(A, 0, len(A) - 1, k2)  


#Question2
def puissance(a, b):
    return a ** b

print(puissance(8, 4))  


#Question3
def tri_bulle(liste):
    n = len(liste)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
            j += 1
        i += 1

liste = [29, 13, 22, 37, 52, 49, 46, 71, 56]

tri_bulle(liste)
print(liste)



#Question 4
def tri_fusion(liste):
    if len(liste) > 1:
        milieu = len(liste) // 2  
        gauche = liste[:milieu]   
        droite = liste[milieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = j = k = 0
        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                liste[k] = gauche[i]
                i += 1
            else:
                liste[k] = droite[j]
                j += 1
            k += 1

        while i < len(gauche):
            liste[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            liste[k] = droite[j]
            j += 1
            k += 1

liste = [29, 13, 22, 37, 52, 49, 46, 71, 56]

tri_fusion(liste)
print(liste)



#Question 5
def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    premier = liste[0]
    gauche = []
    droite = []
    
    for x in liste[1:]:
        if x <= premier:
            gauche.append(x)
        else:
            droite.append(x)
    
    return tri_rapide(gauche) + [premier] + tri_rapide(droite)

liste = [29, 13, 22, 37, 52, 49, 46, 71, 56]

liste_triee = tri_rapide(liste)

print(liste_triee)
