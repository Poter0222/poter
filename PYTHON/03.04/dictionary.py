#encoding=utf-8
# 04

# 字典的運算：key-value 配對
dic={"apple":"頻果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小頻果"
print(dic["apple"])
print("apple" in dic) # 判斷 key 是否存在 （只判斷 key 不看value)
print("蟲蟲" in dic) # 只判斷 key 不看 value
print("text" in dic)
print("text" not in dic)
del dic["apple"] # 刪除字典中的鍵值對(key-value pair)
import json 
dic_json = json.dumps(dic,ensure_ascii=False,encoding="UTF-8")
print(dic)

# 將列表帶入字典
dictionary={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print(dictionary)

