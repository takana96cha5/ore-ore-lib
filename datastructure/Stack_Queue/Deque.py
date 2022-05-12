class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 両端キュー 先頭と末尾の両方からから出入りができる
class Deque:
    def __init__(self):
        self.head = None # 先頭のノード
        self.tail = None # 末尾のノード

    # キューの先頭の Node の値を返すメソッド
    def peek_front(self):
        if self.head == None: return None
        return self.head.data

    # キューの末尾の Node の値を返すメソッド
    def peek_back(self):
        if self.tail == None: return None
        return self.tail.data

    # リストの先頭に要素を挿入するメソッド
    def enqueue_front(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    # リストの末尾に要素を挿入するメソッド
    def enqueue_back(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # リストの先頭にある要素を削除して返すメソッド
    def dequeue_front(self):
        if self.head == None: return None

        temp = self.head
        self.head = self.head.next
        if self.head is not None: self.head.prev = None
        else: self.tail = None
        return temp.data

    # リストの末尾にある要素を削除して返すメソッド
    def dequeue_back(self):
        if self.tail == None: return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is not None: self.tail.next = None
        else: self.head = None
        return temp.data

# 整数で構成される配列が与えられるので、両端キューを用いて最大値を返す関数
def get_max(arr):
    deque = Deque()
    # 最初の要素を両端キューの最初に追加します。
    deque.enqueue_front(arr[0])

    # 最大値は両端キューの先頭へ、その他の値は末尾へ向かいます。
    for i in arr[1:]:
        if i > deque.peek_front(): deque.enqueue_front(i)
        else: deque.enqueue_back(i)

    return deque.peek_front()

# スライディングウィンドウ
# サイズ k のウィンドウを配列の中で 1 つずつ右側にずらし、ウィンドウの中での最大値を求める
def get_max_windows(arr, k):
    if len(arr) < k: return []

    deque = Deque()
    results = []
    # dequeを初期化する
    for i, num in enumerate(arr[:k]): # 頭からk個の要素を取り出す
        # 新しい値と既存の値を比較して、新しい値以下は全て削除するので、
        # dequeの末尾は新しい値より大きい値になります。
        # dequeの先頭は最大値です。(新しい値より大きいので削除されないから。)
        while deque.peek_back() is not None and arr[deque.peek_back()] <= num:
            deque.dequeue_back()
        deque.enqueue_back(i)

    for i, num in enumerate(arr[k:], k): # enumerate(リスト,開始インデックス数)
        # dequeの先頭は最大値
        results.append(arr[deque.peek_front()])
        # ウィンドウ外にある要素は取り除く
        while deque.peek_back() is not None and deque.peek_front() <= i-k:
            deque.dequeue_front()
        # 現在の値とそれより小さい全てのdequeの値をチェック
        while deque.peek_back() is not None and arr[deque.peek_back()] <= num:
            deque.dequeue_back()

        deque.enqueue_back(i)

    # 最後の最大値を追加
    results.append(arr[deque.peek_front()])

    return results

# スライディングウィンドウ
# サイズ k のウィンドウを配列の中で 1 つずつ右側にずらし、ウィンドウの中での最小値を求める
def get_min_windows(intArr,k):
    if len(intArr) < k:
        return []

    deque = Deque()
    results = []
    # dequeを初期化（intArrの頭からk個の要素を取り出す）
    for i, num in enumerate(intArr[:k]):
        while (deque.peek_back() is not None) and (intArr[deque.peek_back()] > num):
            deque.dequeue_back()
        deque.enqueue_back(i)

    for i, num in enumerate(intArr[k:], k): # enumerate(リスト,開始インデックス数)
        # dequeの先頭は最小値
        results.append(intArr[deque.peek_front()])

        if i - deque.peek_front() >= k:
            deque.dequeue_front()

        # 現在の値とそれより大きい全てのdequeの値をチェック
        while deque.peek_back() is not None and intArr[deque.peek_back()] > num:
            deque.dequeue_back()

        deque.enqueue_back(i)

    # 最後の最大値を追加
    results.append(intArr[deque.peek_front()])

    return results


if __name__ == '__main__':
    print(get_max([34,35,64,34,10,2,14,5,353,23,35,63,23]))  # 353
    print(get_max_windows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4))
    print(get_min_windows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4))
