#encoding=utf-8
# 06

# 定義函式
# 函式內部的程式碼，若是沒有做函式呼叫，就不會執行
# return：回傳，不看過程，reture只會回傳自己那一行後面的資料
# def 函式名稱(參數名稱):
#    函式內部程式碼
def multiply(n1, n2):
    print(n1*n2)
    return 
def multiply_1(n1, n2):
    return n1*n2 # 直接return回傳值的情況通常是在有"函式外部繼續操作資料"的需求時使用

# 呼叫函式
# 之所以會回傳兩個值是因為我 print(n1*n2) 又 return
value=multiply(5, 6) # 把回傳值放入 value
print(value) 
value_1=multiply_1(4, 3)+multiply_1(5, 10) # 同 (3*4)+(5*10)
print(value_1)

# 程式的包裝
def calculate(n1, n2):
    sum=0
    for n in range(n1, n2):
        sum=sum+n
    print(sum)

calculate(0, 11)




