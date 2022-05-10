class Task:
    def __init__(self, name):
        self.name = name
        self.next = None

# 全体の ToDoList を定義します
class TodoList:
    def __init__(self):
        # 最初は ToDoList は空です
        self.head = None

    # 各項目を出力します
    def printList(self):
        print("Printing the Todo List...")

        # イテレータを用意します
        currentNode = self.head
        while currentNode is not None:
            # 現在のノードの値を出力します
            print(currentNode.name)
            # 現在のノードを次のノードに変更します
            currentNode = currentNode.next

# リストを始めます。先頭は空です
toDoList = TodoList()

# リストの中の最初の項目に先頭を設定します
task1 = Task("Fix the alarm clock.")
toDoList.head = task1

# 残りの項目にも同じ処理を行います。次の項目を割り当てることによって、項目どうしをつなげます
task2 = Task("Pickup grandmother from the dentist.")
task1.next = task2

task3 = Task("Call the handyman to fix the home appliance.")
task2.next = task3

task4 = Task("Go to the park to jog.")
task3.next = task4

# リストを読み込みます
toDoList.printList()
