num500 = int(input())
num100 = int(input())
num50  = int(input())
num_sum= int(input())

# if num500 != 0:
#     num500 = num500+1
# if num100 != 0:
#     num100 = num100+1
# if num50 != 0:
#     num50 = num50+1

answer = 0

# for n500 in range(num500):
#     for n100 in range(num100):
#         for n50 in range(num50):
#             if 500 * n500 + 100 * n100 + 50 * n50 == num_sum:
#                 answer = answer + 1

i = 0
j = 0
k = 0
while True:
    if i <= num500:
        while True:
            if j <= num100:
                while True:
                    if k <= num50:
                        if 500 * i + 100 * j + 50 * k == num_sum:
                            answer = answer + 1
                        k = k + 1
                    else:
                        break
                j = j + 1
            else:
                break
        i = i + 1
    else:
        break

print(answer)
