'''
二分探索木から削除
hard
異なる整数値で構成される二分探索木（BST）の根ノード root と整数 key が与えられるので、
BST から key を削除する bstDelete という関数を作成してください。
もし key がすでに BST 内に存在しない場合は何も削除せず、根ノードをそのまま返してください。


関数の入出力例
入力のデータ型： binaryTree<integer> root, integer key
出力のデータ型： binaryTree<integer>
bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [0,-10,9,null,-3]
bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 20 )--> [0,-10,5,null,-3,null,9]
bstDelete( toBinaryTree([1,null,2]), 1 )--> [2]
bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 3 )--> [5,4,6,2,null,null,7]
bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> [6,3,7,2,4]
bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 15 )--> [5,3,6,2,4,null,7]
bstDelete( toBinaryTree([3,2]), 3 )--> [2]
bstDelete( toBinaryTree([1]), 0 )--> [1]
bstDelete( toBinaryTree([25,15,35,null,20,30,40]), 25 )--> [30,15,35,null,20,null,40]
bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 9 )--> [0,-10,5,null,-3]
bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [0,-10,9,null,-3]
bstDelete( toBinaryTree([5,2,18,-4,3,null,null]), -4 )--> [5,2,18,null,3]
'''

# https://recursionist.io/dashboard/problems/submissions/211227

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstDelete(root,key):
        if not root:
            return
        if key < root.data:
            root.left = bstDelete(root.left, key)
        elif key > root.data:
            root.right = bstDelete(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif not root.right and root:
                root = root.right
            else:
                root.data = getNext(root) # swap
                root.right = bstDelete(root.right, root.data) # delete the original node
        return root

# return left most of root.right
def getNext(root):
    root = root.right
    while root.left:
        root = root.left
    return root.data
