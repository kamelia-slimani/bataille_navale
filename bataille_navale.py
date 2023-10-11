# -*- coding: utf-8 -*-
import random
import pygame
import sys

# Initialiser Pygame
pygame.init()

TAILLE_GRILLE = 8  # Augmenter la taille de la grille
CASE_SIZE = 60    # Reduire la taille des cases

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

def tirer_case(x, y):
    if grille[x][y] == 'X':
        print("Touché !")
        grille[x][y] = '*'
        return True
    else:
        print("Manqué !")
        grille[x][y] = 'M'
        return False

def creer_interface():
    # Créer la fenêtre
    fenetre = pygame.display.set_mode((TAILLE_GRILLE*CASE_SIZE, TAILLE_GRILLE*CASE_SIZE))
    pygame.display.set_caption("Bataille Navale")

    # Charger l'image de fond
    fond = pygame.image.load('fond.jpeg')
    fond = pygame.transform.scale(fond, (TAILLE_GRILLE*CASE_SIZE, TAILLE_GRILLE*CASE_SIZE))
    fenetre.blit(fond, (0, 0))

    # Charger l'image du bateau
    bateau = pygame.image.load('bateau.png')
    bateau = pygame.transform.scale(bateau, (CASE_SIZE, CASE_SIZE))

    # Dessiner les navires
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if grille[i][j] == 'X':
                fenetre.blit(bateau, (j*CASE_SIZE, i*CASE_SIZE))

    pygame.display.flip()

    # Boucle de jeu
    while any('X' in ligne for ligne in grille):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x //= CASE_SIZE
                y //= CASE_SIZE

                if x < 0 or x >= TAILLE_GRILLE or y < 0 or y >= TAILLE_GRILLE:
                    print("Coordonnées invalides, réessayez.")
                    continue

                if tirer_case(y, x):
                    break

creer_interface()
