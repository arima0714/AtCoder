# 入力は1行で[数値 数値]
line_1 = input().split()

if (int(line_1[0]) * int(line_1[1])) % 2:
    print("Odd")
else:
    print("Even")
