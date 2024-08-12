import pygame, sys, os, random, webbrowser

# Inicializar Pygame
pygame.init()

# Configurar la variable de entorno para centrar las ventanas
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Globales (para todos, las globales específicas de sus juegos colóquenlas en la sección de la lógica correspondiente)
jugando = True

# Configuraciones de la ventana
ANCHO, ALTO = 720, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
icono = pygame.image.load('img/ESCUDO-UNViMe.png')
pygame.display.set_icon(icono)
pygame.display.set_caption("Expo Carreras - Programación")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS1 = (120, 120, 120)
GRIS2 = (170, 170, 170)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Fuentes
fuente = pygame.font.Font(None, 40)
#fuente_j1 = pygame.font.Font('freesansbold.ttf', 20)
#fuente_j2 = pygame.font.Font('freesansbold.ttf', 20)
#fuente_j3 = pygame.font.Font('freesansbold.ttf', 20)
#fuente_j4 = pygame.font.Font('freesansbold.ttf', 20)
#fuente_j5 = pygame.font.Font('freesansbold.ttf', 20)


""" Debajo pueden colocar las variables, clases, funciones, y todo lo que necesiten
específicamente para sus juegos, si hay código que peude ser reutilizado colóquenlo arriba.
Ordenen su código como les quede más cómodo.
"""

# Lógica del juego 1

# ejemplo de definición del nombre del juego 1
nombre_j1 = "Juego 1"

# Lógica del juego 2
nombre_j2 = "Juego 2"

# Lógica del juego 3
nombre_j3 = "Juego 3"

# Lógica del juego 4
nombre_j4 = "Juego 4"

# Lógica del juego 5
nombre_j5 = "Juego 5"

# Cargar la imagen del título
logo_UNViMe = pygame.image.load('img/LOGO-UNViMe-BLANCO-PIE.png')
logo_UNViMe_rect = logo_UNViMe.get_rect()

# Cargar y redimensionar las imágenes para los botones
botones_ancho, botones_alto = 120, 120
boton_juego1 = pygame.image.load('img/boton_juego1.png')
boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))

boton_juego2 = pygame.image.load('img/boton_juego2.png')
boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))

boton_juego3 = pygame.image.load('img/boton_juego3.png')
boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))

boton_juego4 = pygame.image.load('img/boton_juego4.png')
boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))

boton_juego5 = pygame.image.load('img/boton_juego5.png')
boton_juego5 = pygame.transform.scale(boton_juego5, (botones_ancho, botones_alto))


# Función para dibujar el menú
def dibujar_menu():
  pantalla.fill(NEGRO)

  logo_UNViMe_rect.center = (ANCHO // 2, 75)
  pantalla.blit(logo_UNViMe, logo_UNViMe_rect)

  # Dibujar botones con imágenes
  boton1_rect = pantalla.blit(boton_juego1, (ANCHO // 5 - boton_juego1.get_width() // 2, 175))
  boton2_rect = pantalla.blit(boton_juego2, (ANCHO // 2 - boton_juego2.get_width() // 2, 175))
  boton3_rect = pantalla.blit(boton_juego3, (ANCHO - (ANCHO // 5) - boton_juego1.get_width() // 2, 175))
  boton4_rect = pantalla.blit(boton_juego4, (ANCHO // 3 - boton_juego4.get_width() // 2, 325))
  boton5_rect = pantalla.blit(boton_juego5, (ANCHO - (ANCHO // 3) - boton_juego5.get_width() // 2, 325))

  pygame.display.flip()

  return boton1_rect, boton2_rect, boton3_rect, boton4_rect, boton5_rect

# Funciones para manejar la lógica de arrancar los juegos
def juego1():
  print("Iniciando Juego 1...")
  # Aquí iría el código para iniciar el juego 1
  # Ej.: iniciarJuego1()

def juego2():
  print("Iniciando Juego 2...")
  # Aquí iría el código para iniciar el juego 2

def juego3():
  print("Iniciando Juego 3...")
  # Aquí iría el código para iniciar el juego 3

def juego4():
  print("Iniciando Juego 4...")
  # Aquí iría el código para iniciar el juego 4

def juego5():
  print("Iniciando Juego 5...")
  # Aquí iría el código para iniciar el juego 5

# Bucle principal
while True:
  
  boton1_rect, boton2_rect, boton3_rect, boton4_rect, boton5_rect = dibujar_menu()

  pos_mouse = pygame.mouse.get_pos()

  if boton1_rect.collidepoint(pos_mouse) or boton2_rect.collidepoint(pos_mouse) or boton3_rect.collidepoint(pos_mouse) or boton4_rect.collidepoint(pos_mouse) or boton5_rect.collidepoint(pos_mouse) or logo_UNViMe_rect.collidepoint(pos_mouse):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar a cursor "manito"
  else:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if boton1_rect.collidepoint(event.pos):
        jugando = True
        juego1()
      elif boton2_rect.collidepoint(event.pos):
        jugando = True
        juego2()
      elif boton3_rect.collidepoint(event.pos):
        jugando = True
        juego3()
      elif boton4_rect.collidepoint(event.pos):
        jugando = True
        juego4()
      elif boton5_rect.collidepoint(event.pos):
        jugando = True
        juego5()
      elif logo_UNViMe_rect.collidepoint(event.pos):
        webbrowser.open('https://www.unvime.edu.ar')
        print("Logo clickeado, abriendo página web...")
  pygame.display.update()
