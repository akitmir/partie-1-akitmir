"""
Auteur: Ayman Kitmir
Matricule: 00048112
Date: 10/11/2019
Ce programme s'agit d'un jeu qui se nomme slideways mais pas complet, opposant 2 joueurs à s'affronter sur ce jeu.
Le but est d'avoir une ligne ou une colonne ou une diagonale complète du caractére d'un des deux joueurs.
Le joueur 1 joue les 'X' et le 2 les 'O'.
Ce code a été écrit dans le cadre du projet d'année du cours de programmation INFO F101(groupe 3).
"""




import os
def boucle_jeu():
        def afficher(M):
            """Affiche le plateau en transformant les entiers 0,1 et 2 en string"""

            os.system("cls"if os.name=="nt" else "clear") # Nettoie le terminal

            for i in range(len(M)):
                for j in range(len(M[i])):
                    if type(M[i][j]) == str:
                        print(M[i][j], end=' ')  # affiches les str espaçés de 1 des entiers
                    elif M[i][j]==0:
                        print("-", end=' ')
                    elif M[i][j]==1:
                        print("X", end=' ')
                    elif M[i][j]==2:
                        print("O", end=' ')
                print("\n", end='')

        def couleur_mise(a):
            """modifie un entier de la matrice par le numéro du joueur (1 ou 2) par rapport a la case choisie"""
            i = 4 - int(a[1])
            if a[0] == "A":
                j = 1
            elif a[0] == "B":
                j = 2
            elif a[0] == "C":
                j = 3
            elif a[0] == "D":
                j = 4
            plateau[i][j] = joueur

        def quelle_est_cette_case(a):
            """trouve quel est la case choisie par le joueur"""
            i = 4 - int(a[1])
            if a[0] == "A":
                j = 1
            elif a[0] == "B":
                j = 2
            elif a[0] == "C":
                j = 3
            elif a[0] == "D":
                j = 4
            return plateau[i][j]

        def verification_choix_du_joueur(a):
            """interrompt la partie si le joueur essaye de tricher ou se trompe en choisissant sa propre case ou une en
            dehors du plateau en lui expliquant son erreur et lui propose de reccomencer son choix,puis renvoie True si
            il s'est corrigé qui permet de continuer le jeu continue le jeu"""
            choix = False
            while choix != True:
                if len(a) == 2:
                    if a[0] >= "A" and a[0] <= "D":
                        if a[1] <= "4" and a[1] > "0":
                            if joueur == 1:
                                if quelle_est_cette_case(a) != 1:
                                    choix = True
                                    if a != choix_case_à_jouer2:
                                        choix = True
                                    else:
                                        print("Arretes de ticher on te voit, elle vient d'être jouer cette case,"
                                              " recommences:")
                                        a = str(input())
                                else:
                                    print("c'est ta case sal fou tu peux plus la modifier, recommences:")
                                    a = str(input())
                            elif joueur == 2:
                                if quelle_est_cette_case(a) != 2:
                                    choix = True
                                    if a != choix_case_à_jouer1:
                                        choix = True
                                    else:
                                        print("Arretes de ticher on te voit, elle vient d'être jouer cette case,"
                                              " recommences:")
                                        a = str(input())
                                else:
                                    print("c'est ta case sal fou tu peux plus la modifier, recommences:")
                                    a = str(input())
                        else:
                            print("La case que tu as choisis est en dehors du plateau, regardes bien le plateau et"
                                  " recommences khey:")
                            a = str(input())
                    else:
                        print("La case que tu as choisis est en dehors du plateau, regardes bien le plateau et"
                              " recommences khey:")
                        a = str(input())
                else:
                    print("lettre majusucule entre A et D, et un chiffre entre 1 et 4 à mettre, recommences")
                    a = str(input())
            return a




        def lignes(a, c):
            """vérifie si une des lignes est remplies du numéro du joueur(1 ou 2) ,renvoie True si oui, sinon renvoie
            False"""
            res=False
            for i in range(4):
               if a[i][1] == c:
                    if a[i][2] == c:
                        if a[i][3] == c:
                            if a[i][4] == c:
                                res = True
            return res




        def diagonales(a,c):
            """vérifie si une des diagonales est remplies du numéro du joueur(1 ou 2) renvoies True si oui, sinon renvoie
            False"""
            if a[0][1] == c:
                if a[1][2] == c:
                    if a[2][3] == c:
                        if a[3][4] == c:
                            res = True
                        else:
                            res = False
                    else:
                        res = False
                else:
                    res = False
            elif a[0][4] == c:
                if a[1][3] == c:
                    if a[2][2] == c:
                        if a[3][1]:
                            res = True
                        else:
                            res = False
                    else:
                        res = False
                else:
                    res = False
            else:
                res = False
            return res

        def colonnes(a, c):
            """verifie si une des colonnes est rempli du numéro du joueur(1 ou 2), renvoies True si oui, sinon renvoie
            False"""
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j] == c:
                        if a[i + 1][j] == c:
                            if a[i + 2][j] == c:
                                if a[i + 3][j] == c:
                                    res = True
                                else:
                                    res = False
                                return res

        def condition_de_victoire(a, c):
            """vérifie si un joueur a gagné, renvoie True si oui"""
            res = False
            if diagonales(a,c) or lignes(a,c) or colonnes(a,c) is True:
                 res = True
                 return res


        joueur = 1
        choix_case_à_jouer1=" "
        choix_case_à_jouer2=" "
        print("Bienvenue au Slideways de la hess")
        plateau = [["4", 0, 0, 0, 0], ["3", 0, 0, 0, 0], ["2", 0, 0, 0, 0], ["1", 0, 0, 0, 0],
                   [" ", "A", "B", "C", "D"]]
        afficher(plateau)
        le_gagnant=False
        while le_gagnant is not True:
            if joueur==1:
                choix_case_à_jouer1=str(input("Bonjour joueur 1, choisissez une case sur le plateau:"))
                choix_case_à_jouer1=verification_choix_du_joueur(choix_case_à_jouer1)
                couleur_mise(choix_case_à_jouer1)
                afficher(plateau)
                if condition_de_victoire(plateau,joueur) is True:
                    le_gagnant=True
                else:
                    joueur=2


            elif joueur==2:
                choix_case_à_jouer2=str(input("Bonjour joueur 2, choisissez une case sur le plateau:"))
                choix_case_à_jouer2=verification_choix_du_joueur(choix_case_à_jouer2)
                couleur_mise(choix_case_à_jouer2)
                afficher(plateau)
                if condition_de_victoire(plateau, joueur) is True:
                    le_gagnant = True
                else:
                    joueur = 1


        print("le joueur",joueur,"a gagné, félicitation.")

boucle_jeu()




