# 連結リストの最初に重複する要素を返す関数

def findMergeNode(headA,headB):
    # リストの長さをそれぞれ取得します。
    lA = getLinkedListLength(headA)
    lB = getLinkedListLength(headB)

    # 二つのリストの長さを比較し、長い方を先頭から切って同じ長さにします。
    headA = getNodeAt(headA, lA-lB) if lA >= lB else headA
    headB = getNodeAt(headB, lB-lA) if lB >= lA else headB

    answer = None

    iteratorA = headA
    iteratorB = headB

    # 二つのiteratorを走査しつつ同じ値になるノードを探します。
    while iteratorA is not None:
        if iteratorA.data is not iteratorB.data: answer = None
        elif answer == None: answer = iteratorA.data

        iteratorA = iteratorA.next
        iteratorB = iteratorB.next

    # 三項演算子　answertがnullだったら-1を返します。
    return -1 if answer == None else answer


# リストの長さを取得する関数
def getLinkedListLength(head):
    iterator = head
    length = 0
    while iterator is not None:
        length += 1
        iterator = iterator.next

    return length


# インデックスのノードを取得する関数
def getNodeAt(head, position):
    iterator = head
    for i in range(position):
        if iterator == None: return None
        iterator = iterator.next

    return iterator
