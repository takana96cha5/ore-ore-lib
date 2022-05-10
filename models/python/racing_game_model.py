'''
レーシングゲーム

int wheels;
String make;
String model;
int year;
String vin;
String color;
double velocity; // 速さ（マイル/秒）
double fuelEconomy; // 燃費（マイル/ガロン）
double tankCapacity; // ガスタンク容量（ガロン）
double weightKg; // 重さ（kg）

1 時間に進むことができる距離を計算する
停止せずに移動できる最大マイル数を計算する
ガソリンが空になるのにかかる時間を計算する（小数点第二位で四捨五入）
車が持つ運動エネルギーを計算する

'''

class Car:
    wheels = 4

    def __init__(self, make, model, year, vin, color, velocity, fuelEconomy, tankCapacity, weightKg):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.color = color
        self.velocity = velocity
        self.fuelEconomy = fuelEconomy
        self.tankCapacity = tankCapacity
        self.weightKg = weightKg

    def getCarString(self):
        return self.make + " " + self.model + " Year: " + str(self.year) + " Vin: " + self.vin + " Color: " + self.color + " Velocity: " + str(self.velocity) + "mps Fuel economy: " + str(self.fuelEconomy) + "mile/gallon Tank capacity: " + str(self.tankCapacity) + " Weight: " + str(self.weightKg) +"Kg. It has " + str(self.wheels) + " wheels."

    # 停止せずに移動できる最大マイル数を計算します
    # 燃費とタンクの大きさから算出できます
    def milesWithoutStop(self):
        return self.fuelEconomy * self.tankCapacity

    # 1 時間に進むことができる距離を計算します
    def getDistance(self):
        return self.velocity * 60 * 60

    # ガソリンが空になるのにかかる時間を計算します
    def hoursToEmpty(self):
        return round(self.milesWithoutStop() / self.getDistance(), 2)

    # 車が持つ運動エネルギーを計算します
    # 運動エネルギー　= 1/2 mv^2
    def getEnergy(self):
        return (self.velocity ** 2) * self.weightKg / 2

teslaS = Car("Tesla", "Model S", 2013, "5YJSA1CN0DFP13393", "Black", 0.04, 98 , 12, 2162)

print(teslaS.getCarString())
print(teslaS.milesWithoutStop())
print(teslaS.getDistance())
print(teslaS.hoursToEmpty())
print(teslaS.getEnergy())

porsche88 = Car("Porsche", "928", 1988, "WP0JB0926JS861742", "Red", 0.057, 36, 12, 1390)

print(porsche88.getCarString())
print(porsche88.milesWithoutStop())
print(porsche88.getDistance())
print(porsche88.hoursToEmpty())
print(porsche88.getEnergy())

ferrari08 = Car("Ferrari", "F430 Spyder", 2008, "ZFFEZ59E780163510", "Orange", 0.059, 11, 18, 1570)

print(ferrari08.getCarString())
print(ferrari08.milesWithoutStop())
print(ferrari08.getDistance())
print(ferrari08.hoursToEmpty())
print(ferrari08.getEnergy())
