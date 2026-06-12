def main():
    lst = list(map(int, input("请输入10个整数: ").split(' ')))
    if len(lst) != 10:
        print("请输入10个整数")
        return
    lst_sorted = lst.copy()
    lst_sorted.sort()
    min = lst_sorted[0]
    max = lst_sorted[9]
    i_min = lst.index(min)
    i_max = lst.index(max)
    print(max, i_max)
    print(min, i_min)
main()
