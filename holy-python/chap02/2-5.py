money = float(input("输入存款: "))
year = int(input("输入存期: "))
rate = float(input("输入年利率: "))
interest = money * pow(1 + rate, year) - money
interest = round(interest, 2)
print(f"存款到期前的税前利息: {interest}")
