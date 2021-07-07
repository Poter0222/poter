#encoding=utf-8
# 07
# 因為我不能用 import 資料夾名稱.模組名稱 來呼叫，因此只好先用 sys 新增路徑，之後再導入模組。


# 主程式
import geometry
import geometry.point
result_distance=point.distance(3,4)
result_distance=str(result_distance)
print("距離："+result_distance)

import geometry.line
result_line=line.slope(1,1,3,3)
result_line=str(result_line)
print("斜率："+result_line)