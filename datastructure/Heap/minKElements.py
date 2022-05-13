'''
K個の最小値
medium
整数によって構成される intArr と整数 k（0 < k <= intArr.length）が与えられるので、
配列から k 個の最小値を返す、minKElements という関数を作成してください。

関数の入出力例
入力のデータ型： integer[] intArr, integer k
出力のデータ型： integer[]
minKElements([3,2,1,5,6,4],2) --> [1,2]
minKElements([3,2,1,5,6,4],3) --> [1,2,3]
minKElements([7,8,2,3,1,7,8,11,4,3,2],5) --> [1,2,2,3,3]
minKElements([6,4,6,2,4,8,10,10,12],5) --> [2,4,4,6,6]
minKElements([8,4,13,10,18],4) --> [4,8,10,13]
minKElements([3,100,201,56,8,591,985,291],4) --> [3,8,56,100]
minKElements([879,487,98,397,610,150,474,977,404,478,623,554,306],6) --> [98,150,306,397,404,474]
'''

import math

def minKElements(intArr,k):
    # buildMinHeap で intArr をヒープ構造にする（一番上が最小値）
    intArr_heap = Heap.buildMinHeap(intArr)
    heapEnd = len(intArr) - 1

    results = []
    count = 0
    while heapEnd > 0 and count < k:
        temp = intArr[0]
        intArr[0] = intArr[heapEnd]
        intArr[heapEnd] = temp
        # 最小値をresultsに格納
        results.append(intArr[heapEnd])
        heapEnd -= 1
        Heap.minHeapify(intArr, heapEnd, 0)
        count += 1

    return results

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
    def minHeapify(arr, heapEnd, i):
        l = Heap.left(i)
        r = Heap.right(i)

        smallest = i
        if l <= heapEnd and arr[l] < arr[smallest]:
            smallest = l
        if r <= heapEnd and arr[r] < arr[smallest]:
            smallest = r

        if smallest != i:
            temp = arr[i]
            arr[i] = arr[smallest]
            arr[smallest] = temp
            arr = Heap.minHeapify(arr, heapEnd, smallest)
        return arr

    @staticmethod
    def buildMinHeap(arr):
        middle = Heap.parent(len(arr))
        for i in range(middle, -1, -1):
            arr = Heap.minHeapify(arr, len(arr)-1, i)
        return arr

# -----------------------------------------------------------


import math

def minKElements(intArr,k):
    # 関数を完成させてください
    if k <= 0 or k > len(intArr): return []

    intArr = buildminHeap(intArr)
    heapEnd = len(intArr) - 1
    result = []
    cnt = 0

    while heapEnd > 0 and cnt < k:
        temp = intArr[0]
        intArr[0] = intArr[heapEnd]
        intArr[heapEnd] = temp
        result.append(intArr[heapEnd])
        heapEnd -= 1
        intArr = minHeapify(intArr, heapEnd, 0)
        cnt += 1

    return result

def buildminHeap(arr):
    middle = parent(len(arr))
    for i in range(middle, -1, -1):
        arr = minHeapify(arr, len(arr)- 1, i)

    return arr

def minHeapify(arr, heapEnd, i):
    l = left(i)
    r = right(i)

    smallest = i

    if l <= heapEnd and arr[l] < arr[smallest]: smallest = l
    if r <= heapEnd and arr[r] < arr[smallest]: smallest = r

    if i != smallest:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        arr = minHeapify(arr, heapEnd, smallest)

    return arr

def left(i):
    return 2 * i + 1

def right(i):
    return 2* i + 2

def parent(i):
    return math.floor((i - 1)/ 2)
