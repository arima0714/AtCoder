N = int(input())

inputs = []

for i in range(N):
    input_line = input().split()
    input_line = [int(s) for s in input_line]
    inputs.append(input_line)
    print(input_line)

