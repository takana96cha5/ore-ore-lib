'''
括弧チェック
Walker は出版社で文章チェックの仕事をしています。
() や {}、[] で括られている文章をチェックしているのですが、
正しく使われているか見なければいけません。
文字列 parentheses が与えられるので、
それが有効かどうか判定する、isParenthesesValid という関数を定義してください。

与えられる文字列が有効の条件は以下の通りです。
- 左カッコが同じ種類の右カッコで閉じられてる
- 左カッコが右カッコによって正しい順で閉じられている

関数の入出力例
入力のデータ型： string parentheses
出力のデータ型： bool
isParenthesesValid("{}") --> true
isParenthesesValid("[{}]") --> true
isParenthesesValid("[{(]") --> false
isParenthesesValid("(){}[]") --> true
isParenthesesValid("((()(())))") --> true
isParenthesesValid("[{(}])") --> false
isParenthesesValid("]][}{({()){}(") --> false
isParenthesesValid("{(([])[])[]}[]") --> true
isParenthesesValid("{(([])[])[]]}") --> false
isParenthesesValid("{{[[(())]]}}") --> true
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

def isParenthesesValid(parentheses):
    # stack.peek() is Noneの時、is_balancedがTrueならTrueと考える

    stack = Stack()
    is_balanced = True
    opening = "([{"
    closing = ")]}"

    for char in parentheses:
        # 始まりの括弧ならスタックに積む
        if char in opening:
            stack.push(char)
        # 閉じ括弧の場合
        elif char in closing:
            # スタックに何もなければ対応する始まり括弧がないことになるのでFalse
            if stack.peek() is None:
                is_balanced = False
                break
            # スタックに何か入っていれば対応する始まり括弧なのか確認する
            else:
                top = stack.pop()
                # is_match()でFalseだったらis_balancedをFalseにする
                if not is_match(top, char):
                    is_balanced = False
                    break

    if stack.peek() is None and is_balanced:
        return True
    else:
        return False

# 始まりの括弧と終わりの括弧が対応するか確認する関数
def is_match(parenth1, parenth2):
    if parenth1 == "(" and parenth2 == ")":
        return True
    elif parenth1 == "[" and parenth2 == "]":
        return True
    elif parenth1 == "{" and parenth2 == "}":
        return True
    else:
        return False

# 連想配列を使った実装
def isParenthesesValid(parentheses):

    charStack = []
    # 正しい括弧のペアでハッシュマップを作成する
    pairs = {
        "}":"{",
        ")":"(",
        "]":"[",
    }

    for i in range(len(parentheses)):
        currChar = parentheses[i]

        if (len(charStack) > 0) and (currChar in pairs) and (charStack[-1] == pairs[currChar]):
            charStack.pop()
        else:
            charStack.append(currChar)

    return len(charStack) == 0
