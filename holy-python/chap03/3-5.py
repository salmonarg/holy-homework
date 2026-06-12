numbers = input("输入整数: ").split(' ')

pos_count = 0
neg_count = 0
sum = 0
count = 0

# 正整数计数
for num in numbers:
    if int(num) > 0:
        pos_count += 1

print(f"正整数的个数是 {pos_count}")

# 负整数计数
for num in numbers:
    if int(num) < 0:
        neg_count += 1

print(f"负整数的个数是 {neg_count}")

# 求和与平均值
for num in numbers:
    sum += int(num)
    count += 1
avg = format(sum / count, ".2f")

print(f"整数和为 {sum}")
print(f"整数的平均值为 {avg}")
