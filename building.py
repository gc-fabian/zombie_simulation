from floor import Floor

class Building:
    def __init__(self, floors_count, rooms_per_floor):
        self.floors = [Floor(i, rooms_per_floor) for i in range(floors_count)]
    
    def get_room(self, floor_number, room_number):
        if 0 <= floor_number < len(self.floors) and 0 <= room_number < len(self.floors[floor_number].rooms):
            return self.floors[floor_number].rooms[room_number]
        else:
            return None

    def show_state(self):
        print("\nEstado del edificio:")
        for floor in self.floors:
            print(floor)
        print()
