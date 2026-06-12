def reverse(n):
    if n == 0:
        return 0
    raw_string = str(abs(n))
    count = len(raw_string)
    rev_string = ""
    abs_n = abs(n)
    flag = 0
    for i in range(count):
        digit = abs_n % 10
        abs_n //= 10
        if digit == 0 and flag == 0:
            continue
        flag = 1
        rev_string += str(digit)
    if n >= 0:
        rev_number = int(rev_string)
    else:
        rev_number = -int(rev_string)
    return rev_number
def main():
    raw = int(input("请输入一个整数: "))
    rev_num = reverse(raw)
    print(f"逆序数: {rev_num}")
main() 
