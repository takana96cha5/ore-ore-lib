'''
あなたは開発チームに所属しており、企業用向けのクラウドシステムを構築するタスクを与えられました。このソフトウェアの一部には、ユーザーがファイルを保存したり、読み書きできる機能が含まれています。ファイルを共有することもできるので、ユーザーは上書きがないように自分のファイルをロックする機能もついています。以下に従って、Files クラスを作成し、テストケースを出力してください。

String fileName	ファイル名
String fileExtension	ファイルの拡張子。.word、.png、.mp4、.pdf でない場合は、.txt に設定されます。
String content	ファイルに含まれるコンテンツ
String parentFolder	ファイルが置かれているフォルダの名前
String getLifetimeBandwidthSize()	サービス中に使われるファイルの最大容量を返します。content に含まれる文字（空白文字も含む）につき、25MB として計算してください。例えば、40 文字含まれている場合、40 * 25MB = 1,000MB = 1GBになります。単位の最大はG（ギガ）とします。1000MB　以上は単位を GB に変換してください
String prependContent(String data)	ファイルの content の先頭にデータ文字列を追加し、新しいcontentを返します。
String addContent(String data, int position)	ファイルの content の指定した位置（インデックス）にデータ文字列を追加し、新しい content を返します。
String showFileLocation()	親ファイル > ファイル名.拡張子という形で返します。
'''

# テストケースを指定するために関数の返し方？を print -> return に変更してみた

class Files:
    def __init__(self, fileName, fileExtension, content, parentFolder):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.parentFolder = parentFolder

    def getLifetimeBandwidthSize(self):
        # MBの容量を計算
        mbSize = len(self.content) * 25

        if mbSize >= 1000:
            front = mbSize // 1000
            back = mbSize % 1000
            return str(front) + "." + str(back) + "GB"
        else:
            return str(mbSize) + "MB"

    # ファイルの content の先頭にデータ文字列を追加し、新しいcontentを返す
    def prependContent(self, head):
        self.head = head
        # addContent()を利用する
        return self.addContent(head, 0)

    # ファイルの content の指定した位置（インデックス）にデータ文字列を追加し、新しい content を返す
    def addContent(self, addData, position):
        self.addData = addData
        self.position = position

        self.content = self.content[:self.position] + self.addData + self.content[self.position:]
        return self.content

    # 親ファイル > ファイル名.拡張子という形で返す
    def showFileLocation(self):
        extentionList = [".word", ".png", ".mp4", ".pdf"]

        if self.fileExtension in extentionList:
            return self.parentFolder + " > " + self.fileName  + self.fileExtension
        else:
            return self.parentFolder + " > " + self.fileName + ".txt"


assignment = Files("assignment", ".word", "ABCDEFGH", "homework")
print(assignment.getLifetimeBandwidthSize())
print(assignment.prependContent("MMM"))
print(assignment.addContent("hello world", 5))
print(assignment.showFileLocation())

blade = Files("blade", ".php", "bg-primary text-white m-0 p-0 d-flex justify-content-center", "view")
print(blade.getLifetimeBandwidthSize())
print(blade.addContent("font-weight-bold ", 11)) # 10 -> 11 change
print(blade.showFileLocation())
