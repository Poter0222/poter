def directory(src, keyword):
    import urllib.request as req
    rev=req.Request(src, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(rev) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("span",class_="ptname")
    with open("觀音高中news.txt", "a", encoding="utf-8") as file:
        for title in titles:
            title=title.getText().strip()
            title_s=title.find(keyword)
            if title_s !=-1:
                file.write(title +"\n")
            else:
                continue
    nextlink=root.find("a", string="下一頁")
    return nextlink["href"]
pageURL="http://www.gish.tyc.edu.tw/files/40-1000-14-1.php"
time=int(input("請輸入搜索頁數 : "))
keyword_title=input("請輸入標題關鍵字 : ")
count=1
while count<=time:
    if count==1:
        with open("觀音高中news.txt","w",encoding="utf-8") as file:
            file.truncate(0) #　truncate(size)刪除 txt 中的內容, size:從哪行開始刪除
    pageURL=directory(pageURL, keyword_title)
    count+=1
else:
    print("---------DONE---------")

