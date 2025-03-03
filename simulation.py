from building import Building

class Simulation:
    def __init__(self, building, propagation_mode="expansion", turn=0):
        self.building = building
        self.propagation_mode = propagation_mode  # "expansion" o "transfer"
        self.turn = turn
    
    def advance_turn(self):
        infected_rooms = []
        for floor in self.building.floors:
            for room in floor.rooms:
                if room.has_zombie:
                    infected_rooms.append((room.floor_number, room.room_number))
        
        new_infections = []
        # Propagar a habitaciones adyacentes (misma fila y pisos contiguos)
        for floor_num, room_num in infected_rooms:
            # Adyacentes en el mismo piso (izquierda y derecha)
            for adj in [room_num - 1, room_num + 1]:
                room = self.building.get_room(floor_num, adj)
                if room and not room.has_zombie and not room.is_blocked:
                    room.infect()
                    new_infections.append((floor_num, adj))
            # Habitación en piso superior e inferior
            for f in [floor_num - 1, floor_num + 1]:
                room = self.building.get_room(f, room_num)
                if room and not room.has_zombie and not room.is_blocked:
                    room.infect()
                    new_infections.append((f, room_num))
        
        # En modo "transfer", se limpian las habitaciones originales
        if self.propagation_mode == "transfer":
            for floor_num, room_num in infected_rooms:
                room = self.building.get_room(floor_num, room_num)
                if room and not room.is_blocked:
                    room.clear()
        
        self.turn += 1
        print(f"Turno {self.turn} completado.")
        if new_infections:
            infected_list = ", ".join(f"P{f}-R{r}" for f, r in new_infections)
            print("Nuevas infecciones en: " + infected_list)
        else:
            print("No hubo nuevas infecciones.")
        print()
    
    def advance_multiple_turns(self, n):
        for _ in range(n):
            self.advance_turn()
    
    def show_statistics(self):
        total_rooms = 0
        infected = 0
        blocked = 0
        for floor in self.building.floors:
            for room in floor.rooms:
                total_rooms += 1
                if room.has_zombie:
                    infected += 1
                if room.is_blocked:
                    blocked += 1
        print(f"Turno actual: {self.turn}")
        print(f"Habitaciones totales: {total_rooms}")
        print(f"Habitaciones infectadas: {infected}")
        print(f"Habitaciones bloqueadas: {blocked}\n")
