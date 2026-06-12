def main():
    lst = []
    for i in range(1,6):
        lst.append(input(f"请输入字符串 {i}: "))
    lst.sort(reverse=True)
    print(f"最大的字符串: {lst[0]}")
main()
