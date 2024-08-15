import pygame # importamos el modulo
from esquivando_parciales.personaje import Cubo #importamos el personaje Cubo del archivo personaje
from esquivando_parciales.enemigo import Enemigo #importamos el personaje Enemigo del archivo enemigo
import random # importamos el modulo
import sys

pygame.init() # inicializando modulos de pygame
pygame.mixer.init() # inicializando modulos de pygame mixer

sonido_colision = pygame.mixer.Sound("esquivando_parciales/vine-boom.mp3") # cargar sonido de colision
#sonido_fondo = pygame.mixer.Sound("oacrna.mp3")
pygame.mixer.music.load("esquivando_parciales/oacrna.mp3") # cargar sonido de fondo
pygame.mixer.music.play(-1) # reproducir musica de fondo 

ANCHO = 1300 # ancho de nuestra ventana
ALTO = 700 # alto de nuestra ventana
VENTANA = pygame.display.set_mode([ANCHO, ALTO]) # pygame para lo que tiene que ver a la libreria, display para la pantalla y en set mode el tamaño
FPS = 60 
FUENTE = pygame.font.SysFont("impact", 40) # fuente de la letra que muestra las vidas y los puntos

jugando = True # sera verdadero mientras estemos jugando

reloj = pygame.time.Clock()

vidas = 5 # variable de vidas iniciada en 5
puntos = 0 # variable de puntos iniciada en 0

tiempo_pasado = 0
tiempo_entre_enemigos = 400

cubo = Cubo(ANCHO / 2, 623, 80, 60) # ubicacion de nuestro personaje en la pantalla

enemigos = []
enemigos.append(Enemigo(ANCHO / 2, 100, 50, 60)) # lugar donde aparecen los enemigos en la pantalla

# Carga y escala de la imagen de fondo
fondo = pygame.image.load("esquivando_parciales/IMG-20230605-WA0029.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

def gestionar_teclas(teclas):

    if teclas[pygame.K_a]:
        if cubo.x <= 0:
            cubo.x = 0
        else:
            cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        if cubo.x >= ANCHO-80:
            cubo.x = ANCHO-80
        else:
            cubo.x += cubo.velocidad 
    
# Parámetros iniciales
tiempo_pasado = 0
tiempo_entre_enemigos = 600  # Tiempo inicial entre enemigos
tiempo_minimo_entre_enemigos = 100  # Límite inferior para el tiempo entre enemigos
factor_reduccion = 7  # Cuánto reducir el tiempo entre enemigos cada vez que aparece uno

# Parámetros iniciales
velocidad_enemigos = 5  # Velocidad inicial de los enemigos
incremento_velocidad = 0.3  # Cuánto aumentar la velocidad cada vez
puntos_para_incrementar = 50  # Incrementar la velocidad cada 50 puntos

def esquivando_parciales(jugando):
    global vidas, tiempo_pasado, tiempo_entre_enemigos, tiempo_minimo_entre_enemigos, puntos, puntos_para_incrementar, texto_final,texto_final,texto_vida,velocidad_enemigos,incremento_velocidad

    VENTANA = pygame.display.set_mode([ANCHO, ALTO])
    pygame.mixer.music.unload()
    pygame.mixer.music.load("esquivando_parciales/oacrna.mp3")
    pygame.mixer.music.play(-1)
    
    # reset a Parámetros iniciales
    tiempo_pasado = 0
    tiempo_entre_enemigos = 600  # Tiempo inicial entre enemigos
    tiempo_minimo_entre_enemigos = 100  # Límite inferior para el tiempo entre enemigos
    factor_reduccion = 7  # Cuánto reducir el tiempo entre enemigos cada vez que aparece uno

    vidas = 5 # variable de vidas iniciada en 5
    puntos = 0 # variable de puntos iniciada en 0

    velocidad_enemigos = 5  # Velocidad inicial de los enemigos
    incremento_velocidad = 0.3  # Cuánto aumentar la velocidad cada vez
    puntos_para_incrementar = 50  # Incrementar la velocidad cada 50 puntos

    while jugando and vidas > 0: # mientras este jugando y las vidas sean mayores a 0
        #sonido_fondo.play()
        tiempo_pasado += reloj.tick(FPS)

        if tiempo_pasado > tiempo_entre_enemigos:
            enemigos.append(Enemigo(random.randint(0, ANCHO), -100, 50, 60))
            Enemigo.velocidad = velocidad_enemigos  # Asignar la velocidad actual a los enemigos
            tiempo_pasado = 0

            # Reducir el tiempo entre enemigos hasta un límite mínimo
            if tiempo_entre_enemigos > tiempo_minimo_entre_enemigos:
                tiempo_entre_enemigos -= factor_reduccion

        if puntos >= puntos_para_incrementar:
            velocidad_enemigos += incremento_velocidad
            puntos_para_incrementar += 50  # Actualizar el umbral para el siguiente incremento


        eventos = pygame.event.get() # esto nos va a dar una lista con todos los eventos que ocurren en el programa
        teclas = pygame.key.get_pressed()

        texto_vida = FUENTE.render(f"vida:{vidas}", True , "red")
        texto_puntos = FUENTE.render(f"puntos:{puntos}", True , "white")

        gestionar_teclas(teclas)

        for evento in eventos: # por cada evento dentro de evento vamos a comprobar que tipo de evento es
            if evento.type == pygame.QUIT: # si el evento corresponde a un evento como cerrar programa o apagar la maquina
                pygame.quit()
                sys.exit() # ya no vamos a estar jugando
            if evento.type == pygame.KEYDOWN:
                if teclas[pygame.K_ESCAPE]:
                    jugando = False
                    VENTANA = pygame.display.set_mode([ANCHO, ALTO])


        VENTANA.blit(fondo, (0, 0))  # Dibuja la imagen de fondo

        cubo.dibujar(VENTANA)        

        for enemigo in enemigos:
            enemigo.dibujar(VENTANA)
            enemigo.movimiento()
            
            if pygame.Rect.colliderect(cubo.rect, enemigo.rect): # para implementar las colisiones, recibe los rectangulos de personaje y enemigo
                sonido_colision.play()
                vidas -= 1 # pierdo una vida cada vez que colisiono
                print(f"Te quedan {vidas} vidas")
                enemigos.remove(enemigo) # se elimina el enemigo luego de colisionar

            if enemigo.y + enemigo.alto > ALTO:
                puntos += 5
                enemigos.remove(enemigo)

        VENTANA.blit(texto_vida, (20, 20)) # ubicacion del texto "vidas"
        VENTANA.blit(texto_puntos, (20, 50)) # ubicacion del texto "puntos"

        pygame.display.update() # mientras el programa este corriendo, la pantalla se seguira actualizando
        # Aquí mostramos la puntuación final cuando el juego termina
    VENTANA.fill((0, 0, 0))  # Limpia la pantalla con color negro
    texto_final = FUENTE.render(f"Juego terminado. Puntuación alcanzada: {puntos}", True, "yellow")
    VENTANA.blit(texto_final, (ANCHO // 2 - texto_final.get_width() // 2, ALTO // 2 - texto_final.get_height() // 2))

    pygame.display.update() # mientras el programa este corriendo, la pantalla se seguira actualizando

        # Pausa para que el jugador vea la puntuación final antes de cerrar el juego
    pygame.time.delay(3000)  # 5 segundos de pausa

    jugando = False # cerramos el programa

if __name__ == '__main__':
    esquivando_parciales(jugando)