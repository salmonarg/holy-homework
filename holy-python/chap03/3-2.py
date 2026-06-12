import math

x = float(input("输入x: "))
if x < 0:
    y = x ** 2
elif x >= 0 and x < 9:
    y = math.sqrt(x)
else:
    y = x - 6
y = format(y, ".2f")
print(f"分段函数的值: {y}")
