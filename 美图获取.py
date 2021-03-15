import requests, json, re
num = 3 #只爬取5张图,可以调大，如果中间网络异常会丢失几张图，最终数量可能达不到
#数量过大可能会被反爬，建议每次不超过18张图。

#下面开始爬取P站图片
datas = []
headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            "Referer": "https://www.pixiv.net/",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": "PHPSESSID=【请在浏览器里面的开发工具里面找PHPSESSID值】"
            }


session = requests.session()

list = session.get("https://www.pixiv.net/ajax/top/illust?mode=all&lang=zh", headers=headers,verify=False).json()["body"]["thumbnails"]["illust"];
# 因为我现在不会验证SSL，所以将verify给关闭了。
for i in range(num):
    id = list[i]["id"]
    print("图片id："+id)
    title = list[i]["title"]
    print("图片标题："+title)
    url = f'https://www.pixiv.net/artworks/{id}'
    print(url)
    try:
        res = session.get(url, headers=headers)
        findurl = re.findall('.*?\"original\":\"(.*?)\"\}.*',res.text)[0]
        print('原图链接：'+findurl)
        res = session.get(findurl, headers=headers)
    except:
        continue


