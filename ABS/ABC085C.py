# 入力は一行のみで[数値1 数値2]の形式

input_line = input().split()
input_line = [int(s) for s in input_line]

print(input_line)