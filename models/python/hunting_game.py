'''
String species // 種
double weightKg // 体重
double heightM // 身長
boolean predator // 動物が捕食者であるかを表します
void domesticate() // 捕食者状態を false に変更します
'''

class Animal:
    def __init__(self, species, weightKg, heightM, predator):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator

    # 捕食者かどうかの状態を変更します
    def domesticate(self):
        self.predator = False

def printAnimal(animal):
    print("The animal species is: " + animal.species + ". It's weight is: " + str(animal.weightKg) + "kg and its height is: " + str(animal.heightM) + "m. " + ("It is a predator!" if animal.predator else "It is a peaceful animal."))

tiger1 = Animal("Tiger", 290, 2.6, True)
bear1 = Animal("Bear", 250, 2.8, True)
snake1 = Animal("Snake", 250, 12.8, True)
dog1 = Animal("Dog", 90, 1.2, False)
cat1 = Animal("Cat", 40, 0.5, False)
cow1 = Animal("Cow", 1134, 1.5, False)

printAnimal(tiger1)
printAnimal(bear1)
printAnimal(cat1)

print("Time to tame the tiger...")

# tiger の状態を捕食者から変え、文字列が predator から peaceful animal になるのを確認しましょう
tiger1.domesticate()
printAnimal(tiger1)

'''
String name // 名前
int age // 年齢
double weightKg // 体重
double heightM // 身長
double strength // 強さ
double cageCubicMeters // ハンターが所有する檻のサイズ
double strengthKg() // ハンターの力。体重と強さを掛け合わせた値を返します
boolean canCaptureAnimal(Animal animal)
// 動物を入力として受け取り、ハンターが動物を捕獲できるかブーリアン値で判定します
// ①ハンターの強さ >= 動物の体重、②檻のサイズ >= 動物の身長、③動物が捕食者ではない
// の全ての条件を満たしている場合のみ true を返します
boolean attemptToDomesticate(Animal animal)
// 動物を入力として受け取り、動物を家畜として飼いならすことができるかブーリアン値で判定します
// ハンターの力 > 動物の体重 × 2 の場合、動物は捕食者ではなくなり、true を返します
'''

# ハンター
class Hunter:
    def __init__(self, name, age, weightKg, heightM, strength, cageCubicMeters):
        self.name = name
        self.age = age
        self.weightKg = weightKg
        self.heightM = heightM
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters

    def canCaptureAnimal(self, animal):
        return True if (self.strengthKg() >= animal.weightKg and self.cageCubicMeters >= animal.heightM) and not animal.predator else False

    def attemptToDomesticate(self, animal):
        if self.strengthKg() <= animal.weightKg * 2:
            return False
        animal.domesticate()
        return True

    def strengthKg(self):
        return self.weightKg * self.strength

def printHunter(hunter):
    print("The hunter's name is: " + hunter.name + ". This hunter can carry: " + str(hunter.strengthKg()) + "kg and has a cage " + str(hunter.cageCubicMeters) + " cubic meters wide")

# 動物
class Animal:
    def __init__(self, species, weightKg, heightM, predator):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator

    def domesticate(self):
        self.predator = False

def printAnimal(animal):
    print("The animal species is: " + animal.species + ". It's weight is: " + str(animal.weightKg) + "kg and its height is: " + str(animal.heightM) + "m. " + ("It is a predator!" if animal.predator else "It is a peaceful animal."))

# 各動物
tiger1 = Animal("Tiger", 290, 2.6, True)
bear1 = Animal("Bear", 250, 2.8, True)
cat1 = Animal("Cat", 29, 0.5, False)
cow1 = Animal("Cow", 1134, 1.5, False)

# 各ハンター
hunternator = Hunter("Hunternator", 30, 124.73, 1.85, 15, 3)
hunterChild = Hunter("Hunter Child Of The Small Giants", 10, 50, 1.2, 0.6, 1)

# 関数の呼び出し
printHunter(hunternator)
printAnimal(tiger1)

print("Can " + hunternator.name + " capture " + tiger1.species + "? The answer is..." + str(hunternator.canCaptureAnimal(tiger1)))
print("Will " + hunternator.name + " be able to domesticate the " + tiger1.species + "?" + " The answer is..." + str(hunternator.attemptToDomesticate(tiger1)))

printAnimal(tiger1)
print("Can " + hunternator.name + " capture " + tiger1.species + "? The answer is..." + str(hunternator.canCaptureAnimal(tiger1)))
