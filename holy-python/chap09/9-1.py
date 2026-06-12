import math

def square_root(x):
    if x < 0:
        raise ArithmeticError("Invalid")
    return math.sqrt(x)
def main():
    x = float(input())
    try:
        print(f"{square_root(x):.2f}")
    except ArithmeticError as ex:
        print(ex)
main()
