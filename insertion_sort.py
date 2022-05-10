def insertionSort(arrList):
    n = len(arrList)

    for i in range(n):
        currentValue = arrList[i]
        # currentValue の左側を探索し、挿入できる箇所を探索します
        for j in range(i - 1, -1, -1):
            # currentValue が小さい場合は、値を入れ替えていきます
            if currentValue <= arrList[j]:
                arrList[j+1] = arrList[j]
                arrList[j] = currentValue
            # currentValue が大きい場合は、、それは正しい位置にあるので、ループを終了して i+1 に移動します
            else: break

arr = [34,4546,32,3,2,8,6,76,56,45,34,566,1]
print(arr)

# 昇順に並び替え
insertionSort(arr)

# ソートされた配列
print(arr)
