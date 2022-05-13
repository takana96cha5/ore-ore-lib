'''

逆間順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、
逆間順を表す配列を返す、reverseInorderTraversal という関数を作成してください。


関数の入出力例
入力のデータ型： binaryTree<integer> root
出力のデータ型： integer[]
reverseInorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [9,5,0,-3,-10]
reverseInorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [7,6,5,4,3,2]
reverseInorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [25,19,8,3,-2,-4,-11,-17,-18]
reverseInorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [19,18,15,13,8,6,5,3,2,1,0,-3,-4,-7,-10]
reverseInorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [19,17,16,15,14,10,1,0,-4,-5,-6,-9]
reverseInorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [19,18,15,13,8,6,5,3,2,1,0,-3,-4,-7,-10]

'''

'''

逆間順（二分木）の解説と解答

逆間順走査では、
(1) 右側のノードに移動
(2) データを訪問、値を配列に追加
(3) 左側のノードに移動
という順で探索を行い、根ノードが空のノードになると終了します。

[0,-10,5,null,-3,null,9] を例に JavaScript で再帰の動きを説明します。
番号は以下を意味します。
(1) reverseInorderTraversalHelper(root.right, arr)
(2) arr.push(root.data)
(3) reverseInorderTraversalHelper(root.left, arr)

(1) 右の子へ移動　0 -> 5
    (1) 右の子へ移動　5 -> 9
        (1) 右へ行きたいけど null なので null を返して呼び出し元へ戻る
        (2) 9 を arr に追加
        (3) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
        呼び出し元へ戻る
    (2) 5 を arr に追加
    (3) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
    呼び出し元へ戻る

(2) 0 を arr に追加

(3) 左の子へ移動　0 -> -10
    (1) 右の子へ移動 -10 -> -3
        (1) 右へ行きたいけど null なので null を返して呼び出し元へ戻る
        (2) -3 を arr に追加
        (3) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
        呼び出し元へ戻る
    (2) -10 を arr に追加
    (3) 左へ行きたいけど null なので null を返して呼び出し元へ戻る
    呼び出し元へ戻る
arr を返す

'''

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def reverseInorderTraversal(root):
    # ヘルパー関数を使います。
    return reverseInorderTraversalHelper(root, [])


def reverseInorderTraversalHelper(root, arr) :
    # ベースケース　根ノードがNoneになると終了します。
    if root == None: return None

    # 右側のノードへ移動します。
    reverseInorderTraversalHelper(root.right, arr)
    # 根ノードのdataをarrにpushします。
    arr.append(root.data)
    # 左側のノードへ移動します。
    reverseInorderTraversalHelper(root.left, arr)

    return arr

