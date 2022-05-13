'''
K個の最大値
medium
整数によって構成される intArr と整数 k（0 < k <= intArr.length）が与えられるので、
配列から k 個の最大値を返す、topKElements という関数を作成してください。

関数の入出力例
入力のデータ型： integer[] intArr, integer k
出力のデータ型： integer[]
topKElements([3,2,1,5,6,4],2) --> [6,5]
topKElements([3,2,1,5,6,4],3) --> [6,5,4]
topKElements([7,8,2,3,1,7,8,11,4,3,2],5) --> [11,8,8,7,7]
topKElements([6,4,6,2,4,8,10,10,12],5) --> [12,10,10,8,6]
topKElements([8,4,13,10,18],4) --> [18,13,10,8]
topKElements([3,100,201,56,8,591,985,291],4) --> [985,591,291,201]
topKElements([879,487,98,397,610,150,474,977,404,478,623,554,306],6) --> [977,879,623,610,554,487]
'''

import math

def topKElements(intArr,k):
    if k == len(intArr):
        return intArr

    results = []
    # heapsort() で intArr をヒープ構造にして昇順にソートする（一番上が最大値）
    sorted_intArr = heapsort(intArr)
    # k個の要素を取り出す
    for i, v in enumerate(sorted_intArr):
        if i == k:
            break
        results.append(v)

    return results

# 降順でのソート
def heapsort(intArr):
    # arrをヒープ構造にする。一番上を最大値にする
    Heap.buildMaxHeap(intArr)
    heapEnd = len(intArr) - 1

    while(heapEnd > 0):
        temp = intArr[heapEnd]
        intArr[heapEnd] = intArr[0]
        intArr[0] = temp
        heapEnd -= 1
        intArr = Heap.maxHeapify(intArr, heapEnd, 0)

    # reversed()で降順にする
    return reversed(intArr)

class Heap:
    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    @staticmethod
    def parent(i):
        return math.floor((i-1)/2)

    @staticmethod
    # ヒープのサイズを追跡するために引数にheapEndを追加する
    def maxHeapify(arr, heapEnd, i):
        l = Heap.left(i)
        r = Heap.right(i)

        biggest = i
        if l <= heapEnd and arr[l] > arr[biggest]:
            biggest = l
        if r <= heapEnd and arr[r] > arr[biggest]:
            biggest = r

        if biggest != i:
            temp = arr[i]
            arr[i] = arr[biggest]
            arr[biggest] = temp
            arr = Heap.maxHeapify(arr, heapEnd, biggest)
        return arr

    @staticmethod
    def buildMaxHeap(arr):
        middle = Heap.parent(len(arr))
        for i in range(middle, -1, -1):
            arr = Heap.maxHeapify(arr, len(arr)-1, i)
        return arr



# ---------------------------------------------------------

import math

def topKElements(intArr,k):
    # 関数を完成させてください
    # 入力配列の長さを崩さないならこのやり方。崩すならpop()を使ってもいいかも
    if k <= 0 and k > len(intArr): return []

    intArr = buildmaxHeep(intArr)
    heapEnd = len(intArr) - 1
    result = []
    cnt = 0
    while heapEnd > 0 and cnt < k:
        temp = intArr[0]
        intArr[0] = intArr[heapEnd]
        intArr[heapEnd] = temp
        result.append(temp)
        heapEnd -= 1
        intArr = maxHeapify(intArr, heapEnd, 0)
        cnt += 1
    return result

def buildmaxHeep(arr):
    middle = parent(len(arr))
    for i in range(middle, -1 , -1):
        arr = maxHeapify(arr, len(arr) - 1, i)
    return arr


# 配列、ヒープ確保の長さ、起点
def maxHeapify(arr, heapEnd, i):
    l = left(i)
    r = right(i)

    biggest = i

    if l <= heapEnd and arr[l] > arr[biggest]: biggest = l
    if r <= heapEnd and arr[r] > arr[biggest]: biggest = r

    if i != biggest:
        temp = arr[i]
        arr[i] = arr[biggest]
        arr[biggest] = temp
        arr = maxHeapify(arr, heapEnd, biggest)
    return arr


# 親半分のノードをノードを求める
def parent(i):
    return math.floor((i - 1) /2)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2
