# 一行目は[数値]
# 二行目以降は一行目の数値の数だけ[数値]

input_number = int(input())

input_line = []

for i in range(input_number):
    input_line.append(int(input()))

input_line.sort(reverse=True)
input_line = list(dict.fromkeys(input_line))

print(len(input_line))
