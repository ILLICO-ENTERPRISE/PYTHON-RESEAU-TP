# Exercice sur les variables
# Apprendre à maitriser les liste compréhensions
# Apprendre à lire dans les fichiers
# Apprendre à manipuler les fonctions
import math


# Ecrire une fonction calcMoy() qui:
#   Prend en paramètre une note de type float et le coefficient de type int
#   Puis retourne la note coefficiée
#   Utiliser cette fonction pour la calcul des notes coéfficiées dans bulidNote()
# Ecrire une fonction buildNote():
#   Cette fonction devra lire le fichier files/notes.txt
#       Le fichier files/notes.txt contient les informations:
#           - Sur le nom de l'étudiant
#           - Sur la note de l'étudiant
#           - Sur le coefficient à appliquer sur la note
#           Toutes ces informations sont groupées dans le fichier comme suit:
#               Nom etudiant,Note,Coefficient
#               Nom etudiant,Note,Coefficient
#               Nom etudiant,Note,Coefficient
#               Nom etudiant,Note,Coefficient
#   A vous de savoir comment récupérer les informations afin de respecter la question suivante.
#   Récupérer l'ensemble des éléments dans une liste de la manière suivante
#       Liste = [
#           (Nom étudiant, note, coefficient),
#           (Nom étudiant, note, coefficient),
#           (Nom étudiant, note, coefficient),
#           (Nom étudiant, note, coefficient),
#       ]
#   Après calculer la note coefficiée de chaque étudiant
#   Puis stocker cette note coefficiée dans La Liste de départ afin qu'on ait comme suit:
#       Liste = [
#           (Nom étudiant, note, coefficient, note coefficiée),
#           (Nom étudiant, note, coefficient, note coefficiée),
#           (Nom étudiant, note, coefficient, note coefficiée),
#           (Nom étudiant, note, coefficient, note coefficiée),
#       ]
# Ensuite calculer la moyenne de toute la classe
#   c-a-d de faire la somme de toutes les notes coefficiées divisée par la somme des coefficients
# Afficher ensuite le résultat de cette moyenne

if __name__ == '__main__':
    print(f'La moyenne de la classe est: {VotreReponse}')
