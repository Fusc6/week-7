class SpeedException(Exception):
    pass
class NoDriverException(Exception):
    def __init__(self):
        super().__init__("Cannot drive without a Driver")
class Car:
    def __init__(self, topSpeed: float):
        self.__topSpeed = None
        self.__speed = 0
        self.__driver = None
        self.setTopSpeed(topSpeed) #call the setter to initialize __topspeed
    
    def setTopSpeed(self, topSpeed):
        if topSpeed > 0:
            self.__topSpeed = topSpeed
        else:
            raise SpeedException(f"invalid top speed{topSpeed}")
    
    def getTopSpeed(self):
        return self.__topSpeed
    
    def getSpeed(self):
        return self.__speed
    
    def setDriver(self, driver):
        self.__driver = driver
    
    def accelerate(self):
        if self.__driver is None:
            raise NoDriverException

        self.__speed += 10
        if self.__speed > self.__topSpeed:
            self.__speed = self.__topSpeed
            raise SpeedException(f"Cannot accelerate above top speed:{self.__topSPeed}")
    
    def decelerate(self):

        if self.__driver is None:
            raise NoDriverException

        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0
            raise SpeedException(f"Cannot decelerate below zero")
    
    def __str__(self):
        return f"Car going {self.__speed}/{self.__topSpeed} kmph"
    
try:
    car1 = Car(250)
    car1.setDriver("Valentino")
    print(car1)

    try:
        car2 = Car(-99)
        print(car2)
    except Exception as e:
        print(e)

    try:
        for _ in range(30):
            car1.accelerate()
            print(car1)
    except Exception as e:
        print("e")

    try:
        for _ in range(30):
            try:
                car1.decelerate()
                print(car1)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

    user_input = input("Enter a new top speed(float): ")
    try:
        newTopSpeed = float(user_input)
        car1.setTopSpeed(newTopSpeed)
        print(f"New top speed set to: {car1.getTopSpeed()}")
    except ValueError as e:
        print(f"ValueError: {e}")

except Exception as e:
    print("Unexpected error:", e)




    







    



    
