'''
Tayler は友達から年利 20% で 10,000 ドル借金をしています。
そこで関数を開発することによって数年後に借金がどれほど膨らむのかシュミレーションすることにしました。
年数 year が与えられるので、返済額を計算する howMuchYourDebt という関数を作成してください。
小数点以下は切り捨てとします。
'''

import math # ライブラリの読み込み

def howMuchIsYourDebt(year:int) -> int:
   interest = 0.2 # 年利 20%
   initialDebt = 10000 # 元金 10000 ドル

   # math.pow() を使って 1.2 の年数乗を計算します。
   # floor で小数点以下を切り捨てます。
   return math.floor(initialDebt * math.pow((1+interest),year))

# --------------以下は解答に書く必要はありません---------------------
# テストケースを入れた関数を呼び出し、print() で表示してみましょう
print(howMuchIsYourDebt(2)) # 14400
print(howMuchIsYourDebt(5)) # 24883
print(howMuchIsYourDebt(10)) # 61917
