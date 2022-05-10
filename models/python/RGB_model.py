'''
int red	0 から 255 までの数値
int green	0 から 255 までの数値
int blue	0 から 255 までの数値
String getHexCode()	カラーコードを 16 進数（文字列）で返します。文字列の先頭には # をつけてください。
Striing getBits()	カラーコードを 2 進数で返します。取得した 16 進数を 2 進数へ変換してください。
String getColorShade()	赤、青、緑の中でどの色が濃いのかを文字列で返します。全ての色の強さが同じ場合、grayscale と返してください。
'''

class RGB:
    hexadecimal = '0123456789abcdef'
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def changeDecToHex(self, decimal):
        """
        10進数を16進数に変換する

        Args:
          decimal(int): 10進数

        Returns:
          hex(str): 16進数
        """
        hex = ''
        while(decimal >= 0):
            currentHex = decimal % 16
            hex = self.hexadecimal[currentHex] + hex
            decimal //= 16
            if decimal == 0: break
        return hex
    def changeHexToBinary(self, hex):
        """
        16進数を2進数に変換する

        Args:
          hex(str): 16進数

        Returns:
          binary(str): 2進数
        """
        hex = self.hexadecimal.find(hex)
        binary = ''
        while(hex >= 0):
            currentBinary = hex % 2
            binary = str(currentBinary) + binary
            hex //= 2
            if hex == 0: break
        return binary
    def getHexCode(self):
        """
        カラーコードを16進数で返す

        Returns:
          (str): カラーコード
        """
        redHex = self.changeDecToHex(self.red).zfill(2)
        greenHex = self.changeDecToHex(self.green).zfill(2)
        blueHex = self.changeDecToHex(self.blue).zfill(2)
        return f'#{redHex}{greenHex}{blueHex}'
    def getBits(self):
        """
        カラーコードを2進数で返す

        Returns:
          (str): 2進法に基づくカラーコード
        """
        bits = ''
        hex = self.getHexCode()[1:]
        for i in hex:
            binary = self.changeHexToBinary(i)
            bits += binary.zfill(4)
        return bits.lstrip('0')
    def getColorShade(self):
        """
        RGBのうちで一番濃い色を文字列で返却

        Returns:
          (str): 一番濃い色 ※全て同じなら'grayscale'
        """
        if self.red == self.blue == self.green: return 'grayscale'
        RGBDict = {'red': self.red, 'green': self.green, 'blue': self.blue}
        return max(RGBDict, key=RGBDict.get)

color1 = RGB(0, 153, 255)
print(color1.getHexCode())
print(color1.getBits())
print(color1.getColorShade())

color2 = RGB(255, 153, 204)
print(color2.getHexCode())
print(color2.getBits())
print(color2.getColorShade())

color3 = RGB(0, 87, 0)
print(color3.getHexCode())
print(color3.getBits())
print(color3.getColorShade())

gray = RGB(123, 123, 123)
print(gray.getHexCode())
print(gray.getBits())
print(gray.getColorShade())
