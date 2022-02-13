# Exercice sur les variables
# Apprendre à maitriser les liste compréhensions
import math

ListeA = [16.68, 98, 55, 100, 200]
ListeB = [
    (4, 5),
    (1, 10),
    (3, 33),
    (2, 48.88)
]

# Ecrire un programme qui permet
# De calculer la surface de chacun des cercles dont les rayons sont dans la ListeA
# 	Veuiller à enrégister dans la ListeA après calcul des surfaces la surface de chacun des cercle à la position correspondante à son rayon
# 		Il faudra en enrégistrant adopter ce format [(rayon, surface), (rayon, surface)]
# 		Exemple: Si on prenait une ListeX = [2, 4]
# 		Le résultat à obtenir est ListeX = [(2, surface pour r=2), (4, surface pour r=4)]
# 		Prenez soin d'utiliser PI = math.pi
# Ainsi une fois fini afficher la liste ListeA qui a changé
# 	Après ce la parcourez la liste B:
# 		Le format de la ListeB est la suivante:
# 			[(indexListeA, value), (indexListeA, value)]
# 			Donc ici ListeB est en Liste de Tuple contenant les index de la Liste A en position 0 des tuples et une valeur arbitraire en position 1
# 			Lors du parcours de la ListeB en fonction des indexes de la ListeA se trouvant en position 0 des tuples de la ListeB faire:
# 				La soustraction de la surface du cercle enrégistré dans ListeA en fonction de la valeur correspondante à l'indexe stocker dans ListeB à la position 0 du tuple correspondant
# 				et stocker les nouvelles valeurs dans ListeA
# 				Puis afficher la nouvelles ListeA
