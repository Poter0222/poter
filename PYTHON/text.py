def directory(src):
    import urllib.request as req
    rev=req.Request(src, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(rev) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("span",class_="ptname")
    from plyer import notification
    notification.notify(
        title="觀音高中- 新公告",
        message= titles.string,
        app_icon=None,
        timeout=10
    )
pageURL="http://www.gish.tyc.edu.tw/files/40-1000-14-1.php"
directory(pageURL)




