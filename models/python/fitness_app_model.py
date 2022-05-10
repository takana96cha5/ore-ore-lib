'''
フィットネスアプリケーション

String firstName: // 名
String lastName: // 姓
double heightM: // 身長（メートル）
double weigthKg: // 体重（キログラム）
int birthYear: // 生まれた年

String person.getFullName(): // フルネームを返します
String person.getAge(): // 年齢を返します
double person.getBmi(): // BMI を返します
double person.eat(int calories): // カロリーを入力として受け取り、摂取後の新しい体重を返します


運動の種類を受け取り、1 分間に消費されたカロリー数を計算する
運動の種類を受け取り、1kg 痩せるのに何時間かかるかを計算する
運動の種類、時間から、新しい体重を計算する
'''

import datetime

class Person:
    def __init__(self, firstName, lastName, heightM, weightKg, birthYear):
        self.firstName = firstName
        self.lastName = lastName
        self.heightM = heightM
        self.weightKg = weightKg
        self.birthYear = birthYear

    # 状態を文字列で表示します
    def getStateString(self):
        return "First Name: " + self.firstName + ", Last Name: " + self.lastName + ", heightM: " + str(self.heightM) + ", weightKg: " + str(self.weightKg) + ", birthYear: " + str(self.birthYear)

    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getAge(self):
        # datetime ライブラリを使って、現在の年を取得します
        # datetime.datetime.now() は今を表すオブジェクトを返します。このオブジェクトの中には、year, month, hour, minuteなどの変数があります
        currentYear = datetime.datetime.now().year
        return currentYear - self.birthYear

    def getBmi(self):
        # BMI の公式は、体重(kg) / 高さ(m) の 2 乗です
        return self.weightKg / (self.heightM ** 2)

    # カロリーを受け取り、摂取後の体重を計算します
    def eat(self, calories):
        # 7700 カロリーにつき、1 キロ増加します
        self.weightKg += calories/7700
        return self.weightKg

    # 運動を文字列として受け取り、1 分間に消費されたカロリー数を返します
    def caloriesBurnedPerMinuteExercise(self, exercise):
        # 燃焼カロリーは MET(Metabnolic Equivalent of Task) を使って計算することができます
        met = 1
        if exercise == "running": met = 8
        elif exercise == "walking": met = 3
        elif exercise == "tennis": met = 5
        elif exercise == "rope jump": met = 9
        # 燃焼カロリーは、met * 3.5 * weight / 200 によって計算することができます
        return met * 3.5 * self.weightKg / 200

    # 運動を文字列として受け取り、1 kg痩せるのに何時間かかるかを返します
    def hoursToLose1KgByExercise(self, exercise):
        return 7700 / (self.caloriesBurnedPerMinuteExercise(exercise) * 60)

    # 運動、時間を入力として受け取り、燃焼されたカロリー数を計算し、体重を更新して新しい体重を返します
    def exercise(self, exercise, minutes):
        # 関数の分解
        caloriesBurned = self.caloriesBurnedPerMinuteExercise(exercise) * minutes
        self.weightKg -= caloriesBurned/7700
        return self.weightKg

carly = Person("Carly", "Angelo", 1.72, 85.5, 1996)
# carly の状態を出力します
print(carly.getStateString())

print("Carly burns: " + str(carly.caloriesBurnedPerMinuteExercise("running")) + " calories per minute running")
print("It takes carly: " + str(carly.hoursToLose1KgByExercise("running")) + " hours running to burn 1 kg")

carly.exercise("running", 600)

print("Carly went running for 10 hours.")
print(carly.getStateString())
