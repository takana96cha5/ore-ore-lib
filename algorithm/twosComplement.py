'''
2の補数
medium
Chan は宿題で、2 進数で 2 の補数を求めるプログラム作成を課されました。
2 進数 bits が与えられるので 2 の補数を返す、twosComplement という関数を作成してください。
ただし入力の 2 進数は 8 ビットとします。
通常、回路はオーバーフローしたビットを保持することはできないですが、今回は 00000000 の 2 の補数の最上位ビットを出力に含めてください。
'''
def twosComplement(bits):
    twosComplement = onesComplement(bits)
    carryOut = False

    for i in reversed(range(0, len(twosComplement))):
        if twosComplement[i] == '0':
            twosComplement = twosComplement[:i] + '1' + twosComplement[i + 1:]
            carryOut = False
            break

        elif twosComplement[i] == '1':
            twosComplement = twosComplement[:i] + '0' + twosComplement[i + 1:]
            carryOut = True

    return '1' + twosComplement if carryOut else twosComplement

def onesComplement(bits):
    onesComplement = ''
    for bit in bits:
        if bit == '1':
            onesComplement += '0'
        else:
            onesComplement += '1'
    return onesComplement

print(twosComplement("00011100"))
print(twosComplement("10010"))
print(twosComplement("001001"))
print(twosComplement("0111010"))
print(twosComplement("1"))

# ---------------------------------------------------------------------------
def twosComplement(bits):
    twoscomp = onesComplement(bits)
    #1の補数の末尾が"0"なら末尾を"1"に置換
    if twoscomp[-1] == "0":
        twoscomp[-1] = "1"
        return "".join(twoscomp)
    else:
        #末尾から順に"0"を探して"0"の要素を"1"に置換(1回のみ)
        for i in range(len(twoscomp)-1,-1,-1):
            if  twoscomp[i] == "0":
                twoscomp[i] = "1"
                return "".join(twoscomp)
                break
            else:
                #2の補数は繰り上げなので見たところは"0"に置換
                twoscomp[i] = "0"
                continue
    #全て"1"の場合は先頭に"1"を追加する
    if all(val == twoscomp[0] for val in twoscomp) == True:
        twoscomp.insert(0,"1")
        return "".join(twoscomp)

#1の補数を求める関数
def onesComplement(bits):
    onescom = []
    for i in bits:
        if i == "0":
            onescom.append("1")
        else:
            onescom.append("0")
    return onescom

# ---------------------------------------------------------------------------

def twosComplement(bits):
    # 2進数bitsとoneの足し算を行う

    # bitsを1の補数(ビット反転)してリスト型にする
    bits = list(onesComplement(bits))
    # 中身が1の配列を用意
    one = [1]

    # ２進数1桁分の足し算の結果を格納する変数を用意
    carry = 0
    # 出力用の変数を用意
    res = ""

    # 足し合わせるに変数、または、1桁分の足し算の結果を格納する変数がnullでないとき
    while len(bits) > 0 or len(one) > 0 or carry > 0:

        # bitsの要素がnullでないとき、bitsの一番右の桁をpopしてcarryに加える
        if len(bits) > 0 : carry += int(bits.pop(-1))

        # oneの要素がnullでないとき、oneの一番右の桁をpopしてcarryに加える
        if len(one)  > 0 : carry += int(one.pop(-1))

        # 繰り上がりが発生した場合、左端に 1 を加える処理
        # carryを2で割った余りを出力用の変数に加える
        res = str(carry % 2) + res

        # carryの中身が1を超えないようにする処理
        carry //= 2 # 切り捨て除算をしてcarryに代入している

    return res

# 1の補数を求める関数
def onesComplement(bits):
    onesComplement = ""
    for i in bits:
        if i == "1":
            onesComplement += "0"
        else:
            onesComplement += "1"

    return onesComplement
