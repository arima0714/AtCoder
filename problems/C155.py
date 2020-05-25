N = int(input())

polls = {}
result = []

for k in range(N):
    S_k = input()
    if (S_k in polls):
        # 既に存在する場合 -> 値を+1
        polls[S_k] = str(int(polls[S_k]) + 1)
    else:
        # 存在していない場合 -> キーを新規作成し値を1にする
        polls[S_k] = "1"

max = 0
# 最大の値を取得する
for key in polls:
    if(max < int(polls[key])):
        max = int(polls[key])

for key in polls:
    if(max == int(polls[key])):
        result.append(key)

result.sort()
for ans in result:
    print(ans)
