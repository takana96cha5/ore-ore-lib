'''片方向連結リスト'''

# ノード
class Node:
    def __init__(self,data: int):
        self.data = data
        self.next = None

    # 新しいノードを現在のノードの次のポインタに追加するメソッド
    def add_next_node(self, newNode):
        # ノードの次のポインタを一時変数に格納
        tempNode = self.next
        # 追加するノードポインタをノードの次のポインタに設定
        self.next = newNode
        # 一時変数に格納していたノードの次のポインタを追加するノードの次のポインタに設定
        newNode.next = tempNode
        '''イメージ
        # {selfNode} -> {NextNode} ===NewNodeを追加==> {selfNode} -> {NewNode} -> {NextNode}
        '''

# 片方向連結リスト
class SinglyLinkedList:
    # 配列を連結リストに変換するコンストラクタ
    def __init__(self, arr: any):
        # 配列の0番目の要素を連結リストのヘッドに追加し、配列が空の場合はデータがヌルのノードを追加します。
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        # 連結リストにほかのノードを追加します。
        # nodeはオブジェクトなので、=は値ではなく、メモリアドレスを指している点に注意してください。
        # ヘッドを現在のノードに設定します。
        currentNode = self.head
        # 配列の要素を1番から最後まで反復します。
        for i in range(1,len(arr)):
            # 現在のノードの次のポインタに取り出した要素を設定します
            currentNode.next = Node(arr[i])
            # 現在のノードを次のノードに更新します
            currentNode = currentNode.next

    # 指定したインデックス番号のノードを取得するメソッド
    def at(self, index: int) -> Node:
        # イテレータにノードのheadを設定します
        iterator = self.head
        # インデックス番号の数だけイテレーターを更新し連結リストを走査します
        for _ in range(0, index):
            iterator = iterator.next
            # もしインデックス番号にたどり着かなかったらNoneを返します
            if iterator == None: return None
        # インデックス番号のノードを返します
        return iterator

    # ノードのインデックス番号を取得するメソッド
    def find_index_of_data(self, key: int) -> int:
        iterator = self.head
        index = 0
        while iterator is not None:
            if iterator.data == key: return index
            iterator = iterator.next
            index += 1
        return None


    # リストの中の最小値のインデックスを返すメソッド
    def find_index_of_min_num(self) -> int:
        # head を iterator に代入します。
        iterator = self.head
        # 暫定の最小値としてどんな値よりも大きな無限である float('inf') を入れておきます。
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


    # 新しいノードを連結リストの先頭に挿入するメソッド
    def preappend(self, data: int):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        # 新しいノードを挿入します
        node.next = self.head
        self.head = node

    # ノードを末尾に挿入するメソッド
    def append(self, data: int):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        # 連結リストの末尾まで走査してノードを追加します
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        iterator.next = node

    # 特定の位置に挿入するメソッド
    def insert_at_position(self, position: int, data: int):

        # deta を入れた新しいノードを作ります。
        node = Node(data)

        # iterator に head を入れます。
        iterator = self.head
        # 与えられた位置の1つ前までリストを走査します。
        for _ in range(position) :
            # もし特定の位置が存在していなかったら null を返します。
            if iterator.next == None: return None
            # iterator を next へ進めます。
            iterator = iterator.next

        # 新しいノードを挿入します
        temp = iterator.next
        iterator.next = node
        node.next = temp

    # ソート済みの連結リストの正しい位置に挿入するメソッド
    def insert_in_sorted_list(self, data: int):
        # 先頭に挿入する場合とそれ以外の場合で場合分けが必要だが、
        # ダミーのノードを先頭に追加することにより場合分けを回避。
        # ダミーのノードを作り、head の前に挿入しておきます。
        dummyNode = Node(None)
        dummyNode.next = self.head
        # iterator にダミーノードを入れます。
        iterator = dummyNode
        # 挿入すべき位置までリストを走査します。
        while not(iterator.next == None) and (iterator.next.data < data) :
            iterator = iterator.next

        # 新しいノードを作ります。
        node = Node(data)

        # 新しいノードを挿入します
        temp = iterator.next
        iterator.next = node
        node.next = temp

    # リストの先頭の要素をポップするメソッド O(1)
    def pop_front(self):
        self.head = self.head.next

    # リストの末尾の要素をポップするメソッド
    def delete_tail(self):

        iterator = self.head
        while iterator.next is not None:
            prev = iterator
            iterator = iterator.next
        prev.next = None

    # インデックス番号の要素を削除するメソッド
    def delete(self,index: int):
        if index == 0: return self.pop_front()

        iterator = self.head
        # 目的のデータの手前のインデックスまで、リストの中を走査します。
        for _ in range(0, index-1):
            # もし、次のノードがなかった場合、nullを返します。インデックス範囲外を意味します。
            if iterator.next == None: return None
            iterator = iterator.next
        # iterator（削除したい要素の1つ前）, 削除したい要素(A), その次の要素(B)
        # iteratorのポインタをAではなくBに変更します。
        iterator.next = iterator.next.next

    # リストの要素の順序を反転するメソッド
    def reverse_list(self):
        # 空の配列, もしくは要素が一つだけの配列の場合は反転させることなく終了します
        if self.head is None or self.head.next is None: return None

        # 単純に考えれば、空の連結リストを用意して値を先頭から挿入していくことで、
        # 逆順の連結リストを取得できます
        # 連結リストの先頭への挿入はO(1) なので時間計算量はO(N)ですが、
        # コピー先の分で空間計算量もO(N) になります。
        # 現在のノード、前のノード、次のノードの3つを把握し、
        # 現在のノードから前のノードへポインタを付け替える操作を繰り返し行うことで、
        # この操作の空間計算量をO(1)にすることができます。
        # オブジェクトなので、=は実際の値を格納しているわけではなく、
        # メモリアドレスを指している点に十分注意ください。
        # A -> B -> C を、C -> B -> Aに変更する場合は、向きに少し混乱するのでゆっくり解読しましょう。
        # head を reverse に格納する
        reverse = self.head
        # head の位置をずらす
        self.head = self.head.next
        # reverse の次のポインタは None
        reverse.next = None
        # リストを走査する
        while self.head is not None:
            # =はメモリアドレスを指します。
            # head を一時退避
            temp = self.head
            # head を更新
            self.head = self.head.next
            # reverse を 更新前の head.next にする
            temp.next = reverse
            # reverse を更新前の head にする
            reverse = temp
            print(f"reverse->reverse.next:{reverse.data}->{reverse.next.data}")
        # 一番最後に head を変更
        self.head = reverse
        print(f"head->haed.next:{self.head.data}->{self.head.next.data}")

    # リストの要素を全てプリントするメソッド
    def print_list(self):
        # リストを走査してプリントしていく
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end =" ")
            iterator = iterator.next
        print("")

    # 連結リストの長さを返すメソッド
    def linked_list_length(self) -> int:
        # リストを走査してカウントしていく
        iterator = self.head
        cnt = 0
        while iterator is not None:
            iterator = iterator.next
            cnt += 1
        return cnt

    # 連結リストの末尾の値を返すメソッド
    def linked_list_last_value(self) -> int:
        # リストを走査して、
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        return iterator.data

    # # 連結リストの長さを n 倍にするメソッド
    # def reproduceByN(self,n):
    #     empty_Node = SinglyLinkedListNode(None)
    #     temp_Node = empty_Node

    #     for _ in range(n):
    #         iterator = self.head
    #         while iterator:
    #             empty_Node.next = SinglyLinkedListNode(iterator.data)
    #             empty_Node = empty_Node.next
    #             iterator = iterator.next
    #     return temp_Node.next

if __name__ == '__main__':
    # numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
    numList = SinglyLinkedList([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    # print("--------")
    # numList.print_list()

    # print(numList.at(3).next.data)
    # print(numList.find_index_of_data(86))

    # print("--------")

    # sortedList = SinglyLinkedList([2,10,34,45,67,356])
    # sortedList.print_list()
    # sortedList.insert_in_sorted_list(16)
    # sortedList.print_list()
    # sortedList.delete_tail()
    # sortedList.print_list()
    numList.reverse_list()
