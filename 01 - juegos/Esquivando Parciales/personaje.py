import pygame

class Cubo: 
    def __init__(self, x, y, ancho, alto): 
        self.x = x 
        self.y = y 
        self.velocidad = 10 
        # Cargar la imagen del cubo
        self.imagen = pygame.image.load("estudioso-removebg-preview.png").convert_alpha()
        # Escalar la imagen al tamaño deseado
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.ancho = ancho
        self.alto = alto
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, VENTANA): 
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo
        VENTANA.blit(self.imagen, self.rect)  # Dibuja la imagen en la ventana
