# 1行目に2行目以降に入力される整数の個数
# 2行目 [数値1 数値2 数値3 ...]

input_num = int(input())
input_line = input().split()
input_line = [int(s) for s in input_line]

counter = 0
loop = True

while True:
    for k in input_line:
        if (k % (2 ** counter)) != 0:
            loop = False
            break
        elif loop == True:
            continue
    if loop == False:
        break
    elif loop == True:
            counter = counter + 1
            continue

print(counter-1)
