'''
ジム建設
hard
あなたは今ジムの建設チームのエンジニアです。
今連結したビルのような建物の中にジムを建設しようとしています。
高さを表す配列 h がヒストグラムとして与えられるので、
ヒストグラム内に描くことのできる長方形の最大面積を返す、
largestRectangle という関数を作成してください。

関数の入出力例
入力のデータ型： integer[] h
出力のデータ型： integer
largestRectangle([3,2,3]) --> 6
largestRectangle([1,2,5,2,3,4]) --> 10
largestRectangle([1,2,3,4,5]) --> 9
largestRectangle([3,4,5,8,10,2,1,3,9]) --> 16
largestRectangle([1,2,1,3,5,2,3,4]) --> 10
largestRectangle([11,11,10,10,10]) --> 50
largestRectangle([8979,4570,6436,5083,7780,3269,5400,7579,2324,2116]) --> 26152
'''
from collections import deque
def largestRectangle(h):
    stack = deque()
    max_area = 0
    for i, height in enumerate(h + [0]):
        while stack and h[stack[-1]] >= height:
            H = h[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, H * W)
        stack.append(i)
    return max_area
