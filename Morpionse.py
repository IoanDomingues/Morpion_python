import random

# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

# Fonction pour vérifier s'il y a une victoire
def verifier_victoire(plateau, joueur):
    for ligne in plateau:
        if all(case == joueur for case in ligne): # Vérification des lignes
            return True

    for colonne in range(3):
        if all(plateau[ligne][colonne] == joueur for ligne in range(3)): # Vérification des colonnes
            return True

    if all(plateau[i][i] == joueur for i in range(3)): # Vérification de la diagonale principale
        return True

    if all(plateau[i][2-i] == joueur for i in range(3)): # Vérification de la 2 ème diagonale
        return True

    return False

# Fonction pour le coup de l'ordinateur
def coup_ordinateur(plateau, joueur):
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = joueur
                if verifier_victoire(plateau, joueur):
                    return i, j
                plateau[i][j] = " "

    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = joueur
            break

# Fonction principale du jeu
def morpion():
    while True:
        plateau = [[" " for _ in range(3)] for _ in range(3)]
        joueurs = ["X", "O"]

        while True:
            afficher_plateau(plateau)
            ligne = int(input("Choisissez la ligne (0, 1, ou 2) : "))
            colonne = int(input("Choisissez la colonne (0, 1, ou 2) : "))

            if plateau[ligne][colonne] == " ":
                plateau[ligne][colonne] = joueurs[0]

                if verifier_victoire(plateau, joueurs[0]):
                    afficher_plateau(plateau)
                    print("Vous avez gagné !")
                    break

                if all(all(case != " " for case in ligne) for ligne in plateau):
                    afficher_plateau(plateau)
                    print("Match nul !")
                    break

                coup_ordinateur(plateau, joueurs[1])

                if verifier_victoire(plateau, joueurs[1]):
                    afficher_plateau(plateau)
                    print("L'ordinateur a gagné !")
                    break

                if all(all(case != " " for case in ligne) for ligne in plateau):
                    afficher_plateau(plateau)
                    print("Match nul !")
                    break

            else:
                print("Case déjà occupée, veuillez choisir une autre case.")

        rejouer = input("Partie terminée ! Souhaitez-vous recommencer ? (oui/non) ")
        if rejouer.lower() != "oui":
            break

morpion()
