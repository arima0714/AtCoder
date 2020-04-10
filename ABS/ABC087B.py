# 4行あり、各行数値が一つずつ入力される

num500 = int(input())+1
num100 = int(input())+1
num50  = int(input())+1
num_sum= int(input())

answer = 0

for n500 in range(num500):
    for n100 in range(num100):
        for n50 in range(num50):
            if 500 * n500 + 100 * n100 + 50 * n50 == num_sum:
                answer = answer + 1

print(answer)
