from random import randint

def main():
    count = int(input("输入需要生成的随机整数个数: "))
    with open("example.txt", 'w') as fo:
        for i in range(count):
            fo.write(str(randint(100,999)))
            if (i + 1) % 5 == 0:
                fo.write("\n")
            else:
                fo.write(" ")
        if count % 5 != 0:
            fo.write("\n")
main()
