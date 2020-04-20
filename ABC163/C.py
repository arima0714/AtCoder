N = int(input())
il1 = input().split()
A = [int(i) for i in il1]

employee = list(A)
employee.append(0)

for i in range(N):
    employee[i] = 0

for i in A:
    employee[i-1] = employee[i-1] + 1

for i in employee:
    print(i)
