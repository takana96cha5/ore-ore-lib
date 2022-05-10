'''
String name	動物の名前
double weightKg	動物の体重
double heightM	動物の身長
boolean isPredator	捕食者かどうか
double speedKph	動物の時速
double activityMultiplier	どれほど動物が活発的か表す数字。動物園の動物は檻に入れられているので活動が制限されているとみなし、活動指数を 1.2 とします。
double getBmi()	動物の BMI を返します。kg / (heightM2) を使ってください。小数点第 2 位以下を切り捨ててください。
double getDailyCalories()	動物が毎日どれほどのカロリーを消費する必要があるか返します。計算式は (70 × weightKg0.75) × activityMultiplier で求めることができます。小数点第 3 位以下を切り捨ててください。
boolean isDangerous()	動物が危険かどうか判断するブーリアン値を返します。動物が捕食者だった場合、危険とみなされ、身長が 1.7 メートル以上、もしくは時速 35km/h 以上の場合も危険とみなされます。
'''

import math

class Animal:
    def __init__(self, name, weightKg, heightM, isPredator, speedKph):
        self.name = name
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
    def activityMultipller(self):
        return 1.2
    def getBmi(self):
        return math.floor(self.weightKg / (self.heightM ** 2) * 100) / 100
    def getDailyCalories(self):
        return math.floor((70 * self.weightKg ** 0.75) * 1.2 * 100) / 100
    def isDangerous(self):
        if self.isPredator == True:
            return True
        elif self.heightM >= 1.7 or self.speedKph >= 35:
            return True
        else:
            return False

rabbit = Animal("rabbit", 10, 0.3, False, 20)
print(rabbit.getBmi())
print(rabbit.isDangerous())

snake = Animal("snake", 30, 1, True, 30)
print(snake.isDangerous())
print(snake.getDailyCalories())

elephant = Animal("elephant", 300, 3, False, 5)
print(elephant.getBmi())
print(elephant.getDailyCalories())

gazelle = Animal("gazelle", 50, 1.5, False, 100)
print(gazelle.getDailyCalories())
print(gazelle.isDangerous())
