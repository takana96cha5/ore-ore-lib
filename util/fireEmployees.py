'''
Cole はある企業の人事として働いており、従業員のリストを整理しています。
従業員のリスト employees と来月解雇されるリスト unemployed が与えられるので、
来月残留する従業員の配列を返す fireEmployees という関数を定義してください。
'''

def fireEmployees(employees:str,unemployed:str) -> str:

    # 空の辞書を作成
    employeesList = {}

    for i in employees:
        employeesList[i] = True     # {'○○': True, '△△': True}を作る

    for i in unemployed:
        employeesList[i] = False    # unemplyedに名前がある人は↑から'○○': Falseになる

    # 来月残留する従業員リスト
    newEmplyeesList = []

    for i in employees:
        if employeesList[i]:
            newEmplyeesList.append(i)

    return newEmplyeesList

# ------------------------
def fireEmployees(employees,unemployed):
    ans = []
    for i in employees:
        if not i in unemployed:
            ans.append(i)
    return ans
