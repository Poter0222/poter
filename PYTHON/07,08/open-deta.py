#encoding= utf-8
# 08

# 網路連線
# Ex. 台大官網
import urllib.request as request
src1="https://www.ntu.edu.tw/"
with request.urlopen(src1) as response:
    deta1=response.read().decode("utf-8") #　取得網站的原始碼
print(deta1)

# Ex. 內湖科技園區廠商目錄
import urllib.request as request
import json # 因為範例的格式是 json
src2='https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'
with request.urlopen(src2) as response:
    deta2=json.load(response) # 利用 JSON 模組處理 json 格式資料
print(deta2)

# 將公司列表名稱列表出來
clist=deta2["result"]["results"]
with open("company.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")


