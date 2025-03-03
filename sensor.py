class Sensor:
    def __init__(self):
        self.status = "normal"
    
    def alert(self):
        self.status = "alert"
    
    def reset(self):
        self.status = "normal"
    
    def __str__(self):
        return self.status
