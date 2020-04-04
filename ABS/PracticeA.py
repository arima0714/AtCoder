line_1 = input()
tmp_str = input()
line_2 = tmp_str.split()
line_3 = input()

integer = int(line_1) + int(line_2[0])+ int(line_2[1])
string  = line_3

print("%d %s" % (integer, string))
