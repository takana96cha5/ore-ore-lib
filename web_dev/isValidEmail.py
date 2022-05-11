'''
メールアドレス認証

Paul は自身のサービスのベータテストユーザーを、メールアドレス登録によって受け付けようと思いました。
その際、ユーザーのメールアドレスが有効なものなのかをチェックするプログラムが必要になります。
あるメールアドレス email を受け取るので、それが正しいものであれば true を、そうでなければ false を返す isValidEmail という関数を作成してください。
ここでの正しいアドレスというのは以下の 4 つの条件を満たすものを指します。
'''
def isValidEmail(email):
    # ＠の後のインデックス
    atIndex = email.find("@")

    # ＠の後のアドレス
    domain = email[atIndex + 1:len(email)]

    if atIndex > 0 and email.find(" ") == -1 and domain.find("@") == -1 and not domain.find(".") == -1:
        return True
    else:
        return False

print(isValidEmail("ccc@aaa.com"))
print(isValidEmail("c@cc@aaa.com"))
print(isValidEmail("cc c@aaa.com"))
print(isValidEmail("cc.c@aaacom"))
print(isValidEmail("cc.c@aaa.com"))
print(isValidEmail("@aaa.com"))

# ---------------------------------------------------------------------------------------
def isValidEmail(email: str) -> bool:
    atmarkIndex = email.find("@")
    domain = cutoutDomain(email)
    return not isInitial(atmarkIndex) and not containSpace(email) and inOnlyOneAtmark(email) and containDot(domain)


def cutoutDomain(email:str) -> str:
    atIndex = email.find("@")
    return email[atIndex + 1:len(email)]

def isInitial(atIndex: int) -> bool:
    return atIndex == 0

def containSpace(email: str) -> bool:
    return not email.find(" ") == -1

def inOnlyOneAtmark(email: str) -> bool:
    return email.count("@") == 1

def containDot(domain: str) -> bool:
    return not domain.find(".") == -1
