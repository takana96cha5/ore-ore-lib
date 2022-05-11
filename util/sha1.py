#coding:utf-8

import hashlib

def main():
    # 文字列
    message = "password01"
    # 文字列をエンコード
    encoded_message = message.encode("utf-8")
    # 文字列からsha1 のハッシュ値を求める
    hash_object = hashlib.sha1(encoded_message)
    # ハッシュ値を16進数でプリント
    print(hash_object.hexdigest())

if __name__ == "__main__":
    main()
