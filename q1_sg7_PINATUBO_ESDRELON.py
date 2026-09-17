# q1_sg7_PINATUBO_ESDRELON

class Glassware: # Parent Class
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware
        print(self.kindofglassware, "created")

class Beaker(Glassware): # Child Class (Inheritance)
    def __init__(self, kindofglassware, capacity):
        self.capacity = capacity
        super().__init__(kindofglassware)
        print("Capacity:", self.capacity)
        
    def __del__(self):
        print(self.kindofglassware, "is lost")

class Tray: # Composition Class
    def __init__(self):
        print("Tray created")
        # Creating 5 Beakers inside Tray
        self.beakers = [Beaker("Beaker", "250ml") for _ in range(5)]
        
    def __del__(self):
        del self.beakers
        print("Tray is gone")

# Testing the implementation
myTray = Tray()
del myTray