import pygame, sys, os, random

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


# Función para dibujar el menú
def dibujar_menu():
  pantalla.fill(NEGRO)

  # Cargar la imagen del título
  imagen_titulo = pygame.image.load('img/LOGO-UNViMe-BLANCO-PIE.png')
  
  # Obtener el tamaño de la imagen
  imagen_rect = imagen_titulo.get_rect()
  
  # Colocar la imagen centrada en la parte superior
  imagen_rect.center = (ANCHO // 2, 80)
  
  # Dibujar la imagen en la pantalla
  pantalla.blit(imagen_titulo, imagen_rect)

  #titulo = fuente.render("Elige un juego:", True, BLANCO)
  #pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))

  juego1 = fuente.render("1. {0}".format(nombre_j1), True, BLANCO) # Repetir este formato para los demás
  pantalla.blit(juego1, (ANCHO // 2 - juego1.get_width() // 2, 180))

  juego2 = fuente.render("2. {0}".format(nombre_j2), True, BLANCO)
  pantalla.blit(juego2, (ANCHO // 2 - juego2.get_width() // 2, 230))

  juego3 = fuente.render("3. {0}".format(nombre_j3), True, BLANCO)
  pantalla.blit(juego3, (ANCHO // 2 - juego3.get_width() // 2, 280))

  juego4 = fuente.render("4. {0}".format(nombre_j4), True, BLANCO)
  pantalla.blit(juego4, (ANCHO // 2 - juego4.get_width() // 2, 330))

  juego5 = fuente.render("5. {0}".format(nombre_j5), True, BLANCO)
  pantalla.blit(juego5, (ANCHO // 2 - juego5.get_width() // 2, 380))

  pygame.display.flip()

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
  
  dibujar_menu()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        jugando = True
        juego1()
      elif event.key == pygame.K_2:
        jugando = True
        juego2()
      elif event.key == pygame.K_3:
        jugando = True
        juego3()
      elif event.key == pygame.K_4:
        jugando = True
        juego4()
      elif event.key == pygame.K_5:
        jugando = True
        juego5()

  pygame.display.update()
