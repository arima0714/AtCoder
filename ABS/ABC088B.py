# １行目 [数値]
# ２行目 [数値1 数値2 数値3 ...] のように１行目の個数分だけ数値が入力される

input_number = input()
input_line   = list(input().split())
input_line = [int(s) for s in input_line]
input_line.sort(reverse=True)



print(input_line)