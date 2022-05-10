'''
Productクラス
very easy
あなたは開発チームに所属しており、請求書を管理する仕事を任されています。以下に従って、Product クラスを作成し、テストケースを出力してください。

String title	製品名
double price	製品の価格（ドル）
'''
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

product1 = Product ("shampoo", 10)
print(product1.title) # --> shampoo
print(product1.price) # --> 10

product2 = Product ("conditioner", 5)
print(product2.title) # --> conditioner
print(product2.price) # --> 5
