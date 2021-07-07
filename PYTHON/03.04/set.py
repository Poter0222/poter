#coding=UTF-8
# 04

# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 in s1)
print(10 not in s1)
s2={4,5,6,7}
s3=s1&s2 # & 交集：數學中”交集”的概念(兩集合中相同的資料)
print(s3) 
s4=s1|s2 # | 聯集：數學中”聯集“的概念(兩集合中的所有資料，但不重複)
print(s4)
s5=s1-s2 # - 差集：從 s1 中，減去和 s2 相同(重疊)的資料
print(s5)
s6=s1^s2 # ^ 反交集：取兩個集中，不重疊的部分
print(s6)

# 把字串中的字母拆解成集合
s=set("hello") # set (你要拆解的字串)
print("h" in s)
print("A" in s)
print("A" not in s )
