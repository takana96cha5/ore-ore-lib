class Node:
    def __init__(self, data):
        # 前後を追跡します。
        self.data = data
        self.prev = None
        self.next = None

# リストは少なくとも1つのノードを持っている必要があります。
# ヌルリストをサポートしたい場合は、それに応じてコードを追加してください。
class DoublyLinkedList:
    def __init__(self, arr):
        # 今回は末尾を追跡します。
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            # 次のノードの前のノードをcurrent Nodeに割り当てます。
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # このcurrent Nodeは最後のnodeです。
        self.tail = currentNode

    # インデックス番号からリスト内の要素にアクセス
    def at(self, index):
        iterator = self.head
        # 片方向リストと同じ処理
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator

    # リストの先頭から要素をpopします。O(1)
    def popFront(self):
        self.head = self.head.next
        self.head.prev = None

    # リストの末尾から要素をpopします。O(1)
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # 与えられたノードをO(1)で削除します。
    def deleteNode(self, node):
        if node is self.tail: return self.pop()
        if node is self.head: return self.popFront()

        node.prev.next = node.next
        node.next.prev = node.prev

    # リストの先頭に要素を追加します。
    def preappend(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode

    # リストの最後に要素を追加します。
    def append(self, newNode):
        self.tail.next = newNode
        newNode.next = None
        newNode.prev = self.tail
        self.tail = newNode

    # 与えられたノードの次に追加します。必要であれば末尾を更新してください。
    # 処理を紙に書いて確認しましょう。オブジェクトなので、=はメモリアドレスを指します。
    def addNextNode(self, node, newNode):
        tempNode = node.next
        node.next = newNode
        newNode.next = tempNode
        newNode.prev = node
        # もし与えられたノードが末尾なら、その後ろに新しいノードが追加されるので、末尾をアップデートしてください。
        # それ以外の場合は、tempNodeの前をnewNodeに設定してください。
        if node is self.tail: self.tail = newNode
        else: tempNode.prev = newNode

    # リストを逆向きに変更する関数
    def reverse(self):
        reverse = self.tail
        iterator = self.tail.prev

        currentNode = reverse
        while iterator is not None:
            currentNode.next = iterator

            iterator = iterator.prev
            if iterator is not None: iterator.next = None

            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        self.tail = currentNode
        self.head = reverse
        self.head.prev = None

    # 逆側から出力する
    def printInReverse(self):
        iterator = self.tail
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.prev
        print()

    def printList(self):
        iterator = self.head
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

numList = DoublyLinkedList([1,2,3,4,5,6,7])

print(numList.head.data)
print(numList.head.next.data)
print(numList.head.next.prev.data)
print(numList.tail.data)
print(numList.tail.prev.data)
print(numList.tail.prev.prev.data)
