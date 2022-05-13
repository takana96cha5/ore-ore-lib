'''

前順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、
前順を表す配列を返す、preOrderTraversal という関数を作成してください。

関数の入出力例
入力のデータ型： binaryTree<integer> root
出力のデータ型： integer[]
preorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [0,-10,-3,5,9]
preorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [5,3,2,4,6,7]
preorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-2,-17,-18,-11,-4,8,3,19,25]
preorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [3,-3,-7,-10,-4,1,0,2,13,6,5,8,18,15,19]
preorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [1,-5,-9,-6,-4,0,15,10,14,17,16,19]
preorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [3,-3,-7,-10,-4,1,0,2,13,6,5,8,18,15,19]

'''

'''

前順（二分木）の解説と解答
前順走査では、
(1) データを訪問、値を配列に追加
(2) 左側のノードに移動
(3) 右側のノードに移動
という順で探索を行い、根ノードが空のノードになると終了します。

[0,-10,5,null,-3,null,9] を例に JavaScript で再帰の動きを説明します。
番号は以下を意味します。
(1) arr.push(root.data)
(2) preorderTraversalHelper(root.left, arr)
(3) preorderTraversalHelper(root.right, arr)

(1) 根ノード 0 を訪問　0 を arr に追加

(2) 左の子へ移動　0 -> -10
    (1) -10 を訪問　-10 を arr に追加
    (2) 左へ行きたいが、null なので null を返して呼び出し元へ戻る
    (3) 右の子へ移動　-10 -> -3
        (1) -3 を訪問　-3 を arr に追加
        (2) 左へ行きたいが、null なので null を返して呼び出し元へ戻る
        (3) 右へ行きたいが、null なので null を返して呼び出し元へ戻る
    呼び出し元へ戻る

(3) 右の子へ移動　0 -> 5
    (1) 5 を訪問　5 を arr に追加
    (2) 左へ行きたいが、null なので null を返して呼び出し元へ戻る
    (3) 右の子へ移動　5 -> 9
        (1) 9 を訪問　9 を arr に追加
        (2) 左へ行きたいが、null なので null を返して呼び出し元へ戻る
        (3) 右へ行きたいが、null なので null を返して呼び出し元へ戻る
    呼び出し元へ戻る
arr を返す

'''
class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorderTraversal(root):
    # ヘルパー関数を使います。
    return preorderTraversalHelper(root, [])


def preorderTraversalHelper(root, arr) :
    # ベースケース　根ノードがNoneになると終了します。
    if root == None : return None

    # 根ノードのdataをarrにpushします。
    arr.append(root.data)
    # 左側のノードへ移動します。
    preorderTraversalHelper(root.left, arr)
    # 右側のノードへ移動します。
    preorderTraversalHelper(root.right, arr)

    return arr
