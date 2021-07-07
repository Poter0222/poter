# 抓取 PTT 八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件, 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)

    # 解析資料，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautufulsSoup 協助我們分析 HTML 格式文件
    # print(root.prettify)
    titles=root.find_all("div", class_="title") # 尋找所有 class="title"的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤(沒有被刪除) 印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextlink=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextlink["href"]
    # print(nextlink["href"]) # 指定其中的 href 的屬性
# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
time=int(input("請輸入要搜索幾頁 : "))
while count<=time:
    pageURL="http://www.ptt.cc"+getData(pageURL)
    count+=1
else:
    print("---------結束---------")

