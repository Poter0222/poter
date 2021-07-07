#encoding=utf-8
# 07

# 載入內建的 sys 模組並取得資訊
# import 模組名稱 as 模組別名
import sys as s
s.path.append("modules") # 在模組的搜尋列表中【 新增路徑 】
print(s.platform) # 印出作業系統
print(s.maxsize) # 印出整數型態的最大值

# 建立 geometry 模組，載入使用 (我有建立了 module_geometry.py 的模組)
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

# 調整搜尋模組的路徑
import sys
print(sys.path) # 印出模組的搜尋路徑
print("-------------------")
print(geometry.distance(3,4,6,7))

