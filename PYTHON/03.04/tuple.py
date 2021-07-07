#coding=UTF-8
# 03

# 有序不可變動列表 Tuple
# 概念同 List ，只是不能去變動資料
data=(3,4,5)
print(data[0:2])
data[0]=5 # 會發生錯誤，因為 Tuple 的資料不可變動
print(data)
