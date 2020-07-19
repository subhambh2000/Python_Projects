import re

fh = open('regex_sum_490405.txt')
s = 0
for line in fh:
    a = re.findall('([0-9]+)',line)
    if len(a) == 0:
        continue
    print(a)
    s = sum([int(i) for i in a],s)
    # start = sum(s,start)
print(s)
