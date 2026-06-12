import math
import sys

a, b, c = map(float, input("输入一元二次方程的系数a, b, c: ").split(','))

delta = b**2 - 4*a*c

if a == 0 and b == 0 and c == 0:
    print("方程无穷解!")
    sys.exit(0)
if a == 0 and b == 0 and c != 0:
    print("方程无解!")
    sys.exit(0)
if a == 0 and b != 0:
    x = -c/b
    print(f"方程有一个根: x={x:.2f}")
    sys.exit(0)

if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"方程有两个不同实根: x1={x1:.2f} x2={x2:.2f}")
elif delta == 0:
    x1 = x2 = -b/(2*a)
    print(f"方程有两个相同实根: x1=x2={x1:.2f}")
else:
    x1 = (-b + math.sqrt(abs(delta))*1j)/(2*a)
    x2 = (-b - math.sqrt(abs(delta))*1j)/(2*a)
    print(f"方程有两个不同虚根: x1={x1.real:.2f}{x1.imag:+.2f}i x2={x2.real:.2f}{x2.imag:+.2f}i")

