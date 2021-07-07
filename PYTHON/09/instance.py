#encoding= utf-8
# 09

# Point  實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
P=Point(3, 4)
P.show() # 呼叫實體方法(函式) 
result=P.distance(0, 0) # 呼叫計算座標 3,4 和座標 0,0 之間的距離
print(result)

# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    # 定義初始化函式
    def __init__(self, name):
        self.name=name
        self.file=None # 尚未開啟檔案: 初期是 None
        # 定義實體方法
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一個檔案
F1=File("instance-test1")
F1.open()
deta=F1.read()
print(deta)
# 讀取第二個檔案
F2=File("instance-test2")
F2=open()
deta=F2.read()
print(deta)

