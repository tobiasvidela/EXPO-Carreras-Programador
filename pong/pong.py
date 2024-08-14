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
hit = pygame.mixer.Sound('pong/sound/hit.mp3')
pygame.mixer.Sound.set_volume(hit, 0.7)

point = pygame.mixer.Sound('pong/sound/point.mp3')
pygame.mixer.Sound.set_volume(point, 0.8)

win = pygame.mixer.Sound('pong/sound/win.mp3')
pygame.mixer.Sound.set_volume(win, 0.6)

# VENTANA
ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pong_icon = pygame.image.load('pong/img/pong_icon.png')
pygame.display.set_icon(pong_icon)
pygame.display.set_caption("PONG!")

# FUENTES
fuente = pygame.font.SysFont('Consolas', int(ANCHO/20))

# TIMER
timer = pygame.time.Clock()
framerate = 300

#   PONG variables
# Jugadores
player_ancho, player_alto = 15, 100
player_speed = 2
p1_x, p1_y = 0, 0
p2_x, p2_y = 0, 0
distancia_borde = 50
p1 = pygame.Rect(p1_x, p1_y, player_ancho, player_alto)
p1.center = (distancia_borde , ALTO / 2)

p2 = pygame.Rect(p2_x, p2_y, player_ancho, player_alto)
p2.center = (ANCHO - distancia_borde, ALTO / 2)

p1_score, p2_score = 0, 0
max_score = 10

# Pelota
ball_ancho, ball_alto = 10, 10
ball_x, ball_y = 0, 0
ball = pygame.Rect(ball_x, ball_y, ball_ancho, ball_alto)
ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)

x_speed, y_speed = 1, 1

