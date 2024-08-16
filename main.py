import pygame, sys, os, random, webbrowser

# imports de funciones que inician los juegos
from esquivando_parciales.juego1 import esquivando_parciales

# Inicializar Pygame
pygame.init()

# Configurar la variable de entorno para centrar las ventanas
os.environ['SDL_VIDEO_CENTERED'] = '1'

#   VARIABLES GLOBALES
jugando = True
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
CIAN = (0, 255, 255)
ROSA = (255, 0, 255)
YELLOW = (255, 255, 0)

#   Configuraciones de la ventana del menú principal
ANCHO, ALTO = 720, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
icono = pygame.image.load('img/ESCUDO-UNViMe.png')
pygame.display.set_icon(icono)
pygame.display.set_caption("Expo Carreras - Programación")

# Cargar la imagen del título
logo_UNViMe = pygame.image.load('img/LOGO-UNViMe-BLANCO-PIE.png')
logo_UNViMe_rect = logo_UNViMe.get_rect()

# Cargar y redimensionar las imágenes para los botones
botones_ancho, botones_alto = 110, 110
boton_juego1 = pygame.image.load('img/boton_juego1.png')
boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))

boton_juego2 = pygame.image.load('img/boton_juego2.png')
boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))

boton_juego3 = pygame.image.load('img/boton_juego3.png')
boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))

boton_juego4 = pygame.image.load('img/boton_juego4.png')
boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))

# Función para dibujar el menú
def dibujar_menu():
  global pantalla
  pantalla.fill(NEGRO)

  logo_UNViMe_rect.center = (ANCHO // 2, 75)
  pantalla.blit(logo_UNViMe, logo_UNViMe_rect)

  # Dibujar botones con imágenes
  boton1_rect = pantalla.blit(boton_juego1, (ANCHO // 2 - boton_juego1.get_width() * 1.25, 165))
  boton2_rect = pantalla.blit(boton_juego2, (ANCHO // 2 + boton_juego2.get_width() * 0.25, 165))
  boton3_rect = pantalla.blit(boton_juego3, (ANCHO // 2 - boton_juego3.get_width() * 1.25, 315))
  boton4_rect = pantalla.blit(boton_juego4, (ANCHO // 2 + boton_juego4.get_width() * 0.25, 315))

  pygame.display.flip()

  return boton1_rect, boton2_rect, boton3_rect, boton4_rect

# Bucle principal
while True:
  
  boton1_rect, boton2_rect, boton3_rect, boton4_rect = dibujar_menu()

  pos_mouse = pygame.mouse.get_pos()

  if boton1_rect.collidepoint(pos_mouse) or boton2_rect.collidepoint(pos_mouse) or boton3_rect.collidepoint(pos_mouse) or boton4_rect.collidepoint(pos_mouse) or logo_UNViMe_rect.collidepoint(pos_mouse):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar a cursor "manito"
  else:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal

  if boton1_rect.collidepoint(pos_mouse):
    boton_juego1 = pygame.image.load('img/boton_juego1_hover.png')
    boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))
  else:
    boton_juego1 = pygame.image.load('img/boton_juego1.png')
    boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))

  if boton2_rect.collidepoint(pos_mouse):
    boton_juego2 = pygame.image.load('img/boton_juego2_hover.png')
    boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))
  else:
    boton_juego2 = pygame.image.load('img/boton_juego2.png')
    boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))

  if boton3_rect.collidepoint(pos_mouse):
    boton_juego3 = pygame.image.load('img/boton_juego3_hover.png')
    boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))
  else:
    boton_juego3 = pygame.image.load('img/boton_juego3.png')
    boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))

  if boton4_rect.collidepoint(pos_mouse):
    boton_juego4 = pygame.image.load('img/boton_juego4_hover.png')
    boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))
  else:
    boton_juego4 = pygame.image.load('img/boton_juego4.png')
    boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if boton1_rect.collidepoint(event.pos):
        jugando = True
        # juegoBRAIAM()
      elif boton2_rect.collidepoint(event.pos):
        jugando = True
        # juegoEZEyMARTI()
      elif boton3_rect.collidepoint(event.pos):
        print("iniciando juego")
        jugando = True
        esquivando_parciales(jugando,ANCHO,ALTO)
      elif boton4_rect.collidepoint(event.pos):
        jugando = True
        # juegoTOBI()
      elif logo_UNViMe_rect.collidepoint(event.pos):
        webbrowser.open('https://www.unvime.edu.ar')
        print("Logo clickeado, abriendo página web...")
  pygame.display.update()
