S = input()
N = len(S)

def plindrome_checker(strings):
    result = True
    length = len(strings)
    for k in range(length):
        if (strings[k] == strings[length-1-k]):
            pass
        else:
            result = False
    return result

str1 = plindrome_checker(S[0:(N-1)//2])
str2 = plindrome_checker(S[(N-1)//2+1:])

if(str1 and str2):
    print("Yes")
else:
    print("No")
