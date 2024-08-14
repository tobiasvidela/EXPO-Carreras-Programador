import pygame

class Enemigo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.velocidad = 4
        # Cargar la imagen del enemigo
        self.imagen = pygame.image.load("Emoji_u1f4dd-removebg-preview.png").convert_alpha()
        # Escalar la imagen al tamaño deseado
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.ancho = ancho
        self.alto = alto
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo
        ventana.blit(self.imagen, self.rect)  # Dibuja la imagen en la ventana

    def movimiento(self):
        self.y += self.velocidad
