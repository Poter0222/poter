#encoding=utf-8
# 06

# 函數的預設資料
# def 函式名稱(參數名稱=預設資料):
#    函式內部的程式碼
def power(base, exp=0):
    print(base**exp)
power(3, 2)

# 使用參數名稱對應
# def 函式名稱(名稱1, 名稱2)
#    函式內部的程式碼
def divide(n1, n2):
    print(n1/n2)
divide(2.0,4)
divide(n2=2,n1=4)

# 無限/不定 參數資料
# def 函式名稱(*無限參數):
#   無限參數以 Tuple 資料型態處理函式內部的程式碼
# 呼叫方式(可傳入無限輸量的參數) 
# 函式名稱(資料1, 資料2, 資料3)
def avg(*ns):
    sum=0
    for n in ns: 
        sum=float(sum+n)
    print(sum/len(ns))
avg(3,4)