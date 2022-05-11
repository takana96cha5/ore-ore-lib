class Node:
    def __init__(self, data):
        self.data = data # 要素の値
        self.next = None # 一つ先のノード

class Stack:
    def __init__(self):
        self.head = None # 先頭のノード

    # スタックの先頭にノードを追加するメソッド
    def push(self, data):
        # 現在の先頭の値を保持する
        temp = self.head
        # 先頭の値を更新する
        self.head = Node(data)
        # 保持していた先頭の値を移動させる
        self.head.next = temp

    # スタックの先頭からノードを取り除き、そのノードの値を返すメソッド
    def pop(self):
        # スタックが空の場合はヌルを返す
        if self.head == None: return None

        # スタックの先頭の値を保持する
        temp = self.head

        # スタックの先頭からノードを取り除く
        self.head = self.head.next

        # 保持していたスタックの先頭の値を返す
        return temp.data

    # スタックの先頭のノードの値を返すメソッド
    def peek(self):
        if self.head is None: return None
        return self.head.data


# 配列を逆順にソートする関数
def reverse(arr):
    s = Stack()
    ans = []
    for i in arr:
        s.push(i)

    for _ in arr:
        ans.append(s.pop())
    return ans


# リストを受け取り、単調減少している部分リストを返す関数
# リストの途中で単調増加する部分が出現したら、部分リストをリセット
def consecutiveWalk(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        # スタックの上にある要素より、arr[i]が大きい場合、スタックをリセット
        if stack.peek() < i:
            # スタックがnullになるまで繰り返す
            while stack.peek() is not None: stack.pop()
        # スタックにプッシュ(スタックは常に単調減少)
        stack.push(i)

    results = []
    # 配列の先頭から追加して、順番を調整
    while stack.peek() is not None: results.insert(0,stack.pop())
    return results


s1 = Stack()
s1.push(2)
print(s1.peek())
s1.push(4)
s1.push(3)
s1.push(1)
print(s1.pop())
print(s1.peek())

s2 = Stack()
s2.pop()
s2.push(9)
s2.push(8)
print(s2.peek())
