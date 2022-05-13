'''
二分探索木内探索

二分探索木（BST）の根ノード root と整数 key が与えられるので、
key と等しい部分木の根ノードを返す、bstSearch という関数を作成してください。
そのようなノードが存在しない場合は、null を返してください。

関数の入出力例
入力のデータ型： binaryTree<integer> root, integer key
出力のデータ型： binaryTree<integer>
bstSearch( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [5,null,9]
bstSearch( toBinaryTree([0,-10,5,null,-3,null,9]), 20 )--> []
bstSearch( toBinaryTree([5,3,6,2,4,null,7]), 3 )--> [3,2,4]
bstSearch( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> [5,3,6,2,4,null,7]
bstSearch( toBinaryTree([5,3,6,2,4,null,7]), 15 )--> []
'''
class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstSearch(root,key):
    iterator = root
    # iteratorがnullでない間ループします。
    while iterator is not None:
        # keyを見つけたらiteratorを返します。
        if iterator.data == key: return iterator
        # 現在のノードよりキーが小さければ左に、大きければ右に辿ります。
        if iterator.data < key: iterator = iterator.right
        else: iterator = iterator.left

    # 見つからなかった場合、iterator は nullになっています。
    return iterator
