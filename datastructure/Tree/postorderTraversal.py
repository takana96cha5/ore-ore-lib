'''
後順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、
後順を表す整数の配列を返す、postorderTraversal という関数を作成してください。


関数の入出力例
入力のデータ型： binaryTree<integer> root
出力のデータ型： integer[]
postorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [-3,-10,9,5,0]
postorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [2,4,3,7,6,5]
postorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-18,-4,-11,-17,3,25,19,8,-2]
postorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-4,-7,0,2,1,-3,5,8,6,15,19,18,13,3]
postorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [-6,-9,0,-4,-5,14,10,16,19,17,15,1]
postorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-4,-7,0,2,1,-3,5,8,6,15,19,18,13,3]
'''

'''

後順（二分木）の解説と解答

後順走査では、
(1) 左側のノードに移動
(2) 右側のノードに移動
(3) データを訪問、値を配列に追加
という順で探索を行い、根ノードが空のノードになると終了します。

[0,-10,5,null,-3,null,9] を例に JavaScript で再帰の動きを説明します。

番号は以下を意味します。
(1) postorderTraversalHelper(root.left, arr)
(2) postorderTraversalHelper(root.right, arr)
(3) arr.push(root.data)

(1) 左の子へ移動　0 -> -10
    (1) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
    (2) 右の子へ移動 -10 -> -3
        (1) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
        (2) 右へ行きたいけど null なので null を返して呼び出し元へ戻る
        (3) -3 を arr に追加
        呼び出し元へ戻る
    (3) -10 を arr に追加
    呼び出し元へ戻る

(2) 右の子へ移動　0 -> 5
    (1) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
    (2) 右の子へ移動　5 -> 9
        (1) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
        (2) 右へ行きたいけど null なので null を返して呼び出し元へ戻る
        (3) 9 を arr に追加
        呼び出し元へ戻る
    (3) 5 を arr に追加
    呼び出し元へ戻る

(3) 0 を arr に追加
arr を返す

'''

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def postorderTraversal(root):
    # ヘルパー関数を使います。
    return postorderTraversalHelper(root, [])


def postorderTraversalHelper(root, arr) :
    # ベースケース　根ノードがNoneになると終了します。
    if root == None: return None

    # 左側のノードへ移動します。
    postorderTraversalHelper(root.left, arr)
    # 右側のノードへ移動します。
    postorderTraversalHelper(root.right, arr)
    # 根ノードのdataをarrにpushします。
    arr.append(root.data)

    return arr
