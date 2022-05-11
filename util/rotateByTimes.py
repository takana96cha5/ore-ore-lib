'''
部屋替え

Glover は定期的に部屋替えを行うルールがあるシェアハウスに住んでいます。
くじ引きで数字をランダムに引いて、その数だけ住人が部屋をずらす仕組みです（例：数字 2 を引いたとき、部屋番号 1 に住んでいる人は 3 に移動します）。
住人たちの ID をまとめた ids と、くじ引きで引いた自然数 n が与えられるので、住人の位置をずらさせた配列を返す、rotateByTimes という関数を作成してください。
'''

def rotateByTimes(ids,n):
    # nが0の場合1度もローテーションさせずにidsを表示させる
    if n == 0:
        return ids

    # n回配列をローテーション（n回末尾の要素を頭に移動させる）
    array = rightShiftValue(ids)
    for _ in range(n-1):  # rightShiftValue()を実行するだけで1回末尾の要素が頭に移動するのでn-1
        array = rightShiftValue(array)
    return array


# 末尾の配列の要素を最初に移動させる関数
def rightShiftValue(array):

    # 末尾の要素からいじるので最初のindexは-1
    index = -1
    # 要素を追加していく新しいリスト
    newList = []

    for _ in array:
        # iは使わない。arrayの要素数だけ繰り返すためのfor
        newList.append(array[index])
        index += 1

    return newList

# ------------------------------------------------------------------------

# 時間計算量O(N)
# 空間計算量O(1)
import math
def reverseInPlace (arr, start, end) :

    middle = math.floor((start + end) / 2)
    for i in range(start, middle + 1) :

        opposite = start + (end - i)
        arr[i], arr[opposite] = arr[opposite], arr[i]

def rotateByTimes(ids,n):
    r = n % len(ids)
    if r == 0: return ids

    l = len(ids) - 1
    reverseInPlace(ids, 0, l)
    reverseInPlace(ids, 0, r-1)
    reverseInPlace(ids, r, l)

    return ids

print(rotateByTimes([1,2,3,4,5],2)) # [4,5,1,2,3]
print(rotateByTimes([1,2,3,4,5],5)) # [1,2,3,4,5]
print(rotateByTimes([10,12,3,4,5],3)) # [3,4,5,10,12]
print(rotateByTimes([4,23,104,435,5002,3],26)) # [5002,3,4,23,104,435]
print(rotateByTimes([4,23,104,435,5002,3],0)) # [4,23,104,435,5002,3]
print(rotateByTimes([4,23,104,435,5002,3],1)) # [3,4,23,104,435,5002]
print(rotateByTimes([4,23,104,435,5002,3],2)) # [5002,3,4,23,104,435]
print(rotateByTimes([2,3],1)) # [3,2]

# ------------------------------------------------------------------------
def rotateByTimes(ids,n):
    if n >= len(ids):
        n = n % len(ids)
    for i in range(n):
        ids.insert(0, ids.pop())
    return ids
