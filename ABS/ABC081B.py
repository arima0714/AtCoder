input_num = int(input())
input_line = input().split()
input_line = [int(s) for s in input_line]

counter = 0

while True:
    for k in input_line:
        if k % (2 ** counter) == False:
            break
        break
    break

print(counter-1)

print(input_num)
print(input_line)