'''
Invoice 請求書作成モデル

String title	製品名
double price	製品の価格（ドル）
Product product	製品オブジェクト
int quantity	購入する製品の数
InvoiceItem next	請求書の次の項目
double getTotalPrice()	購入する数量に基づいて、製品の合計価格を計算します。
String invoiceNumber	請求書番号
InvoiceItem invoiceItemHead	購入したアイテムのリストの開始（連結リストの先頭）を表す InvoiceItem
double amountDue(bool taxes)	請求書の支払総額を計算します。InvoiceItemHead から始まるすべてのリスト項目を反復処理し、数量も考慮して計算する必要があります。入力が true に設定されている場合は、合計金額に、消費税分の 10% を加算してください。
String invoiceDate: // 請求書が作成された日付
String company: // 会社名
String companyAddress: // 会社の住所
String billToName: // 請求書先の名前
String billToAddress: // 請求書先の住所

void printBuyingItems():
// 請求書の全項目と数量を出力します。以下のようにそれぞれのアイテムを出力してください。
// item : shampoo, price :10, quantity : 7

void printInvoice():
// 請求書の全内容を出力します。以下のように出力してください。
/*
Invoice
No. : UC1234567890
INVOICE DATE : 2020/05/06
SHIP TO : Recursion
ADDRESS : Los Angeles
BILL TO : Steven
ADDRESS : Dallas
shampoo($10)--- 7 pcs. --- AMOUNT: 70
conditioner($5)--- 9 pcs. --- AMOUNT: 45
tooth brush($3)--- 10 pcs. --- AMOUNT: 30
SUBTOTAL : 145
TAX : 14.5
TOTAL : 159.5
*/

'''
class Invoice :
    def __init__(self,invoiceNumber, invoiceDate, company, companyAddress, billToName, billToAddress, invoiceItemHeadNode) :
        self.invoiceNumber = invoiceNumber
        self.invoiceDate = invoiceDate
        self.company = company
        self.companyAddress = companyAddress
        self.billToName = billToName
        self.billToAddress = billToAddress
        self.invoiceItemHeadNode = invoiceItemHeadNode

    # 請求書の支払総額を計算します。InvoiceItemHeadNodeから始まるすべてのリスト項目を反復処理し、数量も考慮して計算する必要があります。Tax inputがTrueに設定されている場合は、合計金額に10%を加算してください。
    def amountDue (self, taxes) :
        currentNode = self.invoiceItemHeadNode
        total = 0

        while currentNode is not None :
            total += currentNode.product.price * currentNode.quantity
            currentNode = currentNode.next

        return  total * 1.1 if taxes else total

    # 請求書の全項目と数量を出力します。「item :shampoo, price :10, quantity:7」のようにそれぞれのアイテムを出力してください。
    def printBuyingItems(self) :
        print("Printing the Item List...")
        currentNode = self.invoiceItemHeadNode
        while currentNode is not None :
            print("item :" + currentNode.product.title + ", price :" + str(currentNode.product.price) + ", quantity:" + str(currentNode.quantity))
            currentNode = currentNode.next


    # 請求書の全内容を出力します。以下のように出力してください。
    def printInvoice(self) :
        print(
            "Invoice\n" +
            "No. : " + self.invoiceNumber + "\n" +
            "INVOICE DATE : " + self.invoiceDate + "\n" +
            "SHIP TO : " + self.company + "\n" +
            "ADDRESS : " + self.companyAddress + "\n" +

            "BILL TO : " + self.billToName + "\n" +
            "ADDRESS : " + self.billToAddress + "\n"
        )

        currentNode = self.invoiceItemHeadNode
        while currentNode is not None :
            print(currentNode.product.title + "($" +str(currentNode.product.price) +")" + "--- " + str(currentNode.quantity) + " pcs. " + "--- AMOUNT: " + str(currentNode.product.price * currentNode.quantity))
            currentNode = currentNode.next


        print(
            "SUBTOTAL : " + str(self.amountDue(False)) + "\n" +
            "TAX : " + str(self.amountDue(True) - self.amountDue(False)) + "\n" +
            "TOTAL : " + str(self.amountDue(True))
        )

class InvoiceItemNode :
    def __init__(self, product, quantity) :
        self.product = product
        self.quantity = quantity
        self.next = None

    # 購入する数量に基づいて、製品の合計価格を計算します。
    def getTotalPrice(self) :
        return self.quantity * self.product.price

class Product:
    def __init__(self, title, price) :
        self.title = title
        self.price = price

product1 = Product ("shampoo", 10)
product2 = Product ("conditioner", 5)
product3 = Product ("tooth brush", 3)

firstItem = InvoiceItemNode(product1, 7)
secondItem = InvoiceItemNode(product2, 9)
firstItem.next = secondItem
thirdItem = InvoiceItemNode(product3, 10)
secondItem.next = thirdItem

invoice = Invoice ("UC1234567890", "2020/05/06", "Recursion", "Los Angles", "Steven", "Dallas", firstItem)

invoice.printBuyingItems()
invoice.printInvoice()

print(invoice.amountDue(False))
print(invoice.amountDue(True))
