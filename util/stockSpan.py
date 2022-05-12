'''
株式分析
medium
Steven は過去のデータを分析して、ROI を最大化しようとしているトレードアナリストです。
今各日の株価を表す整数の配列 stocks が与えられるので、
各日の i 日から何日前まで連続でその i 日の価格より高いかを配列で返す、
stockSpan という関数を作成してください。
ただし、株価の上昇には同じ日を含みます。

例えば、[1,2,5] は、[1,2,3] を返します。
1 日目は 1、2 日目は 1、2 と 2 連続、3 日目は 1, 2, 5 と 3 連続で株価が上昇しているからです。

関数の入出力例
入力のデータ型： integer[] stocks
出力のデータ型： integer[]
stockSpan([30,50,60,20,30,64,80]) --> [1,2,3,1,2,6,7]
stockSpan([24,5,67,60,24,64,23,536,345]) --> [1,1,3,1,1,3,1,8,1]
stockSpan([200,85,40,60,40,65,90]) --> [1,1,1,2,1,4,6]
stockSpan([30,45,20,100,235,300,4500,40,100]) --> [1,2,1,4,5,6,7,1,2]
stockSpan([34,640,100,234,56,34,25,200,1020,160]) --> [1,2,1,2,1,1,1,4,9,1]
'''

# スタックを使った実装
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data

    def printStack(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data)
            iterator = iterator.next

def stockSpan(stocks):
    stack = Stack()
    result = []

    for i in stocks:
        count = 1
        iterator = stack.head
        # stackが空=1日目なのでresultに1を記録。stack.push(i)をして次の株価と比較していく
        if iterator is None:
            result.append(count)
            stack.push(i)
            continue
        # iterator.data（前日の株価）の方が低い場合、繰り返す
        while iterator.data < i:
            count += 1
            iterator = iterator.next
            if iterator is None:
                break
        result.append(count)
        stack.push(i)

    return result



"""[24,5,67,60,24,64,23,536,345]
1,1,3,1,1,5,1,8,1
1,1,3,1,1,3,1,8,1]


200,85,40,60,40,65,90
1,1,1,2,1,4,6
 [1,1,1,2,1,4,6]

 [30,50,60,20,30,64,80]
1,2,3,1,2,6,7

 [30,45,20,100,235,300,4500,40,100]
1,2,1,4,5,6,7,1,2

 34,640,100,234,56,34,25,200,1020,160]
 1,2,1,2,1,1,1,4,9,1
 1,2,1,2,1,1,1,4,9,1]"""

# for 文を使った実装
def stockSpan(stocks):
    stack = []
    results = []

    for i in range(len(stocks)) :
        current = stocks[i]
        counter = 1

        while len(stack) > 0 and stocks[stack[-1]] < current: counter += results[stack.pop()]

        results.append(counter)
        stack.append(i)

    return results

if __name__ == '__main__':
    print(stockSpan([30,50,60,20,30,64,80])) # [1,2,3,1,2,6,7]
    print(stockSpan([24,5,67,60,24,64,23,536,345])) # [1,1,3,1,1,3,1,8,1]
    print(stockSpan([200,85,40,60,40,65,90])) # [1,1,1,2,1,4,6]
    print(stockSpan([30,45,20,100,235,300,4500,40,100])) # [1,2,1,4,5,6,7,1,2]
    print(stockSpan([34,640,100,234,56,34,25,200,1020,160])) # [1,2,1,2,1,1,1,4,9,1]
