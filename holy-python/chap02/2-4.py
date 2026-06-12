import math
a = int(input("输入整数a: "))
rad50 = math.radians(50)
res_raw = (math.cos(rad50) + math.sqrt(37.5)) / (a + 1)
res = format(res_raw, ".2f")
print(f"计算结果: {res}")
