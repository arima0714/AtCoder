# 入力は一行のみで[文字列]

S = input()

dream = "dream"
dreamer = "dreamer"
erase = "erase"
eraser = "eraser"

loop = True

answer = "YES"

while loop == True:
    if(len(S) == 0):
        break
    if(S[-1] == "m" and S[-5:] == dream):
        S = S[0:len(S)-len(dream)]
    elif(S[-1] == "e" and S[-5:] == erase):
        S = S[0:len(S)-len(erase)]
    elif(S[-3:] == "ser" and S[-6:] == eraser):
        S = S[0:len(S)-len(eraser)]
    elif(S[-3:] == "mer" and S[-7:] == dreamer):
        S = S[0:len(S)-len(dreamer)]
    elif(len(S) != 0):
        answer = "NO"
        loop = False
        break

print(answer)
