'''
高さ height と幅 width が与えられるので、デバイスの向きを返す、screenViewMode という関数を定義してください。もし、高さが幅以上の場合、portrait を返し、それ以外の場合では landscape を返します。
'''

def screenViewMode(height:int,width:int) -> str:

    # 述語 height が width 以上のときの処理
    if height >= width: return "portrait"
    # それ以外の処理
    return "landscape"

# --------------以下は解答に書く必要はありません---------------------
# テストケースを入れた関数を呼び出し、print() で表示してみましょう。

print(screenViewMode(200,150)); # portrait
print(screenViewMode(120,100)); # portrait
print(screenViewMode(50,100)); # landscape
print(screenViewMode(60,60)); # portrait
