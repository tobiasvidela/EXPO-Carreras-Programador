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
#CIAN = (0, 255, 255)
#ROSA = (255, 0, 255)
#YELLOW = (255, 255, 0)

# SONIDOS
hit = pygame.mixer.Sound('./sound/hit.mp3')
pygame.mixer.Sound.set_volume(hit, 0.7)

point = pygame.mixer.Sound('./sound/point.mp3')
pygame.mixer.Sound.set_volume(point, 0.8)

win = pygame.mixer.Sound('./sound/win.mp3')
pygame.mixer.Sound.set_volume(win, 0.6)

# VENTANA
ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pong_icon = pygame.image.load('./img/pong_icon.png')
pygame.display.set_icon(pong_icon)
pygame.display.set_caption("PONG!")

# FUENTES
fuente = pygame.font.SysFont('Consolas', int(ANCHO/20))

# TIMER
timer = pygame.time.Clock()
framerate = 300

#   MENU DEL JUEGO
# Botones del menu de Pong
botones_ancho, botones_alto = 300, 300
button_1P = pygame.image.load('./img/button_1P.svg')
button_1P = pygame.transform.scale(button_1P, (botones_ancho + 100, botones_alto + 100))

button_2P = pygame.image.load('./img/button_2P.png')
button_2P = pygame.transform.scale(button_2P, (botones_ancho, botones_alto))

button_salir = pygame.image.load('./img/button_salir.png')
button_salir = pygame.transform.scale(button_salir, (50, 50))

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
ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - ball_alto / 2)

x_speed, y_speed = 1, 1

def arrancar_musica():
  pygame.mixer.music.play(loops=-1, fade_ms=150)

def cargar_musica():
  pygame.mixer.music.unload()
  pygame.mixer.music.load('./music/bg-music-3.mp3')
  pygame.mixer.music.set_volume(0.5)

def set_ventana_pong(modo: str) -> pygame.display:
  caption = "PONG! - " + modo
  pong_screen = pygame.display.set_mode((ANCHO, ALTO))
  pygame.display.set_caption(caption)
  pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal
  return pong_screen

