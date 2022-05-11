'''
パーフェクトナンバー

Mayer は、6 と 6 以外の約数 1, 2, 3 を全てを足した値が一致することに気が付きました。他にもあるのではないかと思い、同様の値を見つけようとしています。
自然数 n が与えられるので、1 から n のうち perfect number（自然数 n と、その数自身を除く自然数 n の約数を全て足し上げたものが一致する値）を返す、perfectNumberList という関数を作成してください。
perfect が存在しない場合は、none と返してください。
'''

import math
def perfectNumberList(n:int) -> int:
    numbers = ''
    for i in range(2, n+1) :
        # パーフェクトナンバーのときだけ追加する
        if isPerfect(i): numbers += str(i) + '-'
    # 文字列が空のとき、つまりパーフェクトナンバーが存在しないときは、noneを返す
    # それ以外の時は、-を除いて返す
    return numbers[0:-1] if numbers != '' else 'none'

# 数値を受け取って、パーフェクトナンバーかどうかチェックする関数
def isPerfect(x:int) -> bool :
    # 以下の処理で1とxを除くので、あらかじめ1を足しておく
    divisors = 1
    n = math.ceil(math.sqrt(x))
    # 約数を足し上げる（1とxを除く）
    for i in range(2, n) :
        if x % i == 0:
            # 割り切れるとき、その数とそのペアを足す
            # 例えば、20/2をしたとき、2と10を足すイメージ
            divisors += i
            divisors += x / i
    # xと合計値が同じかどうかチェックする
    return x == int(divisors)

print(perfectNumberList(3)) # none
print(perfectNumberList(6)) # 6
print(perfectNumberList(28)) # 6-28
print(perfectNumberList(100)) # 6-28
print(perfectNumberList(496)) # 6-28-496
print(perfectNumberList(1000)) # 6-28-496
print(perfectNumberList(10000)) # 6-28-496-8128
