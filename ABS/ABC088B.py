input_number = input()
input_line   = list(input().split())
input_line = [int(s) for s in input_line]
input_line.sort(reverse=True)

print(input_line)