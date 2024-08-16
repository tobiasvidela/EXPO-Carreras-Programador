import tkinter
import random
import time
import pygame

# Inicializa pygame
pygame.init()
pygame.mixer.init()

# Carga archivos de sonido
sonido_clic = pygame.mixer.Sound('./memorama/imagenes_memorama/voltear.wav')  
sonido_pareja = pygame.mixer.Sound('./memorama/imagenes_memorama/ganador.wav')  
sonido_no_pareja = pygame.mixer.Sound('./memorama/imagenes_memorama/equivocado.wav') 
sonido_ganador = pygame.mixer.Sound('./memorama/imagenes_memorama/win.mp3')
pygame.mixer.Sound.set_volume(sonido_ganador, 0.6)

def shuffle(arr):
    last_index = len(arr) - 1
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1
    return arr

def reiniciar_juego():
    global intentos, contador_gana, emparejados, barajeado, botones, boton_reinicio, mensaje_felicitacion

    # Ocultar el botón de reinicio
    boton_reinicio.grid_forget()

    # Destruir botones existentes
    for boton in botones:
        boton.destroy()

    # Eliminar mensaje de felicitación si existe
    if mensaje_felicitacion is not None:
        mensaje_felicitacion.destroy()
        mensaje_felicitacion = None

    # Reiniciar las variables del juego
    intentos = 0
    contador_gana = 0
    emparejados = []

    # Rebarajear imágenes
    barajeado = shuffle(imagenes)

    # Crear y mostrar los botones nuevamente
    botones = []
    for i in range(12):
        boton = tkinter.Button(ventana, image=imapreg, width="180", height="180", command=lambda numelec=i: eleccion(numelec))
        botones.append(boton)

    c = 0
    for x in range(3):
        for y in range(4):
            botones[c].grid(row=x, column=y, padx=25, pady=25)
            c += 1

    # Actualizar etiqueta de intentos
    etiqueta_intentos.config(text="Intentos : " + str(intentos))

def eleccion(n):
    global contador_gana, posiciones, emparejados, intentos, ventana, mensaje_felicitacion, etiqueta_intentos

    # Reproduce sonido de clic
    sonido_clic.play()

    if n in emparejados:
        return  # El botón ya está emparejado, no hacer nada

    if posiciones[0] is None:
        botones[n].config(image=barajeado[n])
        posiciones[0] = n
    elif posiciones[0] is not None:
        if posiciones[0] == n:
            return  # El botón seleccionado es el mismo que el anterior, no hacer nada
        else:
            posiciones[1] = n
            botones[n].config(image=barajeado[n])
            ventana.update()
            if barajeado[posiciones[0]] == barajeado[posiciones[1]]:
                contador_gana += 1
                emparejados.append(posiciones[0])
                emparejados.append(posiciones[1])
                posiciones = [None, None]
                intentos += 1
                etiqueta_intentos.config(text="Intentos : " + str(intentos))
                # Reproduce sonido de pareja encontrada
                sonido_pareja.play()
            else:
                time.sleep(0.25)
                botones[posiciones[0]].config(image=imapreg)
                botones[posiciones[1]].config(image=imapreg)
                posiciones = [None, None]
                intentos += 1
                etiqueta_intentos.config(text="Intentos : " + str(intentos))
                # Reproduce sonido de no pareja
                sonido_no_pareja.play()

    if contador_gana == 6:
        # Sonido si gana el juego
        sonido_ganador.play()
        time.sleep(1)
        for boton in botones:
            boton.destroy()
        mensaje_felicitacion = tkinter.Label(ventana, text="¡¡Bien hecho!!", font=("Impact", 50), fg="gold", bg="white")
        mensaje_felicitacion.place(x=350, y=300)
        # Mostrar botón de reinicio
        boton_reinicio.grid(row=4, column=0, columnspan=4, pady=20)

# Configuración de la ventana
ventana = tkinter.Tk()
ventana.geometry("1200x950")
ventana.configure(bg="dark blue")
ventana.title("MEMORAMA")

# Cargar imágenes
imagen0 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/rana.png")
imagen1 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/elefante.png")
imagen2 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/delfin.png")
imagen3 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/aguila.png")
imagen4 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/tortuga.png")
imagen5 = tkinter.PhotoImage(file="./memorama/imagenes_memorama/tigre.png")
imapreg = tkinter.PhotoImage(file="./memorama/imagenes_memorama/logo unvime.png")

imagenes = [imagen0, imagen1, imagen2, imagen3, imagen4, imagen5, imagen0, imagen1, imagen2, imagen3, imagen4, imagen5]

def memorama(jugando):
    global imagenes, contador_gana, posiciones, emparejados, intentos, etiqueta_intentos, ventana, mensaje_felicitacion, intentos, barajeado, botones, boton_reinicio

    while jugando:
        # Inicializar juego
        barajeado = shuffle(imagenes)
        intentos = 0
        contador_gana = 0
        posiciones = [None, None]
        emparejados = []
        mensaje_felicitacion = None

        # Crear botones
        botones = []
        for i in range(12):
            boton = tkinter.Button(ventana, image=imapreg, width="180", height="180", command=lambda numelec=i: eleccion(numelec))
            botones.append(boton)

        c = 0
        for x in range(3):
            for y in range(4):
                botones[c].grid(row=x, column=y, padx=25, pady=25)
                c += 1


        # Etiqueta de intentos
        etiqueta_intentos = tkinter.Label(ventana, text="Intentos : " + str(intentos), font=("Impact", 30), bg="RoyalBlue4", fg="white")
        etiqueta_intentos.place(x=965, y=350)

        # Botón de reinicio
        boton_reinicio = tkinter.Button(ventana, text="Reiniciar Juego", font=("Impact", 30), command=reiniciar_juego)

        ventana.mainloop()

        # Cerrar
        jugando = False

if __name__ == '__main__':
    memorama(True)
