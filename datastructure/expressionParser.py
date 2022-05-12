'''
数式の解析
medium
文字列で表現された数式 expression が与えられるので、
その数式を評価し、整数の結果を返す、
expressionParser という関数を作成してください。
ただし、割り算に関しては小数点以下を切り捨てた整数値を返してください。


関数の入出力例
入力のデータ型： str
出力のデータ型： int
expressionParser("2+4*6") --> 26
expressionParser("2*3+4") --> 10
expressionParser("3-3+3") --> 3
expressionParser("2+2+2") --> 6
expressionParser("1-1-1") --> -1
expressionParser("3*3/3*3*3") --> 27
expressionParser("14/3*2") --> 8
expressionParser("12/3*4") --> 16
expressionParser("1+2+3+4+5+6+7+8+9+10") --> 55
expressionParser("1+2*5/3+6/4*2") --> 6
expressionParser("42") --> 42
expressionParser("7*3622*636*2910*183+343/2926/1026") --> 8587122934320

'''

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



class HelperFunction:
    @staticmethod
    def reverse(stack):
        newStack = Stack()
        while(stack.peek() != None ):
            newStack.push(stack.pop())
        return newStack

    @staticmethod
    def calculator(op1,op2,operatorChar):
        op1, op2 = float(op1), float(op2)
        cal = {
            '+': op1 + op2,
            '-': op1 - op2,
            '*': op1 * op2,
        }
        if operatorChar == '/':
            if op2 == 0: return op1
            else: return op1 // op2
        else: return cal[operatorChar]


def expressionParser(expression):
    # ここから書きましょう
    operator = Stack()
    op= Stack()
    priority = []
    i = 0
    # 掛け算.割り算
    while( i < len(expression)):
        if "+-*/".find(expression[i]) > -1 :
            operator.push(expression[i])
            i+=1
        else:
            n = ""
            while( i < len(expression) and "+-*/()".find(expression[i]) == -1 ):
                 if i > len(expression) :
                   break
                 n+=expression[i]
                 i+=1
            op.push(n)

            tmp = operator.pop()
            if tmp and  "*/".find(tmp) > -1 :
               op2 = op.pop()
               op1 = op.pop()
               print(op1,tmp,op2)
               if op2 != None :
                   op.push(HelperFunction.calculator(op1,op2,tmp))
            else:
                operator.push(tmp)

    operator = HelperFunction.reverse(operator)
    op = HelperFunction.reverse(op)

    while(operator.peek() != None):
        tmp = operator.pop()
        op1 = op.pop()
        op2 = op.pop()
        print(op1,tmp,op2)
        if op2 is None :
            break;
        op.push(HelperFunction.calculator(op1,op2,tmp))
    return int(op.peek())

if __name__ == '__main__':
    expressionParser()
