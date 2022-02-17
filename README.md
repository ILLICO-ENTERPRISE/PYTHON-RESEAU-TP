# PYTHON-RESEAU-TP

## Pré-requis
* [Langage SQL](https://sql.sh/)
* [Sqlite3](https://sqlitebrowser.org/dl/)
* [Python Sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [Table Plus](https://tableplus.com/)

```bash
pip install pysqlite3 
```


#### Creation de la base de données
* Créer une base de données du nom de <code>persons.db</code>
* Utiliser n'importe quel client de base de données puis connectez vous à votre base de données sqlite3
* Créer une table du nom de <code>persons</code> dans cette base de données, soit par requête SQL ou soit par l'interface de vôtre client SQL ou client de base de données
    * La table aura les colonnes suivantes:
        * <code>name</code>
        * <code>sex</code>
        * <code>age</code>
        * <code>country</code>
* Insérer deux valeurs dans la base de données à l'aide de vôtre client SQL et vérifier que les données s'enrégistrent correctement avant de passer à la suite du TP
* Faites et tester les requêtes de <code>SELECT</code> pour récupérer l'ensemble des données de la base de données. Ensuite écrivez la requête d'<code>INSERTION</code> des données dans la base de données.

#### Récupération des données depuis le fichier files/persons.txt
* Créer un fichier du nom de <code>module.py</code> dans lequel vous allez écrire les fonctions suivantes:
    * Une fonction du nom de <code>openFile()</code> qui prendra le path du fichier en paramètre et qui retournera le contenu du fichier
    * Ecrivez une autre fonction du nom de <code>unserialize()</code>, qui prend en paramètre une chaine de caractères et qui formate suivant les séparteurs contenus et renvoit une liste contenant des tuples se présentant comme suit:
        * (name1, sex1, age1, country1)
        * (name2, sex2, age2, country2)
        * (name3, sex3, age3, country3)
        * (nameN, sexN, ageN, countryN)
    * Ecrivez une autre fonction du nom de <code>main()</code>. Cette fonction ne prend rien en paramètre mais combine les fonctions ci-dessus comme suit: <code>unserialize(openFile(filename))</code> et retourne cette instruction.

#### Mise en place du serveur

Pour la mise en place du serveur copier le code ci après dans un fichier du nom de <code>server.py</code>:
```python3
#!/usr/bin/env python3
import socket
from module import *


def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(('', port))  # Écoute sur le port 50000
    serveur.listen(5)

    while True:
        client, infosClient = serveur.accept()
        print("Client connecté. Adresse " + infosClient[0])
        # Reçoit 1024 octets. Vous pouvez changer pour recevoir plus de données
        requete = client.recv(buffer)
        # decoder la reponse du client en utf-8
        print(requete.decode("utf-8"))
        reponse = "Connexion établie avec le serveur"
        client.send(reponse.encode("utf-8"))
        # time.sleep(2)
        client.close()
    serveur.close()


if __name__ == "__main__":
    openServer('127.0.0.1', 50000)
```

#### Mise en place du client

Pour la mise en place du client copier le code ci après dans un fichier du nom de <code>client.py</code>:

```python3
#!/usr/bin/env python3
import socket
import datetime


def openClientTunnel(host,
                     port,
                     buffer=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connexion au serveur de MPSI/ISI")
    print(f'Connexion faite à: {datetime.datetime.now()}')
    print(f'Connexion faite via le port: {port} à l\'adresse: {host}')
    # Customer send message to server
    client.send("Bonjour, je suis le client".encode("utf-8"))
    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    print("Connexion fermée")
    client.close()


if __name__ == '__main__':
    openClientTunnel("127.0.0.1", 50000)

```

#### Les consignes du TP
* Enrégistrer les données récuperer dans <code>module.py</code> dans la base de données:
    * Créer un fichier du nom de <code>database.py</code> dans lequel vous allez implémenter les fonctions participant à la connexion à la base de données sqlite3
        * Ecrivez une fonction du nom de <code>fetchDBB()</code>, qui initialise la connexion à la base de données.
        * Ecrivez une autre fonction du nom <code>getAllData()</code>, qui applique la requête <code>SELECT</code> ecrite au dessus, comme requete vers la base de données.
        * Ecrivez une autre fonction du nom de <code>insertData()</code>, qui va insérer la liste des personnes récupérées au nivreau de la fonction <code>main()</code> du module <code>module.py</code>
        * Puis envoyer cette liste à travers le tunnel de communication établie entre le serveur et le client dès que le client demande la connexion au serveur.