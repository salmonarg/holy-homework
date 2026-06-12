def mid(a, b, c):
    largest = a if a > b else b
    if c > largest:
        largest = c
    lst = [a, b, c]
    lst.remove(largest)
    res = max(lst)
    return res
def main():
    a, b, c = map(int, input("请输入三个整数: ").split(','))
    res = mid(a, b, c)
    print(f"中间数: {res}")
main()
