'''
ヒープソート
medium
整数によって構成される intArr が与えられるので、
ヒープソートアルゴリズムによって、昇順ソートする、heapsort という関数を作成します。
配列の要素間の入れ替えをすることによって、空間計算量 O(1) で実装してください。

関数の入出力例
入力のデータ型： integer[] intArr
出力のデータ型： integer[]
heapsort([1,2,3]) --> [1,2,3]
heapsort([1,2,3,4]) --> [1,2,3,4]
heapsort([1,2,3,4,5]) --> [1,2,3,4,5]
heapsort([6,5,4,3,2,1,0,-1,-2,-3,-4,-5]) --> [-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
heapsort([3,4,5,5,5,6,7,2,10,2,1,-10,2,-2,0,-1]) --> [-10,-2,-1,0,1,2,2,2,3,4,5,5,5,6,7,10]
'''

import math

# 昇順でのソート
def heapsort(intArr):
    # 関数を完成させてください
    # arrをヒープ構造にする。一番上を最大値にする
    intAr = buildmaxHeap(intArr)
    heapEnd = len(intArr) - 1

    while(heapEnd > 0):
        temp = intArr[heapEnd]
        intArr[heapEnd] = intArr[0]
        intArr[0] = temp
        heapEnd -= 1
        intArr = maxHeapify(intArr, heapEnd, 0)

    return intArr



def buildmaxHeap(arr):
    middle = parent(len(arr))
    for i in range(middle, -1, -1):
        arr = maxHeapify(arr, len(arr) - 1, i)
    return arr


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
        # print(arr , i ,biggest)
        arr = maxHeapify(arr, heapEnd, biggest)

    return arr


def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return math.floor((i - 1) / 2)


# ----------------------------------------------------

import math

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

def heapsort(intArr):
    # buildMaxHeap()でintArrをヒープ構造にする（1番上は最大値になっている）
    Heap.buildMaxHeap(intArr)

    # ヒープサイズを追跡するために heapEnd(インデックスの値) を配列の最後の要素にする
    heapEnd = len(intArr) - 1
    while heapEnd > 0:
        # 最大値である根ルートと葉ノードのheapEndを入れ替える
        temp = intArr[heapEnd]
        intArr[heapEnd] = intArr[0]
        intArr[0] = temp

        # 一番最後はソートされているのでheapEndから-1する
        heapEnd -= 1
        Heap.maxHeapify(intArr, heapEnd, 0)

    return intArr
