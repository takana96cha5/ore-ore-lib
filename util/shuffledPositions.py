'''
配列のシャッフル

mith は間違い探しゲームに参加しました。
異なる数字が並べられているボード arr と同じ数字がシャッフルされたボード shuffledArr が与えられるので、
shuffledArr に対して arr がどこのインデックスへ移動したかを返す、
shuffledPositions という関数を定義してください。
'''

def shuffledPositions(arr:int,shuffledArr:int) -> str:
    # ハッシュマップを作ります。
    hashmap = {}
    # shuffledArrをループして、要素とそのインデックスをハッシュマップに入れます。
    for i in range(len(shuffledArr)) :
        hashmap[shuffledArr[i]] = i

    # 答えを入れる配列を初期化します。
    res = []
    # arrをループしてハッシュマップに保存した要素のインデックスをO(1)で取得します。
    for i in range(len(arr)) :
        res.append(hashmap[arr[i]])

    return res

print(shuffledPositions([2,32,45],[45,32,2])) # [2,1,0]
print(shuffledPositions([10,11,12,13],[12,10,13,11])) # [1,3,0,2]
print(shuffledPositions([10,11,12,13],[10,11,12,13])) # [0,1,2,3]
print(shuffledPositions([1350,181,1714,375,1331,943,735],[1714,1331,735,375,1350,181,943])) # [4,5,0,3,1,6,2]

'''
shuffledPositions([2,32,45],[45,32,2]) --> [2,1,0]

shuffledPositions([10,11,12,13],[12,10,13,11]) --> [1,3,0,2]

shuffledPositions([10,11,12,13],[10,11,12,13]) --> [0,1,2,3]

shuffledPositions([1350,181,1714,375,1331,943,735],[1714,1331,735,375,1350,181,943]) --> [4,5,0,3,1,6,2]
'''
