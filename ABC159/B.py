S = input()
print(S[0]+S[-1])
N = len(S)
print(N)

def plindrome_checker(strings):
    result = True
    length = len(strings)
    for k in range(length):
        if (strings[k] == strings[-1 * k]):
            pass
        else:
            result = False
    return result


