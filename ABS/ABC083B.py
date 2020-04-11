input_line = input().split()

answer = 0

for i in range(int(input_line[0]) + 1) :
    tmp = 0
    for j in list(str(i)):
        tmp = tmp + int(j)
    if int(input_line[1]) <=  tmp <= int(input_line[2]) :
        print("tmp = ", i)
        answer = answer + i
        
print(answer)
