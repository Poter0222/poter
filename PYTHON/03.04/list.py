#coding=UTF-8
# 03

# 有序可變動列表 List
# 跟字串類似，一樣會對列表內的資料做編號
grades=[12,60,15,70,90]
print(grades[0]) # [x] 第x個資料
grades[0]=55 # 把grades列表中的第0個資料改成55 
print(grades)
print(grades[1:4]) # 跟字串概念相同
grades[1:4]=[] # 連續刪除列表中從編號 1 到編號 4（不包括）的資料
print(grades)
grades=grades+[12,13] # 串接列表（有加法概念）
print(grades)
length=len(grades) # 可取得列表的長度（資料數）len(列表名稱)
print(length)
# 巢狀列表
deta=[[3,4,5],[6,7,8]] # 列表[3,4,5]是 deta 的第 0 個資料
print(deta[0][1]) # 印出deta第 0 個資料的 第 0 個東西
print(deta[0][0:2]) # 印出deta第 0 個資料的第0到2的東西
deta[0][0:2]=[5,5,5] #把deta第 0 個資料的第 0 到 2 個位置改成 5,5,5
print(deta[0])







