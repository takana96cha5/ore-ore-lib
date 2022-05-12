import math

class BinaryTree:
    def __init__(self, data):
        self.data = data
        # 左二分木
        self.left = None
        # 右二分木
        self.right = None

'''
ソート済みのリストをBSTに移行するアルゴリズムを再帰的に実装していきます。

二分探索木へ変換するにあたって、二分探索木の探索効率を最高にするためには、木の高さが重要でした。
木の高さを小さく抑えるためには、左右の要素をほぼ均等に配置する必要があります。

ここで二分木の性質を利用し、配列の中間の要素をルートとします。
それを中心に左側は左部分木、右側は右部分木として再帰的に分割することによって、
最終的に平衡二分探索木を構築することができます。

ここでも中級で学習した分割統治法を使用することがわかるかと思います。
ベースケースを設定し、ベースケースに到達するまで問題を複数の部分問題に分割して考えてみましょう。
再帰の流れを具体的に [1,2,3,4,5,6,7] の例で説明します。

(1) 配列の start と end（インデックス）を追跡するため、
ヘルパー関数 sortedArrToBSTHelper を用意します。
start は 0、end は 6 としてスタートします。

(2) 現在の中間の要素のインデックスは 3 なので、
区間 (0, 2) を左部分木とし、区間 (4,6) を右部分木にします。

(3) 先に左部分木に相当する sortedArrToBST(0,2) を呼び出します。
現在の中間の要素のインデックスは 1 なので、区間 (0,0) を左部分木とし、
区間 (2,2) を右部分木とします。
このように start と end が同じになった時をベースケースとします。
要素が 1 つになった時に新しいノードを作って再帰を終了します。

ここでお気づきかと思いますが、要素が１つになったのでそれぞれ左ノードと右ノードとして返します。

(4) 次に右部分木に相当する sortedArrToBST(4,6) を呼び出します。
現在の中間の要素のインデックスは 5 なので、区間 (4,4) を左部分木とし、
区間 (6,6) を右部分木とします。
ここでも要素が 1 つになったのでそれぞれ左ノードと右ノードとして返します。

(5) 最後に配列の中心を根ノードとして、左右の部分木を合わせて新しいノードにします。

'''
def sortedArrayToBSTHelper(arr, start, end):
    if start == end: return BinaryTree(arr[start], None, None)

    mid = math.floor((start+end)/2)

    left = None
    if mid-1 >= start: left = sortedArrayToBSTHelper(arr, start, mid-1)

    right = None
    if mid+1 <= end: right = sortedArrayToBSTHelper(arr, mid+1, end)

    root = BinaryTree(arr[mid], left, right)
    return root

def sortedArrayToBST(nums):
    if len(nums) == 0: return None
    return sortedArrayToBSTHelper(nums, 0, len(nums)-1)

# BSTリストの中にキーが存在かどうかによって、true、falseを返します。
# 再帰
def keyExist(key, bst):
    if bst == None: return False
    if bst.data == key: return True

    # 現在のノードよりキーが小さければ左に、大きければ右に辿ります。
    if bst.data > key: return keyExist(key, bst.left)
    else: return keyExist(key, bst.right)



# ツリーの合計値を返す関数
def sumOfThreeNodes(root):
    if root is None: return 0
    if root.right is None:right = 0
    else:right = root.right.data
    if root.left is None:left = 0
    else:left = root.left.data
    return root.data + left + right



binaryTree = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)

binaryTree.left = node2
binaryTree.right = node3

if __name__ == '__main__':
    print("Root: " + str(binaryTree.data))
    print("Left: " + str(binaryTree.left.data))
    print("Right: " + str(binaryTree.right.data))

    balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
    print(balancedBST)


    balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
    print(keyExist(6, balancedBST))
    print(keyExist(10, balancedBST))
    print(keyExist(45, balancedBST))

