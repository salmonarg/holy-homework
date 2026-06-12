def count_vowel(vowel, line):
    count = 0
    for ch in line:
        if ch == vowel:
            count += 1
    return count
def main():
    line = input()
    line = line.lower()
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        print(count_vowel(vowel, line), end=" ")
    print("")
main()
