# 入力は二行でそれぞれ[数値]

input_nums = int(input())
input_line = input()

result = 0

for k in range(input_nums):
    for j in range(k):
        for i in range(j):
            if(j-i == k-j):
                pass
            elif(input_line[i] == input_line[j]):
                pass
            elif(input_line[i] == input_line[k]):
                pass
            elif(input_line[j] == input_line[k]):
                pass
            else:
                result = result + 1

print(result)
