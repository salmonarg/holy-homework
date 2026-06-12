def is_anagram(str1, str2):
    lst1 = list(str1)
    lst2 = list(str2)
    lst1.sort()
    lst2.sort()
    str1d = ""
    str2d = ""
    for ch in lst1:
        str1d += ch
    for ch in lst2:
        str2d += ch
    if str1d == str2d:
        return True
    else:
        return False
def main():
    str1 = input("请输入单词 1: ")
    str2 = input("请输入单词 2: ")
    if is_anagram(str1, str2):
        print("字母异位词")
    else:
        print("非字母异位词")
main()
