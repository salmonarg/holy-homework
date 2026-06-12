def count_char(s):
    char_dict = {}
    for i in range(len(s)):
        if s[i].isalpha:
            if s[i] not in char_dict:
                char_dict[s[i]] = 0
            char_dict[s[i]] += 1
    for key, value in sorted(char_dict.items()):
        print(key, ":", value, sep="")
def main():
    s = input("请输入一个字符串: ")
    s = s.lower()
    count_char(s)
main()
