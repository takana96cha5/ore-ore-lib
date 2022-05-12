class Node:
    def __init__(self, data):
        # 前後を追跡します。
        self.data = data
        self.prev = None
        self.next = None

# リストは少なくとも1つのノードを持っている必要があります。
# ヌルリストをサポートしたい場合は、それに応じてコードを追加してください。
class DoublyLinkedList:

    # 配列を双方向連結リストに変換するコンストラクタ
    def __init__(self, arr):
        # 今回は末尾を追跡します。
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return None

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            # 次のノードの前のノードをcurrent Nodeに割り当てます。
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # このcurrent Nodeは最後のnode(tail)です。
        self.tail = currentNode

    # インデックス番号からリスト内のノードにアクセスするメソッド
    def at(self, index) -> Node:
        iterator = self.head
        # 片方向リストと同じ処理(走査)
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator

    # リストの先頭から要素をpopします。O(1)
    def pop_front(self):
        self.head = self.head.next
        self.head.prev = None

    # リストの末尾から要素をpopします。O(1)
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # 与えられたノードをO(1)で削除します。
    def delete_node(self, node: Node):
        if node is self.tail: return self.pop()
        if node is self.head: return self.pop_front()

        node.prev.next = node.next
        node.next.prev = node.prev

    # 与えられたインデックス番号のノードを削除します。
    def delete_node_of_index(self, index: int):

        node = self.at(index)

        if node is self.tail: return self.pop()
        if node is self.head: return self.pop_front()

        node.prev.next = node.next
        node.next.prev = node.prev


    # リストの先頭に要素を追加します。
    def preappend(self, node: Node):
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    # リストの最後に要素を追加します。
    def append(self, node: Node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    # 与えられたインデックス番号の次に新たなノードを追加します。必要であれば末尾を更新してください。
    # 処理を紙に書いて確認しましょう。オブジェクトなので、=はメモリアドレスを指します。
    def addNextNode(self, index: int, data: int):
        node = self.at(index)
        newNode = Node(data)

        tempNode = node.next
        node.next = newNode
        newNode.next = tempNode
        newNode.prev = node
        # もし与えられたノードが末尾なら、その後ろに新しいノードが追加されるので、末尾をアップデート。
        # それ以外の場合は、tempNodeの前をnewNodeに設定。
        if node is self.tail: self.tail = newNode
        else: newNode.next.prev = newNode

    # リストを逆向きに変更するメソッド
    def reverse(self):
        reverse = self.tail
        iterator = self.tail.prev

        # 末尾から走査
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
        # リストの末尾から走査
        iterator = self.tail
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.prev
        print()

    def printList(self):
        # リストの前方から走査
        iterator = self.head
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()


if __name__ == '__main__':
    numList = DoublyLinkedList([1,2,3,4,5,6,7])

    numList.printList()

    print(numList.at(0))
