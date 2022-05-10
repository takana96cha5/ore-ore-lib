'''
String name	犬の種類の名前
int size	犬のサイズ
int age	犬の年齢
String bark()	犬の鳴き声を文字列として返します。犬のサイズが 50 以上の時、Wooof! Woof!、サイズが 20 以上の時、Ruff! Ruff!、それ以外の時は、Yip! Yip! と返します。
int calcHumanAge()	犬の年齢から人間の年齢に換算します。人間の年齢＝ 12 +（犬の年齢 - 1）× 7 を使用してください。
'''
class Dog():
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def bark(self):
        if self.size >= 50:
            return 'Wooof! Woof!'
        elif self.size >= 20:
            return 'Ruff! Ruff!'
        else:
            return 'Yip! Yip!'

    def calcHumanAge(self):
        return 12 + (self.age - 1) * 7

goldenRetriever = Dog("Golden Retriever", 60, 10)
print(goldenRetriever.bark())
print(goldenRetriever.calcHumanAge())

siberianHusky = Dog("Siberian Husky", 55, 6)
print(siberianHusky.bark())
print(siberianHusky.calcHumanAge())

poodle = Dog("poodle", 10, 1)
print(poodle.bark())
print(poodle.calcHumanAge())

shibaInu = Dog("shibaInu", 35, 4)
print(shibaInu.bark())
print(shibaInu.calcHumanAge())
