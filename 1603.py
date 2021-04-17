class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
        print(big,medium,small)

    def addCar(self, carType):
        print(self.big)
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
list = [[1, 1, 0], [1], [2], [3], [1]]
obj = ParkingSystem(1, 1, 0)
param_1 = []
param_1.append( obj.addCar(1))
param_1.append( obj.addCar(2))
param_1.append( obj.addCar(3))
param_1.append( obj.addCar(1))
print(param_1)
