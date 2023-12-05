#!/usr/bin/python3

# Instalar "sudo apt install python3-pygame"

import pygame
import sys
import random

pygame.init()

size = (700, 700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fuentepuntaje = pygame.font.Font(None, 30)
fuentesnake = pygame.font.Font(None, 80)
fuentepuntuacion = pygame.font.Font(None, 30)
sonidoright = pygame.mixer.Sound("rightsnake.mp3")
sonidoleft = pygame.mixer.Sound("leftsnake.mp3")
sonidoup = pygame.mixer.Sound("upsnake.mp3")
sonidodown = pygame.mixer.Sound("downsnake.mp3")
sonidofood = pygame.mixer.Sound("foodsnake.mp3")
sonidodeath = pygame.mixer.Sound("deathsnake.mp3")


# Definir colores
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (800, 500)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 150, 0)
GreenSlow = (0, 200, 0)
Lime = (0, 230, 0)
Maroon = (128, 0, 0)
NavyBlue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)


def comida():
    comidax = random.randrange(75, 600, 25)
    comiday = random.randrange(125, 575, 25)
    comida_posicion = [comidax, comiday]
    return comida_posicion


def funcion_snake():

    snake_position = [175, 200]
    snake_body = [[375, 325], [400, 50], [425, 50]]
    change = "RIGHT"
    comida_posicion = comida()
    puntaje = 0
    textosnake = "SNAKE"
    textopuntuacion = "Puntuación: "

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # ----- Lógica del juego ----- #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                    sonidodown.play()
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                    sonidoleft.play()
                if event.key == pygame.K_UP:
                    change = "UP"
                    sonidoup.play()
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
                    sonidodown.play()
        if change == "RIGHT":
            snake_position[0] += 25
            # Añade 25 pixeles para ver que se va moviendo
        if change == "LEFT":
            snake_position[0] -= 25
        if change == "UP":
            snake_position[1] -= 25
        if change == "DOWN":
            # El [0] y el [1] es para que acceda a "snake_position"
            snake_position[1] += 25
        snake_body.insert(0, list(snake_position))
        # Añadimos a snake_body todo lo que sumamos y restamos arriba
        if snake_position == comida_posicion:
            sonidofood.play()
            comida_posicion = comida()
            puntaje += 1
            print(puntaje)
        else:
            snake_body.pop()
            # Esto elimina la ultima posicion para que no crezca

            # ----- Lógica del juego ----- #

        screen.fill(GreenSlow)
        # Zona de dibujo
        for x in range(50, 650, 50):
            pygame.draw.rect(screen, Lime, (x, 100, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 150, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 200, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 250, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 300, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 350, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 400, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 450, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 500, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 550, 25, 25))
            pygame.draw.rect(screen, Lime, (x, 600, 25, 25))
        for y in range(75, 650, 50):
            pygame.draw.rect(screen, Lime, (y, 125, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 175, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 225, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 275, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 325, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 375, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 425, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 475, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 525, 25, 25))
            pygame.draw.rect(screen, Lime, (y, 575, 25, 25))
        for position in snake_body:
            pygame.draw.rect(screen, Aqua,
                             pygame.Rect(position[0], position[1], 25, 25))
        pygame.draw.line(screen, Black, [48, 100], [650, 100], 5)
        pygame.draw.line(screen, Black, [50, 100], [50, 625], 5)
        pygame.draw.line(screen, Black, [48, 625], [650, 625], 5)
        pygame.draw.line(screen, Black, [650, 98], [650, 627], 5)
        pygame.draw.rect(screen, Red,
                         pygame.Rect(comida_posicion[0],
                                     comida_posicion[1], 25, 25))
        textopuntaje = fuentepuntaje.render(str(puntaje), 10, Black)
        screen.blit(textopuntaje, (180, 50))
        textosnake1 = fuentesnake.render(textosnake, 10, NavyBlue)
        screen.blit(textosnake1, (400, 30))
        textopuntuacion1 = fuentepuntuacion.render(textopuntuacion, 10, Black)
        screen.blit(textopuntuacion1, (50, 50))
        if puntaje < 5:
            clock.tick(10)
        if puntaje >= 5 and puntaje < 10:
            clock.tick(15)
        if puntaje >= 10:
            clock.tick(20)
        if snake_position[0] <= 25 or snake_position[0] >= 650:
            sys.exit()
        if snake_position[1] <= 75 or snake_position[1] >= 625:
            sys.exit()
        pygame.display.flip()
        # ZONA DE DIBUJO
        # Actualizar la pantalla para que se muestre del color seleccionado


funcion_snake()
pygame.quit()
