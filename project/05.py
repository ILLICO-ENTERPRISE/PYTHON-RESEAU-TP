# Exercice sur les variables
# Apprendre à maitriser les liste compréhensions
# Apprendre à lire dans les fichiers
# Apprendre à manipuler les fonctions
import math


# Ecrire une fonction cleanFile() programme qui permet
#   Cette fonction prendra en paramètre le path du fichier
#   Ensuite lire le fichier files/lorem.txt
#   Puis supprimer tous les caractères suivants:
#       Les points (.)
#       Les points d'exclammation (!)
#       Les points d'interrogation (?)
#       Les virgules (,)
#       Les points virgules (;)
#       Les sauts a la ligne (\n)
# Après le nettoyage
# Ecrire une fonction main()
# Cette fonction main() ne prendra rien en paramètre
#   Elle devra changer la chaine de caractère retournée par la fonction cleanFile en liste de mots
#   Ainsi on obtiendra une Liste contenant tous les mots du fichier lorem.txt
#       Affecter la liste obtenue à la variable ListeMot
#   Après il va falloir modifier ListeMot comme suit:
#   En utilisant les listes compréhension et la fonction enumerate()
#       Remplacer le contenu de ListeMot par une liste de tuple dont les éléments sont comme suit:
#           ListeMot = [
#               (Mot1, longueur du mot1, index1),
#               (Mot2, longueur du mot2, index2),
#               (Mot3, longueur du mot3, index3),
#               .................................
#               .................................
#               (Mot4, longueur du mot4, index4),
#           ]
#       Ensuite une fois cette nouvelle liste ListeMot obtenue, il faudra:
#           Arranger cette liste selon le tuple dont la longueur de mot est plus élevée
#           Ensuite retourner à la fin de la fonction main() la nouvelle liste ordonée
# EN fin afficher la fonction main() dans print() car main() retourne une liste
# NB: Veuiller à respecter la syntaxe retenue en cours pour les fonctions
#   c-à-d de préciser les types des arguments en entrées et du type du résultat
# NB: Ecrivez un code clair et concis et pas de déclaration en plus


def cleanFile(filePath: str) -> str:
    # completer la fonction
    pass


def main() -> list:
    # completer la fonction
    pass


if __name__ == '__main__':
    print(main())
