#coding:utf-8

import hashlib

def main():
    # 変換したい文字列
    message = "password01"
    # ハッシュ値を求めた結果
    print(hashlib.sha1(message.encode("utf-8")).hexdigest())

if __name__ == "__main__":
    main()
