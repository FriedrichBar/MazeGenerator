from ImagesUtils import empty_img, write_img
from Labyrinthe import *

def conversionLabyrintheAPixels(Labyrinthe, celluleDepart):
    """
    Convertis un labyrinthe(matrice) en pixels

    IN: Labyrinthe(matrice)

    OUT: pixels
    """
    celluleDepartX = celluleDepart[0]
    celluleDepartY = celluleDepart[1]
    # Récupération de la taille du labyrinthe
    pixels = empty_img(len(Labyrinthe), len(Labyrinthe[0]))
    for x in range(len(pixels)):
        for y in range(len(pixels[x])):
            for z in range(len(pixels[x][y])):
                # Si c'est un mur
                if Labyrinthe[x][y] == 0:
                    pixels[x][y][z] = 0
                # Si c'est un chemin
                if Labyrinthe[x][y] == 1:
                    pixels[x][y][z] = 255
    # Coloration de la cellule objectif en rouge
    pixels[celluleDepartX][celluleDepartY][0] = 255
    pixels[celluleDepartX][celluleDepartY][1] = 0
    pixels[celluleDepartX][celluleDepartY][2] = 0
    return pixels

def enregistrementLabyrinthe(fichier, pixels):
    """
    Enregistre le labyrinthe sous une image .png
    
    IN: fichier(nom du fichier), pixels

    OUT: N/A
    """
    write_img(fichier, pixels)