'''
二分探索木内のキー
異なる整数値で構成される二分探索木（BST）の根ノード root と整数 key が与えられるので、
key が BST の中に存在するかどうか判定する exist という関数を作成してください。
key が BST の中に存在していれば true を、そうでなければ false を返してください。

関数の入出力例
入力のデータ型： binaryTree<integer> root, integer key
出力のデータ型： bool
exists( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> true
exists( toBinaryTree([0,-10,5,null,-3,null,18]), 20 )--> false
exists( toBinaryTree([5,3,6,2,4,null,7]), 3 )--> true
exists( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> true
exists( toBinaryTree([5,3,6,2,4,null,7]), 15 )--> false
'''

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def exists(root,key):
    iterator = root
    # iteratorがnullでない間ループします。
    while iterator is not None:
        # keyを見つけたらTrueを返します。
        if iterator.data == key: return True
        # 現在のノードよりキーが小さければ左に、大きければ右に辿ります。
        if iterator.data < key: iterator = iterator.right
        else: iterator = iterator.left

    # 見つからなかった場合、Falseを返します。
    return False
