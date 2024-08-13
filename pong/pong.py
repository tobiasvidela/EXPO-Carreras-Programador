import pygame, sys, random

# Iniciar Pygame
pygame.init()

# VARIABLES GLOBALES
jugando = True

# COLORES
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CIAN = (0, 255, 255)
ROSA = (255, 0, 255)
YELLOW = (255, 255, 0)

# SONIDOS

# FUENTES

# VENTANA
ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pong_icon = pygame.image.load('pong/img/pong_icon.png')
pygame.display.set_icon(pong_icon)
pygame.display.set_caption("PONG!")

# TIMER
timer = pygame.time.Clock()
framerate = 60

# PONG variables
player_ancho, player_alto = 15, 100
p1_ancho, p1_alto = player_ancho, player_alto
p2_ancho, p2_alto = player_ancho, player_alto
p1_x, p1_y = (50 - p1_ancho / 2), (ALTO / 2 - p1_alto / 2)
p2_x, p2_y = (ANCHO - 50 - p2_ancho / 2), (ALTO / 2 - p2_alto / 2)

# funciones
def checkStopPlaying():
  global jugando
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.QUIT:
      jugando = False
      # Reset window size and caption

def drawPlayers():
  global p1_ancho, p1_alto, p2_ancho, p2_alto, p1_x, p1_y, p2_x, p2_y

  p1 = pygame.draw.rect(pantalla, BLANCO, [p1_x, p1_y, p1_ancho, p1_alto])
  p2 = pygame.draw.rect(pantalla, BLANCO, [p2_x, p2_y, p2_ancho, p2_alto])

# Bucle principal
while jugando:
  timer.tick(framerate)

  pantalla.fill(NEGRO)

  drawPlayers()

  checkStopPlaying()
  
  pygame.display.flip()