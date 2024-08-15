import pygame, sys, os, random, webbrowser

# imports de funciones que inician los juegos
from pong.pong import runPong

# Inicializar Pygame
pygame.init()

# Configurar la variable de entorno para centrar las ventanas
os.environ['SDL_VIDEO_CENTERED'] = '1'

#   VARIABLES GLOBALES
jugando = True

# Rutas
bg_music_1 = './music/bg-music-1.mp3'
bg_music_2 = './music/bg-music-2.mp3'
bg_music_3 = './music/bg-music-3.mp3'

selected_path = './sound/selected.mp3'
icon_path = 'img/ICONO_CLUB.png'
caption = "Expo Carreras - Club de Programación UNViMe"
logo_path = 'img/LOGO_CLUB_LONG.png'

boton_juego1_path = './img/boton_juego1.png'
boton_juego2_path = './img/boton_juego2.png'
boton_juego3_path = './img/boton_juego3.png'
boton_juego4_path = './img/boton_juego4.png'
boton_juego1_hover_path = './img/boton_juego1_hover.png'
boton_juego2_hover_path = './img/boton_juego2_hover.png'
boton_juego3_hover_path = './img/boton_juego3_hover.png'
boton_juego4_hover_path = './img/boton_juego4_hover.png'

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
CIAN = (0, 255, 255)
ROSA = (255, 0, 255)
YELLOW = (255, 255, 0)

#   SOUNDS
pygame.mixer.music.unload()
pygame.mixer.music.load(bg_music_2)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1, fade_ms=150)

selected = pygame.mixer.Sound(selected_path)
pygame.mixer.Sound.set_volume(selected, 1)

#   Configuraciones de la ventana del menú principal
ANCHO, ALTO = 720, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
icono = pygame.image.load(icon_path)
pygame.display.set_icon(icono)
pygame.display.set_caption(caption)

# Cargar la imagen del título
logo = pygame.image.load(logo_path)
logo_rect = logo.get_rect()

# Cargar y redimensionar las imágenes para los botones
botones_ancho, botones_alto = 110, 110
boton_juego1 = pygame.image.load(boton_juego1_path)
boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))

boton_juego2 = pygame.image.load(boton_juego2_path)
boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))

boton_juego3 = pygame.image.load(boton_juego3_path)
boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))

boton_juego4 = pygame.image.load(boton_juego4_path)
boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))

# Función para dibujar el menú
def dibujar_menu():
  global pantalla
  pantalla.fill(NEGRO)

  logo_rect.center = (ANCHO // 2, 75)
  pantalla.blit(logo, logo_rect)

  # Dibujar botones con imágenes
  boton1_rect = pantalla.blit(boton_juego1, (ANCHO // 2 - boton_juego1.get_width() * 1.25, 165))
  boton2_rect = pantalla.blit(boton_juego2, (ANCHO // 2 + boton_juego2.get_width() * 0.25, 165))
  boton3_rect = pantalla.blit(boton_juego3, (ANCHO // 2 - boton_juego3.get_width() * 1.25, 315))
  boton4_rect = pantalla.blit(boton_juego4, (ANCHO // 2 + boton_juego4.get_width() * 0.25, 315))

  pygame.display.flip()

  return boton1_rect, boton2_rect, boton3_rect, boton4_rect

def update_cursor(pos_mouse, *args: pygame.image) -> None:
  # El cursor está en el estado normal
  cursor_set = False
  for button in args:
    if button.collidepoint(pos_mouse):
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar a cursor "manito"
      cursor_set = True
      break  # Si ya se ha encontrado un botón, no es necesario seguir comprobando los demás
  if not cursor_set:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal

def update_button(pos_mouse, boton1_rect, boton2_rect, boton3_rect, boton4_rect):
  if boton1_rect.collidepoint(pos_mouse):
    boton_juego1 = pygame.image.load(boton_juego1_hover_path)
    boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))
  else:
    boton_juego1 = pygame.image.load(boton_juego1_path)
    boton_juego1 = pygame.transform.scale(boton_juego1, (botones_ancho, botones_alto))

  if boton2_rect.collidepoint(pos_mouse):
    boton_juego2 = pygame.image.load(boton_juego2_hover_path)
    boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))
  else:
    boton_juego2 = pygame.image.load(boton_juego2_path)
    boton_juego2 = pygame.transform.scale(boton_juego2, (botones_ancho, botones_alto))

  if boton3_rect.collidepoint(pos_mouse):
    boton_juego3 = pygame.image.load(boton_juego3_hover_path)
    boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))
  else:
    boton_juego3 = pygame.image.load(boton_juego3_path)
    boton_juego3 = pygame.transform.scale(boton_juego3, (botones_ancho, botones_alto))

  if boton4_rect.collidepoint(pos_mouse):
    boton_juego4 = pygame.image.load(boton_juego4_hover_path)
    boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))
  else:
    boton_juego4 = pygame.image.load(boton_juego4_path)
    boton_juego4 = pygame.transform.scale(boton_juego4, (botones_ancho, botones_alto))
  
  return boton_juego1, boton_juego2, boton_juego3, boton_juego4

def set_menu(ANCHO, ALTO, icon_path, music_path):
  pantalla = pygame.display.set_mode((ANCHO, ALTO))
  icono = pygame.image.load(icon_path)
  pygame.display.set_icon(icono)
  pygame.display.set_caption(caption)
  pygame.mixer.music.unload()
  pygame.mixer.music.load(music_path)
  pygame.mixer.music.play()

def sonido_boton(selected):
  pygame.mixer.music.pause()
  pygame.time.delay(150)
  pygame.mixer.Sound.play(selected)

def main():
  global boton_juego1, boton_juego2, boton_juego3, boton_juego4
  while True:
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.unpause()
    
    boton1_rect, boton2_rect, boton3_rect, boton4_rect = dibujar_menu()

    pos_mouse = pygame.mouse.get_pos()

    update_cursor(pos_mouse, boton1_rect, boton2_rect, boton3_rect, boton4_rect)

    boton_juego1, boton_juego2, boton_juego3, boton_juego4 = update_button(pos_mouse, boton1_rect, boton2_rect, boton3_rect, boton4_rect)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Click en boton
        sonido_boton(selected)

        if boton1_rect.collidepoint(event.pos):
          jugando = True
          # juegoBRAIAM()
        elif boton2_rect.collidepoint(event.pos):
          jugando = True
          # juegoEZEyMARTI()
        elif boton3_rect.collidepoint(event.pos):
          jugando = True
          # juegoNICO()
        elif boton4_rect.collidepoint(event.pos):
          jugando = True
          print("Running Pong")
          runPong(jugando, ANCHO, ALTO)
          set_menu(ANCHO, ALTO, icon_path, bg_music_2)
        elif logo_rect.collidepoint(event.pos):
          webbrowser.open('https://www.unvime.edu.ar')
          print("Logo clickeado, abriendo página web...")
    pygame.display.update()

if __name__ == '__main__':
  main()