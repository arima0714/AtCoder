num500 = int(input())
num100 = int(input())
num50  = int(input())
num_sum= int(input())

answer = 0

for n500 in range(num500 + 1):
    for n100 in range(num100 + 1):
        for n50 in range(num50 + 1):
            if 500 * n500 + 100 * n100 + 50 * n50 == num_sum:
                answer = answer + 1

print(answer)
