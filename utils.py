import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_building(building):
    """
    Dibuja el edificio en consola.
    Cada piso se dibuja como una fila, empezando por el piso más alto.
    Cada habitación se muestra en una celda:
      'B' para bloqueada,
      'Z' para infectada,
      'O' para limpia.
    """
    floors = building.floors
    if not floors:
        print("Edificio sin pisos.")
        return

    # Dibujar de arriba hacia abajo
    for floor in reversed(floors):
        print("     " + "+-----" * len(floor.rooms) + "+")
        floor_line = f"{floor.floor_number:>3}  |"
        for room in floor.rooms:
            floor_line += f"  {room.get_draw_char()}  |"
        print(floor_line)
    print("     " + "+-----" * len(floors[0].rooms) + "+\n")
