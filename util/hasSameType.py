'''
マッチングアプリ
medium
Redd はマッチングアプリを開発しています。
ユーザーの属性をアルファベットで記録しており、
アルファベットの並ぶパターンが同じユーザーは相性が良いと判定しています。
ユーザー1 の属性 user1、ユーザー2 の属性 user2 が与えられるので、
この 2 つが同じパターンをしているかどうか判定する、hasSameType という関数を定義してください。
'''

def hasSameType(user1:str,user2:str) -> bool:
    # user1とuser2の文字列の長さが異なる時点でFalse
    if len(user1) != len(user2):
        return False

    # user1の文字をキー、user2の文字を値としてハッシュマップを作成
    hashmap1 = {}
    # user2の文字をキー、user1の文字を値としてハッシュマップを作成
    hashmap2 = {}

    for i in range(len(user1)):
        hashmap1[user1[i]] = user2[i]
        hashmap2[user2[i]] = user1[i]

    # user1[i]の値とhashmap2[user2[i]]の値が等しくなければFalse
    # （辞書型は同じキーがあった場合上書きされる法則を利用している）
    for i in range(len(user1)):
        if user1[i] != hashmap2[user2[i]] or user2[i] != hashmap1[user1[i]]:
            return False

    return True

'''
入力のデータ型： string user1, string user2

出力のデータ型： bool

hasSameType("aabb","yyza") --> false

hasSameType("aappl","bbtte") --> true

hasSameType("aappl","bbttb") --> false

hasSameType("aabb","abab") --> false

hasSameType("aappl","bktte") --> false

hasSameType("aaapppl","bbbttke") --> false

hasSameType("abcd","tso") --> false

hasSameType("abcd","jklm") --> true

hasSameType("aaabbccdddaa","jjjddkkpppjj") --> true

hasSameType("aaabbccdddaa","jjjddkkpppjd") --> false
'''

