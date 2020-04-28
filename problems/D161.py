K = int(input())

def check_runrun(number):
    num_str = str(number)
    ans = True
    if(len(num_str) == 1):
        return ans
    else:
        for i in range(len(num_str)-1):
            if(abs(int(num_str[i]) - int(num_str[i+1])) > 1):
                ans = False
                break
        return ans

print(check_runrun(K))
