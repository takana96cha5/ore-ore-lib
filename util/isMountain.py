'''
山型

Bond はクラスの文化祭で行う劇で背景を制作することになり、現在は山を作っています。
各地点での山の高さの一覧 height が与えられるので、山型になっているかどうか判断する isMountain という関数を定義してください。

山型の条件は以下の通りです。
- 配列のサイズが 3 以上であること。
- 高さは初めは上がり続け、一度下がったら下がり続けること。（例:1,2,3,4,5,3,2,1）
'''
def isMountain(height:int) -> bool:

    # 配列のサイズが3未満、隣り合う配列が同じ数値の場合はFalse
    if len(height) < 3  or isFlat(height) or isBig(height):
        return False

    # 最後の値が昇順になっていたらFalse
    if height[len(height)-2] < height[len(height)-1]:
        return False

    # 凸部分が1回のみあればTrue
    count = 0
    for i in range(0, len(height)-2): # 終点が降順であることは↑で確認しているのでlen(height)-2
        if height[i] < height[i+1] and height[i+1] > height[i+2]:
            count += 1

    if count != 1:
        return False

    return True


# 1番目の数値が2番目より大きいか判定する関数
def isBig(array):
    if array[0] > array[1]:
        return True
    return False

# 隣り合う配列が同じ値か判定する関数
def isFlat(array):
    for i in range(0, len(array)-1):
        if array[i] == array[i+1]:
            return True
    return False

'''
TestCase

isMountain([1,2,3,2]) --> true
isMountain([1,2]) --> false
isMountain([2,1]) --> false
isMountain([1,2,2,2,2]) --> false
isMountain([1,2,3]) --> false
isMountain([4,3,2,1]) --> false
isMountain([1,2,2,2,3,2]) --> false
isMountain([3,2,2,2,1,1]) --> false
isMountain([10,20,30,400,500,10]) --> true
isMountain([100,200,100,400,500,100]) --> false
isMountain([100,200,300,200,100,300]) --> false
isMountain([100,50,100,200,300,400]) --> false
isMountain([53,158,477,994,994,867,797,755,744,621,616]) --> false
'''
