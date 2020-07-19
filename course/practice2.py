# Opening of file
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    fh = open('mbox-short.txt')

# Average spam confidence
# pos = line.find(' ')
# nm = nm + float(line[pos+1:])
# count = count + 1
# nm = nm/count
# print('Average spam confidence:',round(nm,12))
# words = list()
# for line in fh:
#     etc = line.split()
#     for i in etc:
#         if i not in words:
#             words.append(i)
# words.sort()
# print(words)

# Number of emails
# count = dict()
# for line in fh:
#     if not line.startswith("From "):
#         continue
#     else:
#         etc = line.split()
#         count[etc[1]] = count.get(etc[1],0) + 1
# email = None
# emailCount = None
# for word,cnt in count.items():
#     if emailCount is None or emailCount < cnt:
#         email = word
#         emailCount = cnt
# # for i in count.keys():
# #     print(count[i],end=" ")
# print(email,emailCount)

# Sorting the distribution by hour
count = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        etc = line.split()
        hour = etc[5].split(':')
        count[hour[0]] = count.get(hour[0],0) + 1
hr = list(sorted([(v,k) for v,k in count.items()]))
# print(hr)
for h,c in hr:
    print(h,c)
