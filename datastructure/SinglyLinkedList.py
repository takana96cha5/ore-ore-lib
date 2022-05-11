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
    # 配列を連結リストに変換する関数
    def __init__(self, arr):
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        currentNode = self.head;
        for i in range(1,len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next

    # 指定したインデックス番号のノードの要素を取得
    def at(self, index):
        iterator = self.head;
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None
        return iterator

    # ノードのインデックス番号を取得する関数
    def findNode(self, key):
        iterator = self.head
        index = 0
        while iterator is not None:
            if iterator.data == key: return index
            iterator = iterator.next
            index += 1
        return None

    # 要素を先頭に挿入する関数
    def preappend(self, newNode):
        newNode.next = self.head
        self.head = newNode

    # 要素を末尾に挿入する関数
    def append(self, newNode):
        iterator = self.head;
        while iterator.next is not None:
            iterator = iterator.next
        iterator.next = newNode

    # リストの先頭の要素をポップします。O(1)
    def popFront(self):
        self.head = self.head.next

    # インデックス番号の要素を削除します。
    def delete(self,index):
        if index == 0: return self.popFront()

        iterator = self.head;
        # 目的のデータの手前のインデックスまで、リストの中を反復します。
        for i in range(0, index-1):
            # もし、次のノードがなかった場合、nullを返します。インデックス範囲外を意味します。
            if iterator.next == None: return None;
            iterator = iterator.next
        # iterator（削除したい要素の1つ前）, 削除したい要素(A), その次の要素(B)
        # iteratorのポインタをAではなくBに変更します。
        iterator.next = iterator.next.next

    # 反転したリストの要素を全て出力する関数
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

    # リストの要素を全て出力する関数
    def printList(self):
        iterator = self.head;
        while iterator is not None:
            print(iterator.data, end =" ")
            iterator = iterator.next
        print("")

numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

numList.printList()
numList.reverseList()
numList.printList()
numList.reverseList()
numList.printList()
