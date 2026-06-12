import sys

score = int(input("输入学生的考试成绩: "))
if score > 100 or score < 0:
    print("学生成绩需为0～100范围内的整数")
    sys.exit(1)
if score >= 90:
    print("等级: A")
elif score >= 80:
    print("等级: B")
elif score >= 70:
    print("等级: C")
elif score >= 60:
    print("等级: D")
else:
    print("等级: E")

