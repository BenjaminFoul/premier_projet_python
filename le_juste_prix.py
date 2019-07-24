from random import randint

entier=randint(1,1000)

print("Bienvenue dans l'émission intitulée : LE JUSTE PRIX")

for nb_essais in range(1,11):
    print("\nIl vous reste",11-nb_essais, "essai(s)")
    entree = int(input("Entrez un prix :\n"))
    if nb_essais != 10:
        if entree<entier :
            print("C'est plus !")
        elif entree>entier :
            print("C'est moins !")
        else:
            break

if entree!=entier:
    print("\nC'est perdu ! Le juste prix était :",entier,"!")
else:
    print("Cest gagné !")

print("\nMerci d'avoir participé ! A bientôt dans le juste prix !")

