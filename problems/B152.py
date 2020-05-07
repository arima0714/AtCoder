il = input().split()
a = il[0]
b = il[1]

a_fixed = a * int(b)
b_fixed = b * int(a)

result = [a_fixed , b_fixed]
result.sort()

print(result[0])
