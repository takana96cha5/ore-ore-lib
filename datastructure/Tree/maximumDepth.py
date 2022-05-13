'''
二分木の最大の深さ
medium
二分木 root が与えられるので、
最大の深さを返す、maximumDepth という関数を作成してください。
ここでの最大の深さとは、根ノードから最も遠い葉ノードまでの最長経路に沿ったノードの数を指します。

関数の入出力例
入力のデータ型： binaryTree<integer> root
出力のデータ型： integer
maximumDepth( toBinaryTree([0]) )--> 1
maximumDepth( toBinaryTree([0,1,null]) )--> 2
maximumDepth( toBinaryTree([0,-10,5,null,-3,null,9]) )--> 3
maximumDepth( toBinaryTree([5,2,18,-4,3]) )--> 3
maximumDepth( toBinaryTree([27,14,35,10,19,31,42]) )--> 3
maximumDepth( toBinaryTree([30,15,60,7,22,45,75,null,null,17,27]) )--> 4
maximumDepth( toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]) )--> 4
maximumDepth( toBinaryTree([50,17,76,9,23,54,null,null,14,19,null,null,72]) )--> 4
maximumDepth( toBinaryTree([16,14,10,8,7,9,3,2,4,1]) )--> 4
maximumDepth( toBinaryTree([30,15,60,7,22,45,75,1,null,17,27,null,null,null,null,-1]) )--> 5
'''

'''

二分木の最大の深さの解説と解答
左側の部分木と右側の部分木を比較して、大きい方を返すことで二分木の深さを取得できます。
ベースケースとして、root が存在しないときは 0、root に子がない時は 1 を返します。
深さをカウントするためのパラメータを扱うため、ヘルパー関数を使うこともできます。
子ノードが存在する場合、カウントを増やしながら葉ノードまで進めていきます。
左右の部分木の深さをそれぞれ変数に保存し、最後に比較して大きい方を返します。
それではコードを見てみましょう。

'''

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def maximumDepth(root):
    # rootがnullの時には0、要素が1つだけの時には1を返します。
    if root == None: return 0
    if root.left == None and root.right == None: return 1
    # ヘルパー関数を使って深さをカウントします。
    return maximumDepthHelper(root,0)


def maximumDepthHelper(root, count) :
    # rootの左の子がnullになるまで左へ進み、nullになったらcountに1を足し変数leftに代入します。
    left = maximumDepthHelper(root.left, count+1) if root.left is not None else count+1
    # rootの右の子がnullになるまで右へ進み、nullになったらcountに1を足し変数rightに代入します。
    right = maximumDepthHelper(root.right, count+1) if root.right is not None else count+1
    # 大きい方を返します。
    return max(left, right)
