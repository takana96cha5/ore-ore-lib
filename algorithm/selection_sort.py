def selectionSort(numList):
    n = len(numList)

    for i in range(n):
        # i 番目の値を暫定の最小値とします
        minIndex = i

        # i 番目より後ろから最小値を探します
        for j in range(i + 1, n):
            # 暫定の最小値以下なら最小値を更新
            if numList[j] <= numList[minIndex]:
                minIndex = j

        # 最小値と先頭を in-place で入れ替え
        temp = numList[i]
        numList[i] = numList[minIndex]
        numList[minIndex] = temp

arr = [34,4546,32,3,2,8,6,76,56,45,34,566,1]

# 昇順に並び替え
selectionSort(arr)

# ソートされた配列
print(arr)
