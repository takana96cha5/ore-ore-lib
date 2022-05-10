class Car:
    def __init__(self, make, model, year, vin, color):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.color = color

    def getCarString(self):
        return self.make + " " + self.model + " " + str(self.year) + " " + self.vin + " " + self.color

teslaS = Car("Tesla", "Model S", 2013, "5YJSA1CN0DFP13393", "Black")
print(teslaS.getCarString())

# tesla S の状態を変更します。黒から白へ色を変更します
teslaS.color = "White"
print(teslaS.getCarString())

porsche88 = Car("Porsche", "928", 1988, "WP0JB0926JS861742", "Red")
print(porsche88.getCarString())

porsche88.color = "Purple"
print(porsche88.getCarString())

# 車の vin number を変更します。(実世界では違法行為です)
print(teslaS.getCarString())
teslaS.vin = "WB10228019ZT94950"

print(teslaS.getCarString())