def dibujar_menu():
  pantalla.fill(NEGRO)
  pong_icon = pygame.image.load('./img/pong_icon.png')
  pygame.display.set_icon(pong_icon)
  pygame.display.set_caption("PONG!")
  
  boton1P_rect = pantalla.blit(button_1P, (ANCHO // 2 - button_1P.get_width() * 0.80, ALTO // 2 - button_1P.get_height() * 0.35))
  boton2P_rect = pantalla.blit(button_2P, (ANCHO // 2 + button_2P.get_width() * 0.05, ALTO // 2 - button_2P.get_height() * 0.5))
  boton_salir_rect = pantalla.blit(button_salir, (button_salir.get_width() // 5, button_salir.get_height() // 5))
  
  pygame.display.flip()

  return boton1P_rect, boton2P_rect, boton_salir_rect

def update_cursor(pos_mouse, *args: pygame.image):
  # El cursor está en el estado normal
  cursor_set = False
  for button in args:
    if button.collidepoint(pos_mouse):
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar a cursor "manito"
      cursor_set = True
      break  # Si ya se ha encontrado un botón, no es necesario seguir comprobando los demás
  if not cursor_set:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Volver al cursor normal

def reset():
  global p1_score, p2_score, x_speed, y_speed
  p1.center = (distancia_borde , ALTO / 2)
  p2.center = (ANCHO - distancia_borde, ALTO / 2)
  p1_score, p2_score = 0, 0
  ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - ball_alto / 2)
  x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
  print(f"RESET: {p1_score}, {p2_score}, {x_speed}, {y_speed}")
  return p1_score, p2_score, x_speed, y_speed

def stop_playing(jugando, keys_pressed) -> bool:
  if keys_pressed[pygame.K_ESCAPE]:
    jugando = False
    pygame.display.set_caption("Pong!")
    pygame.mixer.music.pause()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  return jugando

def runAI():
  # P2 AI mejorada
  # La velocidad de P2 se ajusta en función de la distancia entre el centro de P2 y el centro de la pelota (ball.centery).
  # Cuanto más lejos esté la pelota, más rápido se moverá P2 hacia ella.
  # min(1.2, abs(ball.centery - p2.centery) / 30) ajusta la velocidad de movimiento.
  # El valor máximo es 1.2 para evitar que P2 se mueva demasiado rápido
  if p2.centery < ball.centery:
    if p2.bottom < ALTO:
      p2.y += player_speed * min(1.2, abs(ball.centery - p2.centery) / 30) * 0.6
  elif p2.centery > ball.centery:
    if p2.top > 0:
      p2.y -= player_speed * min(1.2, abs(ball.centery - p2.centery) / 30) * 0.6

def mover_jugador(keys_pressed):
  if keys_pressed[pygame.K_w]:
    if p1.top > 0:
      p1.top -= player_speed
  if keys_pressed[pygame.K_s]:
    if p1.bottom < ALTO:
      p1.bottom += player_speed
  runAI()

def mover_jugadores(keys_pressed):
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

def dificultad(p1_score, p2_score) -> int:
  velocidad = 2
  if p1_score + p2_score < 5:
    pygame.mixer.music.set_volume(0.5)
  if p1_score + p2_score >= 5:
    velocidad = 2.45
    pygame.mixer.music.set_volume(0.7)
  if p1_score + p2_score >= 10:
    velocidad = 2.5
    pantalla.fill((100, 0, 0))
    pygame.mixer.music.set_volume(1)
  return velocidad

def colisiones_bordes(y_speed):
  # Rebote con bordes
  if ball.y >= ALTO:
    y_speed = -1
    pygame.mixer.Sound.play(hit)
  if ball.y <= 0:
    y_speed = 1
    pygame.mixer.Sound.play(hit)
  return y_speed
    
def colisiones_jugadores(x_speed):
  # Rebote con jugador
  if p1.colliderect(ball) and x_speed < 0:
    pygame.mixer.Sound.play(hit)
    x_speed = 1
  if p2.colliderect(ball) and x_speed > 0:
    pygame.mixer.Sound.play(hit)
    x_speed = -1
  return x_speed

def manejar_colisiones(x_speed, y_speed):
  return colisiones_jugadores(x_speed) , colisiones_bordes(y_speed)

def Pong1P(jugando):
  arrancar_musica()
  pong_screen = set_ventana_pong("1P")

  p1_score, p2_score, x_speed, y_speed = reset()

  # Bucle principal
  while jugando:
    
    timer.tick(framerate)

    keys_pressed = pygame.key.get_pressed()

    mover_jugador(keys_pressed)
        
    jugando = stop_playing(jugando, keys_pressed)
        
    # Rebote con bordes y jugadores
    x_speed, y_speed = manejar_colisiones(x_speed, y_speed)

    # "Gol"
    gol = False
    if ball.x <= 0 - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p2_score += 1
    if ball.x >= ANCHO - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p1_score += 1
      
    if gol:
      pygame.time.delay(900)
      p1.center = (distancia_borde , ALTO / 2)
      p2.center = (ANCHO - distancia_borde, ALTO / 2)
      ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - ball_alto / 2)
      x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    
    p1_score_text = fuente.render(str(p1_score), True, BLANCO)
    p2_score_text = fuente.render(str(p2_score), True, BLANCO)
    
    ball.x += x_speed * dificultad(p1_score, p2_score)
    ball.y += y_speed * dificultad(p1_score, p2_score)

    pong_screen.fill(NEGRO)

    pygame.draw.rect(pong_screen, BLANCO, p1)
    pygame.draw.rect(pong_screen, BLANCO, p2)
    pygame.draw.circle(pong_screen, BLANCO, ball.center, ball_ancho)

    pong_screen.blit(p1_score_text, (ANCHO // 2 - 100, 30))
    pong_screen.blit(p2_score_text, (ANCHO // 2 + 100, 30))
    
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
  arrancar_musica()
  pong_screen = set_ventana_pong("2P")

  p1_score, p2_score, x_speed, y_speed = reset()

  # Bucle principal
  while jugando:
    
    timer.tick(framerate)

    keys_pressed = pygame.key.get_pressed()

    mover_jugadores(keys_pressed)
    
    jugando = stop_playing(jugando, keys_pressed)
        
    # Rebote con bordes y jugadores
    x_speed, y_speed = manejar_colisiones(x_speed, y_speed)
    
    # "Gol"
    gol = False
    if ball.x <= 0 - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p2_score += 1
    if ball.x >= ANCHO - ball.width / 2:
      pygame.mixer.Sound.play(point)
      gol = True
      p1_score += 1
      
    if gol:
      pygame.time.delay(900)
      p1.center = (distancia_borde , ALTO / 2)
      p2.center = (ANCHO - distancia_borde, ALTO / 2)
      ball.center = (ANCHO / 2 - ball_ancho / 2, ALTO / 2 - ball_alto / 2)
      x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

    p1_score_text = fuente.render(str(p1_score), True, BLANCO)
    p2_score_text = fuente.render(str(p2_score), True, BLANCO)
    
    ball.x += x_speed * dificultad(p1_score, p2_score)
    ball.y += y_speed * dificultad(p1_score, p2_score)

    pong_screen.fill(NEGRO)

    pygame.draw.rect(pong_screen, BLANCO, p1)
    pygame.draw.rect(pong_screen, BLANCO, p2)
    pygame.draw.circle(pong_screen, BLANCO, ball.center, ball_ancho)

    pong_screen.blit(p1_score_text, (ANCHO // 2 - 100, 30))
    pong_screen.blit(p2_score_text, (ANCHO // 2 + 100, 30))
    
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

def runPong(jugando, main_ancho = ANCHO, main_alto = ALTO):
  cargar_musica()

  pantalla = set_ventana_pong("")

  menu = True

  while menu:
    boton1P_rect, boton2P_rect, boton_salir_rect = dibujar_menu()

    pos_mouse = pygame.mouse.get_pos()

    update_cursor(pos_mouse, boton1P_rect, boton2P_rect, boton_salir_rect)

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
          print("Stopping Pong")
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          jugando = True
          Pong1P(jugando)
        elif event.key == pygame.K_2:
          jugando = True
          Pong2P(jugando)
        elif event.key == pygame.K_ESCAPE:
          menu = False
          print("Stopping Pong")

    pygame.display.update()

if __name__ == "__main__":
  runPong(jugando)