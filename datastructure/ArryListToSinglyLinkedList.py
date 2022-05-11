# ノード
class SinglyLinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# 片方向リスト
class SinglyLinkedList:
    def __init__(self, node):
        # 先頭を定義します。
        self.head = node

def ArryListToSinglyLinkedList(arr:int) -> SinglyLinkedList:
    # 配列から連結リストを作成します。
    numList = SinglyLinkedList(SinglyLinkedListNode(arr[0]))

    # 連結リストにほかのノードを追加します。
    # nodeはオブジェクトなので、=は値ではなく、メモリアドレスを指している点に注意してください。
    currentNode = numList.head
    for i in range(1,len(arr)):
        currentNode.next = SinglyLinkedListNode(arr[i])
        currentNode = currentNode.next
    return numList

#     '''連結リストをプリント'''
#     result = ""
#     # 連結リストを反復します。
#     # 反復によって、現在のノードは次のノードになります。この処理を最後のノードまで繰り返します。
#     currentNode = numList.head
#     while currentNode is not None:
#         # 現在のノードを出力します。
#         result += str(currentNode.data) + " -> "
#         currentNode = currentNode.next
#     print(result + "END")

# '''TEST'''
# ArryListToSinglyLinkedList([3,2,1,5,6,4])
# ''' --> 3➡2➡1➡5➡6➡4➡END'''
# ArryListToSinglyLinkedList([7,8,2,3,1,7,8,11,4,3,2])
# '''--> 7➡8➡2➡3➡1➡7➡8➡11➡4➡3➡2➡END'''
# ArryListToSinglyLinkedList([34,35,64,34,10,2,14,5,353,23,35,63,23])
# '''--> 34➡35➡64➡34➡10➡2➡14➡5➡353➡23➡35➡63➡23➡END'''
# ArryListToSinglyLinkedList([1])
# '''  --> 1➡END'''
