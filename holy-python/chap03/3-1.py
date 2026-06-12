number = int(input("输入一个整数: "))
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} 能同时被 2 和 3 整除!")
if number % 2 == 0 or number % 3 == 0:
    print(f"{number} 能被 2 或 3 整除!")
    if (number % 2 == 0) != (number % 3 == 0):
        print(f"{number} 能被 2 或 3 整除且只被其一整除!")

