'''
ページ付け

Joe は web サイト作成をしており、pagination を担当することになりました。
URL によって構成される配列 urls、各ページのサイズ pageSize、特定のページ page が与えられるので、
特定のページに表示される URL を返す、websitePagination という関数を作成してください。
例えば、url1, url2, url3, url4, url5, url6, url7, url8, url9 の一覧があり、1 ページに含まれる URL の数が 3、現在作成しているページが 2 ページ目の場合、
各ページに 3 つの URL が含まれることになるので、返される配列は 2 ページに含まれる url4, url5, url6 になります。

-------------------------------
| Previous | 1 | 2 | 3 | Next |
-------------------------------

'''

def websitePagination(urls:str,pageSize:int,page:int) -> str:
    pageGroup = []
    for i in range(0, len(urls), pageSize):
        pageGroup.append(urls[i:i + pageSize])
    return pageGroup[page-1]

# --------------------------------------------------

def websitePagination(urls,pageSize,page):
    # 現在のページにあるurlの最初のインデックス
    index = pageSize * (page - 1)
    output = []

    # pageSize分だけurlを取得していきます
    # インデックスが配列のサイズを超えるか、urlをoutputに格納した回数がpageSizeに到達したら処理を終えます
    while index < len(urls) and pageSize > 0:
        output.append(urls[index])
        index += 1
        pageSize -= 1

    return output

print(websitePagination(["url1","url2","url3","url4","url5","url6"],4,1))
print(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],3,2))
print(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],4,3))
