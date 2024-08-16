![Logo UNViMe](https://i0.wp.com/www.unvime.edu.ar/wp-content/uploads/2018/04/logo-unvime.png?fit=266%2C132&ssl=1)

# EXPO Carreras (Programación)
## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una serie de juegos en Python, diseñados para demostrar lo que se puede aprender en la carrera de programación. Estos juegos están pensados para ser presentados en la exposición de carreras de nuestra institución y despertar el interés en la programación.
## Juegos Incluidos
  - **MEMORAMA**:El memorama es un juego que desafía la memoria de los jugadores. El objetivo es encontrar pares de cartas iguales. Los jugadores deben voltear dos cartas en cada turno, intentando recordar la ubicación de las cartas para hacer coincidir los pares. El juego continúa hasta que todos los pares han sido encontrados.Es un excelente ejercicio para mejorar la memoria y la concentración, además de ser divertido y fácil de aprender.
  - **SNAKE GAME**: El objetivo del juego es mover una serpiente por la pantalla para recolectar comida, lo que hará que la serpiente crezca en longitud. El jugador controla la dirección de la serpiente usando las flechas del teclado.
  - **ESQUIVANDO PARCIALES**: intenta terminar la carrera sin rendir parciales.
  - **PONG**: El clásico juego bidimensional que simula el tenis de mesa. El jugador controla una paleta en el juego, moviéndola hacia arriba y hacia abajo en el lado izquierdo o derecho de la pantalla, con el objetivo de anotar diez puntos antes que su oponente.

## Colaboradores
Este proyecto está siendo desarrollado por un equipo de 5 programadores:
  - Braiam Herrera (Project Lead)
  - Ezequiel Manquez
  - Martina Moneo
  - Nicolás García
  - Tobías Uriel Videla Guliotti

## Guía para Colaboradores

### Descargar los cambios
1. **Conectar con el repositorio**: Antes hacer un `pull`, primero hay que concectarse al repositorio.
``` bash
git remote add origin "enlace"
```
2. **Hacer el `pull`**: Copiar todos los cambios de la rama `main` a tu repositorio local.
``` bash
git pull origin main
```

### Crear una Rama para Desarrollar un Juego
1. **Actualizar el repositorio local**: Antes de comenzar a trabajar, asegúrate de que tu repositorio local esté actualizado con la última versión en `main`.
``` bash
git checkout main
git pull origin main
```
2. **Crear una nueva rama**: Crea una nueva rama para el desarrollo de tu juego. Utiliza un nombre descriptivo para la rama.
``` bash
git checkout -b nombre_de_la_rama
```
3. **Desarrollar el juego**: Realiza los cambios y desarrollos necesarios en la nueva rama.

### Hacer Commit y Push de tus Cambios
1. **Hacer commit de los cambios**: Una vez que hayas realizado tus cambios, haz un commit describiendo lo que has hecho.
``` bash
git add .
git commit -m "Descripción de los cambios"
```
2. **Subir los cambios a GitHub**: Sube los cambios de tu rama al repositorio remoto.
``` bash
git push origin nombre_de_la_rama
```

### Hacer un Merge de la Rama
1. **Volver a `main`**: Cambia a la rama `main` antes de hacer el merge.
``` bash
git checkout main
```
2. **Actualizar `main`**: Asegúrate de que la rama `main` esté actualizada.
``` bash
git pull origin main
```
3. **Revisar los cambios antes de hacer `merge`**: Antes de hacer `git merge nombre_de_la_rama`, asegurarse de revisar los cambios con `git diff` para asegurar que se está fusionando solo lo que realmente se desea.
``` bash
git checkout nombre_de_la_rama
git diff main
```
4. **Hacer merge**: Haz un merge de la rama en `main`. Asegúrate de resolver cualquier conflicto que pueda surgir.
``` bash
git checkout main
git merge nombre_de_la_rama
```
5. **Push de `main` actualizado**: Finalmente, sube los cambios fusionados a GitHub.
``` bash
git push origin main
```
### Mantener el Repositorio Actualizado
Cada vez que trabajes en el proyecto, asegúrate de:
1. Actualizar tu rama `main`.
``` bash
git checkout main
git pull origin main
```
2. *Consultar con los demás colaboradores*.
## Contribuir

Si deseas contribuir al proyecto, por favor sigue la guía de colaboradores descrita anteriormente. Asegúrate de que tu código esté bien documentado y de seguir las buenas prácticas de programación.

---
