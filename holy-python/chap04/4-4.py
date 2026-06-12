import sys

def is_ugly(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return True
    else:
        return False
def main():
    n = int(input("请输入一个正整数: "))
    if n <= 0:
        print("请输入正整数")
        sys.exit(1)
    print(is_ugly(n))
main()
