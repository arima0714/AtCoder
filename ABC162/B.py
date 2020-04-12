# 入力は一行のみで[数値]

input_num = int(input())

answer = 0

for i in range(input_num):
    if i%3 == 0:
        pass
    elif i%5 == 0:
        pass
    else:
        answer = answer + i

print(answer)
