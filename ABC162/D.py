input_nums = int(input())
input_line = input()

for k in range(input_nums):
    for j in range(k):
        for i in range(j):
            if(i > j or j > k):
