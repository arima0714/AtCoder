# 入力は1行の文字列

input_str = input()
result = 0

for index in input_str:
    if index == "1":
        result += 1

print(result)