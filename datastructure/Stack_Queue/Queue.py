class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# キュー（FIFO） 末尾から入って先頭から出る
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # キューの先頭の Node の値を返します。
    def peek_front(self):
        if self.head == None: return None
        return self.head.data
    # キューの末尾の Node の値を返します。
    def peek_back(self):
        if self.tail == None: return self.peek_front()
        return self.tail.data

    # キューの末尾に Node を挿入します。
    def enqueue(self,data):
        if self.head == None:
            self.head = Node(data)
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # キューの先頭の Node を取り除き、その値を返します。
    def dequeue(self):
        if self.head == None: return None
        temp = self.head

        if self.head.next == None:
            self.head = None
            self.tail = None
        else: self.head = self.head.next

        return temp.data

if __name__ == '__main__':

    q = Queue()
    print(q.peekFront())
    print(q.peekBack())

    q.enqueue(4)
    print(q.peekFront())
    print(q.peekBack())

    q.enqueue(50);
    print(q.peekFront())
    print(q.peekBack())

    q.enqueue(64)
    print(q.peekFront())
    print(q.peekBack())

    print("dequeued :" + str(q.dequeue()))
    print(q.peek_front())
    print(q.peek_back())
