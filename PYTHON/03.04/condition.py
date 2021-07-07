#coding=utf-8
# 04

# 判斷式
x=input("請輸入數字：") # 取得字串形式的輸入
x=int(x) # 將字串型態轉換成單純 "數字"
if x>200:
    print("大於200")
elif x>100:
    print("大於100, 小於等於200")
else:
    print("小於等於100")
# 四則運算
n1=float(input("請輸入數字一：")) # float 把字串型態轉成 "浮點數" 
n2=float(input("請輸入數字二："))
op=input("請輸入運算符號(+,-,*,/):")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援")


