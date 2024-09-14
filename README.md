
# Proyecto de Herramientas Computacionales

Este repositorio contiene una serie de scripts desarrollados en Python para crear diferentes juegos y aplicaciones gráficas utilizando el módulo `turtle`. Además, se incluyen funcionalidades adicionales como la modificación de figuras y la interacción del usuario con los objetos.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Overview General](#overview-general)
- [Cambios Relevantes](#cambios-relevantes)

## Instalación

Para correr estos proyectos, necesitas instalar las dependencias especificadas. Puedes hacerlo siguiendo los pasos a continuación:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/repo_herramientas_computacionales.git
   cd repo_herramientas_computacionales
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` debe contener las siguientes dependencias:

   ```plaintext
   freegames==2.5.3
   paho-mqtt==1.6.1
   pip==22.0.4
   setuptools==58.1.0
   ```

## Cómo Ejecutar

Cada archivo es independiente, por lo que puedes ejecutarlos con el siguiente comando en la terminal:

```bash
python nombre_del_archivo.py
```

Por ejemplo, para ejecutar el archivo `Paint.py`, debes correr:

```bash
python Paint.py
```

## Overview General

Este proyecto contiene scripts que implementan funcionalidades gráficas y de juego, utilizando la biblioteca `turtle` y otros módulos auxiliares como `freegames` para facilitar la creación de gráficos y elementos interactivos.

### Funcionalidades Incluidas:
- **Dibujo de figuras geométricas** con el uso de `turtle`.
- **Modificación de colores y formas** para proyectiles y balones.
- **Interacción mediante el teclado y el mouse** para controlar elementos gráficos en los juegos.
- **Animación de fantasmas y otros objetos** dentro del entorno gráfico.

## Cambios Relevantes

### `Cambio de la figura de los proyectiles Y balones`

En este commit, se cambió la figura de los proyectiles y balones dentro de los juegos. Los objetos ahora son más dinámicos y se mueven de manera más fluida.

#### Snippet relevante:
```python
for target in targets:
    goto(target.x, target.y)
    shape("triangle")
    stamp()
```

### `Cambio de color de proyectiles y balones`

En este commit, se añadió la funcionalidad de cambiar los colores de los proyectiles y balones aleatoriamente cada vez que son lanzados o aparecen en pantalla.

#### Snippet relevante:
```python
current_color = choice(["red", "blue", "green"])
square(ball.x, ball.y, 9, current_color)
```

### `Dibujar triángulo`

Se añadió la capacidad de dibujar triángulos además de otras formas como círculos y cuadrados. El triángulo es dibujado usando las funciones de `turtle`.

#### Snippet relevante:
```python
def triangle(start, end):
    # Dibuja un triángulo equilátero.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
```

## Contribuciones

Este proyecto ha sido desarrollado con base en varios ejercicios y modificaciones sugeridas para mejorar la interacción y la funcionalidad visual de los juegos. Los commits documentan cada uno de estos cambios de manera incremental.

---

Cualquier sugerencia o colaboración adicional es bienvenida para seguir mejorando este conjunto de herramientas computacionales.
