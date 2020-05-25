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

def return_result(input_k):
    i = 0
    tmp = 1
    while tmp <= input_k:
        i = i + 1
        if (check_runrun(i)):
            # print("tmp = "+str(tmp) + " i = " +str(i))
            tmp = tmp + 1
    return i


print(return_result(K))
