# Exercice sur les variables
# Apprendre à maitriser les liste compréhensions
# Apprendre à lire dans les fichiers
# Apprendre à manipuler les fonctions
import math
import time


# Ecrire une fonction unStackThread()
#   Cette fonction aura pour but de simuler une PILE
#   Afin de remplir les conditions pour cette fonction
#       Ecrivez en premier une fonction du nom de askTask()
#           Cette fonction demandera à l'utilisateur d'entrer:
#               - Le nom d'une tâche
#               - Un nombre entier mais de manière unique
#               - Prenez le soin de vérifier qu'il entre un numéro unique
#   Sentez-vous libre d'utiliser l'approche la plus simple
#   Ecrivez une autre fonction du nom de askTasks()
#       Cette fonction répète askTask() cinq fois
#           Dans cette fonction boucler 5 fois sur la méthode askTask()
#           Puis enrégistré à chaque itération la liste retournée par askTask dans une liste tasks déclarée au tout début de la fonction
# Ensuite mettre les fonctions
#   Invoquer unStackThread()
#       Cette fonction prendra en paramètre la liste retournée par askTasks()


def unStackThread(tasks: list):
    tasks = sorted(
        tasks,
        reverse=True,
        key=lambda x: x[1]
    )
    while True:
        if len(tasks) > 0:
            print(f'------ {time.time()}')
            time.sleep(2)
            print(f'Task of name {tasks.pop()[0]} is treat')
        else:
            break


if __name__ == '__main__':
    # Completer la fonction
