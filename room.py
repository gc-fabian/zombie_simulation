from sensor import Sensor

class Room:
    def __init__(self, floor_number, room_number):
        self.floor_number = floor_number
        self.room_number = room_number
        self.has_zombie = False
        self.sensor = Sensor()
        self.is_blocked = False  # Habitacion bloqueada
    
    def infect(self):
        # Si está bloqueada, no se infecta
        if self.is_blocked:
            return
        if not self.has_zombie:
            self.has_zombie = True
            self.sensor.alert()
    
    def clear(self):
        # Quita el zombi y resetea el sensor
        self.has_zombie = False
        self.sensor.reset()
    
    def block(self):
        self.is_blocked = True
    
    def unblock(self):
        self.is_blocked = False
    
    def get_draw_char(self):
        """
        Retorna:
          'B' si está bloqueada,
          'Z' si tiene zombi,
          'O' si está limpia.
        """
        if self.is_blocked:
            return 'B'
        elif self.has_zombie:
            return 'Z'
        else:
            return 'O'
    
    def __str__(self):
        if self.is_blocked:
            marker = "B"
        elif self.has_zombie:
            marker = "Z"
        else:
            marker = "O"
        return f"{marker}({self.sensor})"
