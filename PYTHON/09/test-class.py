#encoding= utf-8
# 09

# 定義規則、類別屬性(封裝在類別中的 變數 和 函式 )
# 定義一個類別 IO, 有兩個屬性 supportedsrcs 和 read
class IO:
    supportedsrcs=["console", 'file']
    def read(src):
        if src not in IO.supportedsrcs:
            print("Not Supported")
        else:
            print("Read form", src)

# 使用類別
print(IO.supportedsrcs)
IO.read("file")
IO.read("internet")