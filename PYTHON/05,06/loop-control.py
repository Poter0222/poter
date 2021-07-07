#encoding=utf-8
#05
# 20210626 : 因為我編寫 print("中文字", n ) 時，它裡面的中文字會是亂碼，因此我藉由str(數字)把數值(inter)改成字串(string)來 string + striing
# review : range(n)代表 0 ~ n-1 的數字
# 重點：break 會強制結束回圈，不會執行 else 區塊

# break (強制跳出“整個”迴圈) 簡易編輯
n=0
while n<5:
    if n == 3:
        break
    print(n) # 印出迴圈中的 n
    n+=1
n_string=str(n)
s="最後的 n : "
print(s+n_string)# 印出迴圈跑完後的 n

# continue (強制跳出“本次”迴圈，繼續進入下一圈) 簡易範例
n1=0
for x in [0,1,2,3]:
    if x%2==0: # x 是偶數
        continue
    print(x)
    n1+=1
n1_string=str(n1)
s="最後的 n1 : "
print(s+n1_string)

# else 簡易範例
sum=0
for n in range(11):
    sum+=n
else:
    print(sum) # 印出 0+1+2+......+10

# 綜合範例：找出整數平方根
# Ex. 輸入9. 得到3
# Ex. 輸入11. 得到【沒有】整數平方根
n=int(input("請輸入一個正整數："))
for i in range(n):
    if i*i==n:
        i1=str(i)
        print("整數平方根："+i1)
        break # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
    print ("沒有整數平方根")









