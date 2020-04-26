S = input()
N = len(S)
print(N)

def plindrome_checker(strings):
    result = True
    length = len(strings)
    for k in range(length):
        print("strings[k] = "+strings[k]+" , strings[-1 * k] = "+strings[length-1-k])
        if (strings[k] == strings[length-1-k]):
            pass
        else:
            result = False
    return result

str1 = plindrome_checker(S[0:(N-1)//2])
str2 = plindrome_checker(S[(N-1)//2+1:])
print("str1 = " + str(str1))
print("str2 = " + str(str2))

if(str1 and str2):
    print("Yes")
else:
    print("No")