def Pong1P(jugando):

  pong_screen = pygame.display.set_mode((ANCHO, ALTO))

  # reset
  p1.center = (distancia_borde , ALTO / 2)
  p2.center = (ANCHO - distancia_borde, ALTO / 2)
  p1_score, p2_score = 0, 0
  ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)
  x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

  # Bucle principal
  while jugando:
    
    timer.tick(framerate)

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
      if p1.top > 0:
        p1.top -= player_speed
    if keys_pressed[pygame.K_s]:
      if p1.bottom < ALTO:
        p1.bottom += player_speed
    if p2.top < ball.y:
      if p2.top > 0:
        p2.top += player_speed * 0.71
    if p2.bottom > ball.y:
      if p2.bottom < ALTO:
        p2.bottom -= player_speed * 0.71
        
    if keys_pressed[pygame.K_ESCAPE]:
      jugando = False
      # Reset window size and caption

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    # Rebote con bordes
    if ball.y >= ALTO:
      y_speed = -1
      pygame.mixer.Sound.play(hit)
    if ball.y <= 0:
      y_speed = 1
      pygame.mixer.Sound.play(hit)
    # "Gol"
    gol = False
    if ball.x <= 0 - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p1_score += 1
    if ball.x >= ANCHO - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p2_score += 1
      
    if gol:
      pygame.time.delay(900)
      ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)
      x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    
    # Rebote con jugador
    if p1.colliderect(ball) and x_speed < 0:
      pygame.mixer.Sound.play(hit)
      x_speed = 1
    if p2.colliderect(ball) and x_speed > 0:
      pygame.mixer.Sound.play(hit)
      x_speed = -1
    
    p1_score_text = fuente.render(str(p1_score), True, BLANCO)
    p2_score_text = fuente.render(str(p2_score), True, BLANCO)
    
    ball.x += x_speed * 2
    ball.y += y_speed * 2

    pong_screen.fill(NEGRO)

    pygame.draw.rect(pong_screen, BLANCO, p1)
    pygame.draw.rect(pong_screen, BLANCO, p2)
    pygame.draw.circle(pong_screen, BLANCO, ball.center, ball_ancho)

    pong_screen.blit(p1_score_text, (ANCHO // 2 + 100, 30))
    pong_screen.blit(p2_score_text, (ANCHO // 2 - 100, 30))
    
    pygame.display.flip()
    
    # GANADOR
    if p1_score == max_score or p2_score == max_score:
      pygame.mixer.Sound.play(win)
      # Loading screen
      pygame.time.delay(1000)
      p1_score, p2_score = 0, 0
      p1.center = (distancia_borde , ALTO / 2)
      p2.center = (ANCHO - distancia_borde, ALTO / 2)

    pygame.display.flip()

def Pong2P(jugando):
  pong_screen = pygame.display.set_mode((ANCHO, ALTO))

  # reset
  p1.center = (distancia_borde , ALTO / 2)
  p2.center = (ANCHO - distancia_borde, ALTO / 2)
  p1_score, p2_score = 0, 0
  ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)
  x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

  # Bucle principal
  while jugando:
    
    timer.tick(framerate)

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
      if p1.top > 0:
        p1.top -= player_speed
    if keys_pressed[pygame.K_s]:
      if p1.bottom < ALTO:
        p1.bottom += player_speed
    if keys_pressed[pygame.K_UP]:
      if p2.top > 0:
        p2.top -= player_speed
    if keys_pressed[pygame.K_DOWN]:
      if p2.bottom < ALTO:
        p2.bottom += player_speed
    if keys_pressed[pygame.K_ESCAPE]:
      jugando = False
      # Reset window size and caption

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    # Rebote con bordes
    if ball.y >= ALTO:
      y_speed = -1
      pygame.mixer.Sound.play(hit)
    if ball.y <= 0:
      y_speed = 1
      pygame.mixer.Sound.play(hit)
    # "Gol"
    gol = False
    if ball.x <= 0 - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p1_score += 1
    if ball.x >= ANCHO - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p2_score += 1
      
    if gol:
      pygame.time.delay(900)
      ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)
      x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    
    # Rebote con jugador
    if p1.colliderect(ball) and x_speed < 0:
      pygame.mixer.Sound.play(hit)
      x_speed = 1
    if p2.colliderect(ball) and x_speed > 0:
      pygame.mixer.Sound.play(hit)
      x_speed = -1
    
    p1_score_text = fuente.render(str(p1_score), True, BLANCO)
    p2_score_text = fuente.render(str(p2_score), True, BLANCO)
    
    ball.x += x_speed * 2
    ball.y += y_speed * 2

    pong_screen.fill(NEGRO)

    pygame.draw.rect(pong_screen, BLANCO, p1)
    pygame.draw.rect(pong_screen, BLANCO, p2)
    pygame.draw.circle(pong_screen, BLANCO, ball.center, ball_ancho)

    pong_screen.blit(p1_score_text, (ANCHO // 2 + 100, 30))
    pong_screen.blit(p2_score_text, (ANCHO // 2 - 100, 30))
    
    pygame.display.flip()
    
    # GANADOR
    if p1_score == max_score or p2_score == max_score:
      pygame.mixer.Sound.play(win)
      # Loading screen
      pygame.time.delay(1000)
      p1_score, p2_score = 0, 0
      p1.center = (distancia_borde , ALTO / 2)
      p2.center = (ANCHO - distancia_borde, ALTO / 2)

    pygame.display.flip()

#   MENU DEL JUEGO
# Botones del menu de Pong
botones_ancho, botones_alto = 300, 300
button_1P = pygame.image.load('pong/img/button_1P.png')
button_1P = pygame.transform.scale(button_1P, (botones_ancho, botones_alto))

button_2P = pygame.image.load('pong/img/button_2P.png')
button_2P = pygame.transform.scale(button_2P, (botones_ancho, botones_alto))

button_salir = pygame.image.load('pong/img/button_salir.png')
button_salir = pygame.transform.scale(button_salir, (50, 50))

def dibujar_menu():
  pantalla.fill(NEGRO)
  
  boton1P_rect = pantalla.blit(button_1P, (ANCHO // 2 - button_1P.get_width() * 1.05, ALTO // 2 - button_1P.get_height() // 2))
  boton2P_rect = pantalla.blit(button_2P, (ANCHO // 2 + button_2P.get_width() * 0.05, ALTO // 2 - button_1P.get_height() // 2))
  boton_salir_rect = pantalla.blit(button_salir, (button_salir.get_width() // 5, button_salir.get_height() // 5))
  
  pygame.display.flip()

  return boton1P_rect, boton2P_rect, boton_salir_rect

def runPong(jugando, menu = True):
  while menu:
    boton1P_rect, boton2P_rect, boton_salir_rect = dibujar_menu()

    pos_mouse = pygame.mouse.get_pos()

    if boton1P_rect.collidepoint(pos_mouse) or boton2P_rect.collidepoint(pos_mouse) or boton_salir_rect.collidepoint(pos_mouse):
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar a cursor "manito"
    else:
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if boton1P_rect.collidepoint(event.pos):
          jugando = True
          Pong1P(jugando)
        elif boton2P_rect.collidepoint(event.pos):
          jugando = True
          Pong2P(jugando)
        elif boton_salir_rect.collidepoint(event.pos):
          menu = False
    
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          jugando = True
          Pong1P(jugando)
        elif event.key == pygame.K_2:
          jugando = True
          Pong2P(jugando)
        elif event.key == pygame.K_ESCAPE:
          menu = False

    pygame.display.update()

#runPong(jugando)