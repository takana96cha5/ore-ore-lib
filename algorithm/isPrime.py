'''
素数

Kate は音楽の野外フェスを行うことになり、入場者の中から抽選でプレゼントを渡す企画を立てています。
そこで、素数の値で入場した方を当選者とすることにしました。
入場者番号 number が与えられるので、素数かどうか判定する isPrime という関数を作成してください。
'''
def isPrime(number:int) -> bool:
    # O(√N)
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
