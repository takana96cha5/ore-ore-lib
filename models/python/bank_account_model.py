'''
あなたは銀行をシュミレーションするビデオゲームに機能を追加しています。この銀行はプレイヤーのお金を BankAccount クラスで管理し、いくつかの機能を提供します。以下に従って、BankAccount クラスを作成し、テストケースを出力してください。

String bankName	銀行口座を管理する銀行名
String ownerName	銀行口座の所有者の名前
int savings	銀行口座の中に現在ある合計貯蓄額
int depositMoney(int depositAmount)	depositAmount によって貯蓄額を増やし、その金額を int 型で返します。もし預金前の貯蓄額が $20,000 以下の場合は、$100 の手数料がかかります。
int withdrawMoney(int withdrawAmount)	withdrawAmount によって貯蓄額を減らし、残りの貯蓄額を整数として返します。最大で貯蓄額の 20% を引き出すことができます。
double pastime(int days)	口座に毎日 0.25 ドル振り込まれていくとき、貯蓄金額を double 型で返します。
'''
import math

class BankAccount:

    def __init__(self, bankName, ownerName, savings):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings

    def depositMoney(self, depositAmount):
        serviceFee = 100 if self.savings <= 20000 else 0
        self.savings += math.floor(depositAmount - serviceFee)
        return self.savings

    def withdrawMoney(self, withdrawAmount):
        maxEnableWithdrawMoneyAmount = self.savings * 0.2
        enableWithdrawMoneyAmount = withdrawAmount if withdrawAmount < maxEnableWithdrawMoneyAmount else maxEnableWithdrawMoneyAmount
        self.savings -= math.floor(enableWithdrawMoneyAmount)
        return self.savings

    def pastime(self, days):
        transferMoneyAmount = 0.25
        self.savings += transferMoneyAmount * days
        return self.savings

user1 = BankAccount("Chase", "Claire Simmmons", 30000)
print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000)
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))
