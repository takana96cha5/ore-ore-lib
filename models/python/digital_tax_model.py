'''
デジタル製品にかかる税金を計算するプログラム

DownloadableProduct
String title: // ダウンロード可能な製品のタイトル
String description: // ダウンロード可能な製品の説明
double price: // ダウンロード可能な製品の価格
double sizeMb: // ダウンロード可能な製品のサイズ(Mb)
String extension: // ダウンロード可能な製品の拡張子

Tax
String name: // 税金の名前
Double federalTax: // 連邦税率
Double stateTax: // 州税率
Double localTax: // 地方税率

'''

class Tax:
    def __init__(self, name, federalTax, stateTax, localTax):
        self.name = name
        self.federalTax = federalTax
        self.stateTax = stateTax
        self.localTax = localTax

class DownloadableProduct:
    def __init__(self, title, description, price, sizeMb, extension):
        self.title = title
        self.description = description
        self.price = price
        self.sizeMb = sizeMb
        self.extension = extension

    def getFinalPrice(self, Object):
        # 連邦税、州税、地方税をプロダクトに適用します
        return self.price * (1 + Object.federalTax + Object.stateTax + Object.localTax)

product1 = DownloadableProduct("A hero returns - Remastered", "A movie about a hero who saves the world.", 23.5, 13000, "mp4")
taxLasVegas = Tax("Las Vegas Taxes", 0.02,0.05,0.01)

print(product1.title + "'s price is: " + str(product1.price))
print(product1.title + "'s final price for " + taxLasVegas.name + " is: " + str(product1.getFinalPrice(taxLasVegas)))
