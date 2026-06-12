def main():
    lst = list(map(int, input().split(' ')))
    if len(lst) >= 100 or len(lst) <= 1:
        return
    print(lst.count(1))
    print(lst.count(5))
    print(lst.count(10))
main()
