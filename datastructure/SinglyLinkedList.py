'''片方向連結リスト'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def addNextNode(self, newNode):
        tempNode = self.next
        self.next = newNode
        newNode.next = tempNode

class SinglyLinkedList:
    # 配列を連結リストに変換するコンストラクタ
    def __init__(self, arr):
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        # 連結リストにほかのノードを追加します。
        # nodeはオブジェクトなので、=は値ではなく、メモリアドレスを指している点に注意してください。
        currentNode = self.head
        for i in range(1,len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next

    # 指定したインデックス番号のノードの要素を取得するメソッド
    def at(self, index):
        iterator = self.head

        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None
        return iterator

    # ノードのインデックス番号を取得するメソッド
    def findNode(self, key):
        iterator = self.head
        index = 0
        while iterator is not None:
            if iterator.data == key: return index
            iterator = iterator.next
            index += 1
        return None


    # リストの中の最小値のインデックスを返すメソッド
    def findMinNum(self):
        # head を iterator に代入します。
        iterator = self.head
        # 暫定の最小値として float('inf') を入れておきます。
        minValue = float('inf')
        # 最小値を更新したら index も更新します。
        index = 0
        # リストのインデックスを追いかける変数
        i = 0

        # iteratorがnullでない間リストを走査します。
        while iterator != None :
            # 暫定の最小値よりもiteratorの値が小さかったら更新します。
            if minValue >= iterator.data :
                minValue = iterator.data
                # その時の i を index に保存します。
                index = i
            # 次のノードへ進めます。
            iterator = iterator.next
            # iをインクリメントします。
            i += 1

        return index


    # 要素を先頭に挿入するメソッド
    def preappend(self, data):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        newNode.next = self.head
        self.head = node

    # 要素を末尾に挿入するメソッド
    def append(self, data):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        iterator.next = node

    # 特定の位置に挿入するメソッド
    def insertAtPosition(self, position, data):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        # iterator に head を入れます。
        iterator = self.head
        # 与えられた位置の1つ前までリストを走査します。
        for i in range(position) :
            # もしiterator.next が null だったら head を返します。
            if iterator.next == None: return None
            # iterator を next へ進めます。
            iterator = iterator.next

        # tempに現在のiterator.nextを入れます。
        temp = iterator.next
        # iterator.next を新しいノードにします。
        iterator.next = node
        # 新しいノードの next を temp にします。
        node.next = temp

    # リストの先頭の要素をポップするメソッド O(1)
    def popFront(self):
        self.head = self.head.next

    # リストの末尾の要素をポップするメソッド
    def deleteTail(self):
        iterator = self.head
        while iterator.next is not None:
            prev = iterator
            iterator = iterator.next
        prev.next = None

    # インデックス番号の要素を削除するメソッド
    def delete(self,index):
        if index == 0: return self.popFront()

        iterator = self.head
        # 目的のデータの手前のインデックスまで、リストの中を反復します。
        for i in range(0, index-1):
            # もし、次のノードがなかった場合、nullを返します。インデックス範囲外を意味します。
            if iterator.next == None: return None
            iterator = iterator.next
        # iterator（削除したい要素の1つ前）, 削除したい要素(A), その次の要素(B)
        # iteratorのポインタをAではなくBに変更します。
        iterator.next = iterator.next.next

    # リストの要素の順序を反転するメソッド
    def reverseList(self):
        if self.head is None or self.head.next is None: return

        # オブジェクトなので、=は実際の値を格納しているわけではなく、メモリアドレスを指している点に十分注意ください。
        # A -> B -> C を、C -> B -> Aに変更する場合は、向きに少し混乱するのでゆっくり解読しましょう。
        reverse = self.head
        self.head = self.head.next
        reverse.next = None
        while self.head is not None:
            # =はメモリアドレスを指します。紙に書いてロジックを確認しましょう。
            temp = self.head
            self.head = self.head.next
            temp.next = reverse
            reverse = temp
        # 処理が終わったら、headのnextを反転したリストを含むtempHeadに割り当てましょう。
        self.head = reverse

    # リストの要素を全てプリントするメソッド
    def printList(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end =" ")
            iterator = iterator.next
        print("")

    # 連結リストの長さを返すメソッド
    def linkedListLength(self):
        iterator = self.head
        cnt = 0
        while iterator is not None:
            iterator = iterator.next
            cnt += 1
        return cnt

    # 連結リストの末尾の値を返すメソッド
    def linkedListLastValue(self):
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        return iterator.data


numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

numList.printList()
numList.reverseList()
numList.printList()
numList.reverseList()
numList.printList()
numList.deleteTail()
numList.printList()
print(numList.findMinNum())
