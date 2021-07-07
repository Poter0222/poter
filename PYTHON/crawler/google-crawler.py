def getData(src, keyword):
    import urllib.request as req
    rev=req.Request(src, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(rev) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautufulsSoup 協助我們分析 HTML 格式文件
    titles=root.find_all("h3", class_="LC20lb DKV0Md")
    for title in titles:
        title=title.getText()
        title_s=title.find(keyword)
        if title_s != -1:
            print(title)
        else:
            continue
    nextlink=root.find("a",id="pnnext")
    return nextlink["href"]
pageURL=input("請輸入搜索網址 : ")
keyword=input("請輸入關鍵字 : ")
count=0
time=int(input("請輸入搜索頁數 : "))
while count<=time:
    pageURL="http://www.google.com"+getData(pageURL, keyword)
    count+=1
else:
    print("---------DONE---------")