# Projet 2020 Maze Runner

## Promotion Cybersécurité du Logiciel 2020-2023

## Fonctionnement

`python3 ProjetLabyrinthe.py`

Le programme renvoie une image du labyrinthe nommée Labyrinthe.png.

La cellule rouge correspond au point d'arrivé, les cellules noires aux murs et les cellules blanches aux chemins.

L'utilisateur peut se déplacer en 8.

## Benchmark

Le programme de benchmark est inclus dans l'archive zip. Pour l'exécuter, il suffit de faire `python3 benchmark.py`.

L = Largeur

l = longueur

N = Nombre de cellules

| L | l   |N      | Temps | N/Temps|
|---|-----|-------|-------|--------|
|5  |5    |25     |0.0020s|12500   |
|25 |25   |625    |0.0560s|11160   |
|50 |50   |2500   |0.2149s|11633   |
|75 |75   |5625   |0.4898s|11484   |
|100|100  |10000  |0.8967s|11152   |
|150|150  |22500  |2.0102s|11192   |
|175|175  |30625  |2.7111s|11296   |
|200|200  |40000  |3.5317s|11326   |
|250|250  |62500  |5.6758s|11011   |
|300|300  |90000  |7.9880s|11267   |
|500|500  |250000 |22.693s|11016   |
|750|750  |562500 |51.054s|11017   |
|1000|1000|1000000|90.844s|11008   |

En comparant ces résultats avec un autre étudiant qui n'a pas utilisé numpy, nous nous rendons compte que nos temps de générations sont largement supérieurs.

Cela est notamment dû lors de la vérification des voisins. En effet, numpy.sum() est beaucoup plus lent que sum() pour des listes.


![alt text](https://i.ibb.co/PgDhr9R/np.png "Graphe vitesse")

Manquant de temps, j'ai décidé de rester sur cette solution avec numpy. Toutefois, cela peut rester intéressant si l'on souhaite comparer différents algorithmes.

## Complexité

Après notre benchmark, lorsque nous comparons les valeures de N/temps, nous nous rendons compte que plus N augmente, moins nous possédons de différence.

Nous en déduisons alors que notre programme possède une complexité égale à O(n).

## Auteur

Friedrich Bär