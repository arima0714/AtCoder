N = int(input())

inputs = []
t = 0
x = 0
y = 0
answer = "Yes"

for i in range(N):
    input_line = input().split()
    input_line = [int(s) for s in input_line]
    t = input_line[0]
    x = input_line[1]
    y = input_line[2]
    inputs.append(input_line)
    if ( t < x + y):
        print("No -> t < x + y")
        answer = "No"
    elif ( (x+y)%2 != t%2):
        print("No -> (x+y)%2 != t%2")
        answer = "No"
    else:
        pass    # YES

print(answer)
