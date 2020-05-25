il1 = input().split()
il2 = input().split()
il1 = [int(s) for s in il1]
il2 = [int(s) for s in il2]
ans = 0

sum_vote = sum(il2)

for i in il2:
    if(i < sum_vote/(4*il1[1])):
        pass
    else:
        ans = ans + 1
    
if ( ans >= il1[1]):
    print("Yes")
else:
    print("No")
