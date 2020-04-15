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
        print("last word is dream")
        S = S[0:len(S)-len(dream)]
    elif(S[-1] == "e" and S[-5:] == erase):
        print("last word is erase")
        S = S[0:len(S)-len(erase)]
    elif(S[-3:] == "ser" and S[-6:] == eraser):
        print("last word is eraser")
        S = S[0:len(S)-len(eraser)]
    elif(S[-3:] == "mer" and S[-7:] == dreamer):
        print("last word is dreamer")
        S = S[0:len(S)-len(dreamer)]
    elif(len(S) != 0):
        answer = "NO"
        loop = False
        break

print(answer)
