# 一行目は[数値]
# 二行目以降は一行目の数値の数だけ[数値]

input_number = input()
input_line = list(input().split())
input_line = [int(s) for s in input_line]

input_line.sort(reverse=True)
input_line = list(dict.fromkeys(input_line))

print(len(input_line))