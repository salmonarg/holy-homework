c_degree = eval(input("输入摄氏温度: "))
f_degree_raw = ((9 / 5) * c_degree) + 32
f_degree = format(f_degree_raw, ".2f")
print(f"对应的华氏温度: {f_degree}")
