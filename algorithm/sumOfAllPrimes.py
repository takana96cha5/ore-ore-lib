'''
素数の和

ある国は長く存続できたことに感謝を込め、国民に給付金を渡そうと考えました。
そこで、建国から経過した年数 n までに含まれている、全ての素数を足した数を給付金にする予定です。
自然数 n が与えられるので、給付金の額を返す sumOfAllPrimes という関数を作成してください。
'''

def sumOfAllPrimes(n):
    sumOfPrimes = 0     # 素数の合計

    # k番目の値が素数か調べます
    for k in range(2, n + 1):
        if isPrime(k): sumOfPrimes += k

    return sumOfPrimes

# 素数か判定する関数
def isPrime(number):
    # 2からnumber-1までの値で割り切れる数があればfalseを返します
    for i in range(2, number):
        if number % i == 0: return False
    # numberが1の場合はfalseを返します
    return number > 1

print(sumOfAllPrimes(1))
print(sumOfAllPrimes(2))
print(sumOfAllPrimes(3))
print(sumOfAllPrimes(100))
