il = input().split()
N = int(il[0])
K = int(il[1])
T = N
# 整数NをK進数に変換し、その桁数を出力する

result = ""

i = 0
k = 0
while (T != 0):
    result = str(T%K)+result
    T = T//K

print (len(result))
