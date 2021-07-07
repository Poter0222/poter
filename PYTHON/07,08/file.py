#encoding= utf-8
# 07

# 儲存檔案
# 你檔案使用什麼格式就用什麼格式寫入 例如我用 utf-8 那顯示中文就沒問題
# 操作(寫入 w 、讀取 r 、讀寫 r+)
# 第一種寫法
import sys
file=open("deta1.txt", mode="w") # 開啟
file.write("hello file\nsecond line\n測試中文\n再次測試") 
file.close() # 關閉
# 第二種寫法（較推薦）
with open("deta2.txt",mode="w") as file:
    file.write("5\n3")

# 讀取檔案
sum=0
with open ("deta2.txt", mode="r") as file:
    for line in file: # 一行一行的讀取
        sum+=int(line) # 將讀取到的逐一相加
print(sum)

# 使用 JSON 格式讀取、複寫檔案
import json
# 從檔案中讀取 JSON y 資料，放入變數 deta 裡面
with open("config.json", mode="r") as file:
    deta=json.load(file) # deta 是一個字典資料
print("name", deta["name"])
print("version", deta["version"])
deta["name"]="new name" # 修改變數中的資料
# 把最新的資料覆寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(deta, file)



