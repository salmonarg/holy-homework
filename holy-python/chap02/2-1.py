a = int(input("输入整数1: "))
b = int(input("输入整数2: "))
total = a + b
avg = format((a + b) / 2 ,".2f")
list1 = [a, b]
max_num = max(list1)
min_num = min(list1)
print(f"两个整数的和: {total}")
print(f"两个整数的平均值: {avg}")
print(f"两个整数的最小值: {min_num}")
print(f"两个整数的最大值: {max_num}")
