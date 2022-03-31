#1
price_list = [32100, 32150, 32000, 32500]
for a in range(4):
    print(f"{a} {price_list[a]}")
#2
price_list = [32100, 32150, 32000, 32500]
for a in range(1, 4):
    print(f"{90 + a*10} {price_list[a-1]}")
#3
for a in range(2002, 2051, 4):
    print(a)
#4
for a in range(10):
    print(a/10)
#5
ticker = "btc_krw"
print(ticker.upper())
#6
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
#7
a = "hello world"
r = a.split(" ", 1)
print(f"{r}")
#8
date = "2020-05-01"
r = date.split("-", 2)
print(f"{r}")
#9
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(",", "")
t = int(a)
print(t)
#10
a = "hello world"
r = a.split(" ", 1)
print(f"{r}")
#11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
#12
nums = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
print(nums[1::2])
#13
리스트 = [3, 100, 23, 44]
for a in range(4):
    if 리스트[a] % 3 == 0:
        print(f"{리스트[a]}")
