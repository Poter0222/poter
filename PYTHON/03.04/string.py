#coding=UTF-8
# 03

# 字串運算
# 字串會對內部的字元編號（索引），從 0 開始
s="hello\"o" # \ 在雙引號前面打入，代表跳脫（跟外面雙引號作區隔) 去避免你打的字串中有跟外面符號衝突的問題
print(s)
# 字串的串接
s="hello"+"world"
print(s)
s="hello" "world" # 同 x="hello"+"world"
print(s)
# 字串換行
s="hello\nworld" # /n代表換行
print(s)
s=""" hello


world"""  # 前後加入“”“可將字串具體空出你空的行數
print(s)
s="hello"*3+"world" #概念同 先乘除後加減
print(s)
# 對字串編號
s="hello"
print(s[1])
print(s[1:4]) # 不包含第 ４ 個字元
print(s[:4]) # 到第 4 個字串（不包含）
