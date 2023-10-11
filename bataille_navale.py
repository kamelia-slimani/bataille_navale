# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import messagebox

TAILLE_GRILLE = 5
grille = [['O' for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

for _ in range(3):
    while True:
        x = random.randint(0, TAILLE_GRILLE - 1)
        y = random.randint(0, TAILLE_GRILLE - 1)
        if grille[x][y] == 'O':
            grille[x][y] = 'X'
            break

def afficher_grille(grille):
    for ligne in grille:
        print(' '.join(ligne))

def tirer(x, y):
    if grille[x][y] == 'X':
        print("Touché !")
        grille[x][y] = '*'
        return True
    else:
        print("Manqué !")
        grille[x][y] = 'M'
        return False

def tirer_case():
    x = int(entree_x.get())
    y = int(entree_y.get

