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
framerate = 200

#   PONG variables
# Jugadores
player_ancho, player_alto = 15, 100
p1_x, p1_y = 0, 0
p2_x, p2_y = 0, 0
distancia_borde = 50
p1 = pygame.Rect(p1_x, p1_y, player_ancho, player_alto)
p1.center = (distancia_borde , ALTO / 2)

p2 = pygame.Rect(p2_x, p2_y, player_ancho, player_alto)
p2.center = (ANCHO - distancia_borde, ALTO / 2)

p1_score, p2_score = 0, 0
max_score = 3

# Pelota
ball_ancho, ball_alto = 10, 10
ball_x, ball_y = 0, 0
ball = pygame.Rect(ball_x, ball_y, ball_ancho, ball_alto)
ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)

x_speed, y_speed = 1, 1

# def Pong():
pong_screen = pygame.display.set_mode((ANCHO, ALTO))

# reset
p1_score, p2_score = 0, 0
ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - - ball_alto / 2)
x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

# Bucle principal
while jugando:
  
  timer.tick(framerate)

  keys_pressed = pygame.key.get_pressed()

  if keys_pressed[pygame.K_w]:
    if p1.top > 0:
      p1.top -= 2
  if keys_pressed[pygame.K_s]:
    if p1.bottom < ALTO:
      p1.bottom += 2
  if keys_pressed[pygame.K_UP]:
    if p2.top > 0:
      p2.top -= 2
  if keys_pressed[pygame.K_DOWN]:
    if p2.bottom < ALTO:
      p2.bottom += 2
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
  if ball.x == 0 - ball.width / 2:
    pygame.mixer.Sound.play(point)
    p1_score += 1
    ball.center = (ANCHO / 2, ALTO / 2)
    pygame.time.delay(700)
    x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
  if ball.x == ANCHO - ball.width / 2:
    pygame.mixer.Sound.play(point)
    p2_score += 1
    ball.center = (ANCHO / 2, ALTO / 2)
    pygame.time.delay(700)
    x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
  
  # Rebote con jugador
  if p1.x - ball.width <= ball.x <= p1.right and ball.y in range(p1.top - ball.width, p1.bottom + ball.width):
    pygame.mixer.Sound.play(hit)
    x_speed = -1
  if p2.x - ball.width <= ball.x <= p2.right and ball.y in range(p2.top - ball.width, p2.bottom + ball.width):
    pygame.mixer.Sound.play(hit)
    x_speed = 1
  
  p1_score_text = fuente.render(str(p1_score), True, BLANCO)
  p2_score_text = fuente.render(str(p2_score), True, BLANCO)
  
  ball.x += x_speed * 2
  ball.y += y_speed * 2

  pantalla.fill(NEGRO)

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
    p1.center = (ANCHO - distancia_borde, ALTO / 2)
    p2.center = (distancia_borde , ALTO / 2)

  pygame.display.flip()