'''
階層走査
medium
二分木 root が与えられるので、
階層ごとに左->右で配列で返す、levelOrderTraversal という関数を作成してください。

関数の入出力例
入力のデータ型： binaryTree<integer> root
出力のデータ型： integer[]
levelOrderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [0,-10,5,null,-3,null,9]
levelOrderTraversal( toBinaryTree([5,2,18,-4,3]) )--> [5,2,18,-4,3]
levelOrderTraversal( toBinaryTree([27,14,35,10,19,31,42]) )--> [27,14,35,10,19,31,42]
levelOrderTraversal( toBinaryTree([30,15,60,7,22,45,75,null,null,17,27]) )--> [30,15,60,7,22,45,75,null,null,17,27]
levelOrderTraversal( toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]) )--> [90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]
levelOrderTraversal( toBinaryTree([50,17,76,9,23,54,null,null,14,19,null,null,72]) )--> [50,17,76,9,23,54,null,null,14,19,null,null,72]
levelOrderTraversal( toBinaryTree([16,14,10,8,7,9,3,2,4,1]) )--> [16,14,10,8,7,9,3,2,4,1]
'''

'''
https://www.youtube.com/watch?v=y2JBNRTWp4c&t=20s
'''

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    queue = [root]
    results = []
    while not len(queue) == 0:
        curr = queue.pop(0)
        if curr == None:
            results.append('null')

        else:
            queue.append(curr.left)
            queue.append(curr.right)
            results.append(curr.data)

    while len(results) > 0 and results[len(results)-1] == 'null': results.pop()

    return results
