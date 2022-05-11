'''
投資の計算

Kathy は現在価格 goalMoney ドルの土地の購入するために、年利 interest（0 < interest < 100）%の金融商品に capitalMoney ドル投資しようと計画しています。
goalMoney, interest, capitalMoney が与えられるので、何年後に土地の購入ができるかを返す、howLongToReachFundGoal という関数を再帰によって作成してください。
なお、毎年得られた利益は同商品に再投資するとし、土地の価格は経過する年数が偶数（0 を含む）の時は 2%、奇数の時は 3% 上昇します。
また、人の寿命は 80 歳未満と仮定し、80 年以上かかる時は 80 としてください。
'''

def howLongToReachFundGoal(capitalMoney:int,goalMoney:int,interest:int) -> int:
    # helper関数に移ります
    return howLongToReachFundGoalHelper(capitalMoney,goalMoney,interest,0)

# 引数に year を追加し、経過年を追跡できるようにします
def howLongToReachFundGoalHelper(capitalMoney:int,goalMoney:int,interest:int,year:int) -> int:
    # capitalMoney が goalMoney 以上になったら経過年を返します
    if capitalMoney >= goalMoney: return year
    # 80年以上経過した場合は 80 を返します
    if year >= 80: return 80

    # 経過年 year が偶数の時は goalMoney を 2% 、奇数の時は 3% 増加させます
    if year % 2 == 0: goalMoney *= 1.02
    else: goalMoney *= 1.03

    # capitalMoney に年利を加えます
    capitalMoney *= (1+interest/100)

    # year に 1 加えて再帰を行います
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year+1)
    # 末尾再帰により空間計算量は O(1), 時間計算量は O(n) になります。howLongToReachFundGoalHelper は自身を n回 作成します。

print(howLongToReachFundGoal(5421,10421,5))
print(howLongToReachFundGoal(5421,30,30))
print(howLongToReachFundGoal(600,10400,7))
