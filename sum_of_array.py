'''分割統治法を使った配列の合計値'''
import math

def sumOfArray(arr):
    return sumOfArrayHelper(arr, 0, len(arr)-1)

def sumOfArrayHelper(arr, start, end):
    if start == end:
        return arr[start]

    mid = math.floor((start+end)/2)

    leftArr = sumOfArrayHelper(arr, start, mid)
    rightArr = sumOfArrayHelper(arr, mid+1, end)

    # 単一要素同士を足します
    return leftArr + rightArr

arr = [2,4,6,8,10,12]
print(sumOfArray(arr))
