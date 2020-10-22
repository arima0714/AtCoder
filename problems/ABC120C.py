S = input()

tmp_s = S
result = 0
while(("01") in tmp_s):
    index = tmp_s.find("01")
    # print(f'index = {index}, tmp_s = {tmp_s}')
    if(index != 0 and index+2 != len(tmp_s)):
        tmp_s = tmp_s[:index] + tmp_s[index+2:]
    elif(index == 0 and index+2 == len(tmp_s)):
        tmp_s = ""
    elif(index == 0):
        tmp_s = tmp_s[index+2:]
    elif(index+2 == len(tmp_s)):
        tmp_s = tmp_s[:index]
    result = result + 2
while(("10") in tmp_s):
    index = tmp_s.find("10")
    # print(f'index = {index}, tmp_s = {tmp_s}')
    if(index != 0 and index+2 != len(tmp_s)):
        tmp_s = tmp_s[:index] + tmp_s[index+2:]
    elif(index == 0 and index+2 == len(tmp_s)):
        tmp_s = ""
    elif(index == 0):
        tmp_s = tmp_s[index+2:]
    elif(index+2 == len(tmp_s)):
        tmp_s = tmp_s[:index]
    result = result + 2

print(result)