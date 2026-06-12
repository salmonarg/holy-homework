import sys

num = int(input("输入三位正整数(个位数不为0):"))
ones = num % 10
if ones == 0:
    print("个位数不可为0")
    sys.exit(1)
tens_raw = num // 10
tens = tens_raw % 10
hunds = tens_raw // 10
rev_num = str(ones) + str(tens) + str(hunds)
print(f"逆序后的数: {rev_num}")
