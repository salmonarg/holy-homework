def main():
    line = input().split()
    numbers = [int(n) for n in line]
    if len(numbers) != 20:
        return
    count = len(set(numbers))
    print(count)
main()

