# Simulación de Invasión Zombi con Sensores IoT

Esta aplicación simula una invasión zombi en un edificio, donde cada habitación cuenta con un sensor IoT. Los zombis se propagan entre habitaciones y pisos, y el usuario puede interactuar con la simulación a través de un menú en la consola.

## Instalación y Ejecución

1. **Requisitos:**  
   - Python 3 (se recomienda versión 3.6 o superior).

2. **Instalación:**  
   - Clona o descarga el repositorio.
   - Abre la terminal y navega al directorio del proyecto.

3. **Ejecución:**  
   Ejecuta el siguiente comando en la terminal:
   ```bash
   python main.py

# Arquitectura y Clases

El proyecto se organiza en varios archivos, cada uno con responsabilidades específicas:

## sensor.py
- Define la clase `Sensor`, que gestiona el estado del sensor (normal o alert).

## room.py
- Define la clase `Room`, que representa una habitación. Cada habitación tiene:
  - Un sensor.
  - Un indicador de presencia de zombis (`has_zombie`).
  - Un estado de bloqueo (`is_blocked`) para evitar infecciones.

## floor.py
- Define la clase `Floor`, que administra un conjunto de habitaciones.

## building.py
- Define la clase `Building`, que contiene varios pisos y facilita el acceso a las habitaciones.

## simulation.py
- Define la clase `Simulation`, la cual orquesta la propagación de los zombis en cada turno. Permite:
  - Avanzar un turno o múltiples turnos.
  - Configurar el modo de propagación (expansión o traslado).

## persistence.py
- Contiene funciones para guardar y cargar el estado de la simulación en un archivo JSON.

## utils.py
- Proporciona funciones utilitarias, como:
  - `clear_console()`: Limpia la consola.
  - `draw_building()`: Dibuja el edificio en forma de cuadrícula ASCII.

## main.py
- Es el punto de entrada de la aplicación. Gestiona la interacción con el usuario mediante un menú interactivo en la consola, que se actualiza en cada turno mostrando el estado actual del edificio.

# Comandos e Instrucciones de Uso

Al ejecutar la aplicación, se presentará un menú interactivo en la consola con las siguientes opciones:

- **Configurar edificio:**
  - Define el número de pisos y habitaciones por piso.
  - Selecciona el modo de propagación:
    - **Expansión:** Los zombis permanecen en la habitación original.
    - **Traslado:** Los zombis se mueven, limpiando la habitación original.

- **Mostrar estado del edificio (texto):**
  - Muestra el estado actual del edificio de forma detallada (para fines de depuración).

- **Avanzar un turno (mover zombis):**
  - Realiza una iteración de la simulación, propagando los zombis a las habitaciones adyacentes.

- **Avanzar múltiples turnos:**
  - Permite simular varios turnos consecutivos.

- **Bloquear/Desbloquear habitación:**
  - Permite marcar o desmarcar una habitación como bloqueada para evitar que se infecte.

- **Mostrar estadísticas del edificio:**
  - Muestra el turno actual y el conteo de habitaciones totales, infectadas y bloqueadas.

- **Guardar estado:**
  - Guarda el estado actual de la simulación en un archivo JSON.

- **Cargar estado:**
  - Carga un estado previamente guardado.

- **Cambiar modo de propagación:**
  - Alterna entre el modo de propagación "expansión" y "traslado".

- **Salir:**
  - Finaliza la aplicación.

Cada vez que se avanza un turno, el edificio se redibuja en la parte superior de la consola utilizando una cuadrícula ASCII, y luego se muestra el menú de opciones para facilitar la interacción.

**¡Disfruta de la simulación y buena suerte en el apocalipsis zombi!**
