from room import Room

class Floor:
    def __init__(self, floor_number, rooms_count):
        self.floor_number = floor_number
        self.rooms = [Room(floor_number, i) for i in range(rooms_count)]
    
    def __str__(self):
        room_states = " ".join(str(room) for room in self.rooms)
        return f"Piso {self.floor_number}: {room_states}"
