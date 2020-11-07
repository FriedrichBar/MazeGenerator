from Affichage import *

Labyrinthe, celluleDepart = DFS(50, 50)
pixelsLabyrinthe = conversionLabyrintheAPixels(Labyrinthe, celluleDepart)
enregistrementLabyrinthe('Labyrinthe.png', pixelsLabyrinthe)