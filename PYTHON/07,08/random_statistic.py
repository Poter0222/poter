#encoding= utf-8
# 07
# 平均數、中位數、標準差、常態分配

# 隨機模組
import random
# 隨機選取
print("-----隨機選取-----")
deta_sample=random.sample([1,5,6,10,20], 3)
print(deta_sample)

# 隨機調換順序 (洗牌的概念)
print("-----隨機調換-----")
deta_shuffle=[1,5,8,20]
random.shuffle(deta_shuffle)
print(deta_shuffle)

# 隨機取得亂數 
print("-----隨機取得亂數-----")
deta_random=random.random() # 0 ~ 1 之間的隨機亂數
deta_uniform=random.uniform(0.0, 1.0) # 同 random
deta_uniform1=random.uniform(60, 100) # 60 ~ 100 之間的隨機亂數
print(deta_random)
print(deta_uniform)
print(deta_uniform1)

# 取得常態亂數 (大部分資料都會集中在你設定的範圍內，會有少數例外)
# 資料名稱=ramdom.normalvariate(平均數, 標準差)
print("-----取得常態分配亂數-----")
deta_normalvariate=random.normalvariate(100,10) # 平均數 100, 標準差 10, 得到的資料數多在 90 ~ 100 之間
print(deta_normalvariate)
 
# 統計模組
# 解決 找不到statistics 的網址 https://stackoverflow.com/questions/53965561/import-statistics-fails-to-run
print("-----統計模組-----")
import sys # 因為我終端機本來找不到 statistics 模組，引此透過 pip3 install statistics 來顯示 statistics 的路徑，之後用 sys 增加路徑
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")
import statistics as stat
# 平均數
deta_mean=stat.mean([1,2,3,4,5,8,100]) # 取得列表資料的平均數
print(deta_mean)
# 中位數
deta_median=stat.median([1,2,3,4,5,8,100]) # 取得列表中間的資料(中間值)
print(deta_median)
# 標準差
data_stdev=stat.stdev([1,2,3,4,5,8,10])
print(data_stdev) # 取得列表的標準差





