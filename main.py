import sys
from utils import clear_console, draw_building
from building import Building
from simulation import Simulation
from persistence import save_state, load_state

def menu():
    simulation = None

    while True:
        clear_console()
        if simulation:
            print(f"Simulación - Turno {simulation.turn} (Modo: {simulation.propagation_mode})")
            draw_building(simulation.building)
        else:
            print("Edificio no configurado.\n")
        
        print("=== Menú de Simulación de Invasión Zombi ===")
        print("1. Configurar edificio")
        print("2. Mostrar estado del edificio (texto)")
        print("3. Avanzar un turno (mover zombis)")
        print("4. Avanzar múltiples turnos")
        print("5. Bloquear/Desbloquear habitación")
        print("6. Mostrar estadísticas del edificio")
        print("7. Guardar estado")
        print("8. Cargar estado")
        print("9. Cambiar modo de propagación")
        print("10. Salir")
        choice = input("Seleccione una opción: ").strip()

        if choice == "1":
            try:
                floors_count = int(input("Ingrese el número de pisos: "))
                rooms_per_floor = int(input("Ingrese el número de habitaciones por piso: "))
                print("Seleccione el modo de propagación:")
                print("1. Expansión (zombis permanecen en la habitación original)")
                print("2. Traslado (zombis se mueven, limpiando la habitación original)")
                mode_choice = input("Opción (1/2, por defecto 1): ").strip()
                propagation_mode = "transfer" if mode_choice == "2" else "expansion"
                building = Building(floors_count, rooms_per_floor)
                simulation = Simulation(building, propagation_mode=propagation_mode)
                # Iniciar invasión en la habitación 0 del piso 0
                building.get_room(0, 0).infect()
                print(f"Edificio configurado exitosamente. Invasión iniciada en Piso 0, Habitación 0. (Modo: {propagation_mode})")
                input("Presione Enter para continuar...")
            except ValueError:
                input("Error: Ingrese valores numéricos válidos. Presione Enter para continuar...")
        
        elif choice == "2":
            if simulation:
                simulation.building.show_state()
                input("Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "3":
            if simulation:
                simulation.advance_turn()
                input("Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "4":
            if simulation:
                try:
                    n_turns = int(input("Ingrese el número de turnos a avanzar: "))
                    simulation.advance_multiple_turns(n_turns)
                    input("Presione Enter para continuar...")
                except ValueError:
                    input("Error: Ingrese un número válido. Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "5":
            if simulation:
                try:
                    print("1. Bloquear habitación")
                    print("2. Desbloquear habitación")
                    sub_choice = input("Seleccione una opción: ").strip()
                    floor_input = int(input("Ingrese el número de piso: "))
                    room_input = int(input("Ingrese el número de habitación: "))
                    room = simulation.building.get_room(floor_input, room_input)
                    if room:
                        if sub_choice == "1":
                            room.block()
                            print(f"Habitación {room_input} del piso {floor_input} bloqueada.")
                        elif sub_choice == "2":
                            room.unblock()
                            print(f"Habitación {room_input} del piso {floor_input} desbloqueada.")
                        else:
                            print("Opción no válida.")
                    else:
                        print("Habitación no encontrada.")
                    input("Presione Enter para continuar...")
                except ValueError:
                    input("Error: Ingrese valores numéricos válidos. Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "6":
            if simulation:
                simulation.show_statistics()
                input("Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "7":
            if simulation:
                save_state(simulation)
                input("Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "8":
            loaded_sim = load_state()
            if loaded_sim:
                simulation = loaded_sim
            input("Presione Enter para continuar...")
        
        elif choice == "9":
            if simulation:
                simulation.propagation_mode = "transfer" if simulation.propagation_mode == "expansion" else "expansion"
                print(f"Modo de propagación cambiado a: {simulation.propagation_mode}")
                input("Presione Enter para continuar...")
            else:
                input("Primero configure el edificio (opción 1). Presione Enter para continuar...")
        
        elif choice == "10":
            print("Saliendo de la simulación. ¡Buena suerte en el apocalipsis zombi!")
            sys.exit(0)
        
        else:
            input("Opción no válida. Presione Enter para continuar...")

if __name__ == '__main__':
    menu()
