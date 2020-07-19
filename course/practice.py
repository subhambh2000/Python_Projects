highest = None
smallest = None
while True:
    num = input('Enter number: ')
    if num == "done":
        break
    # noinspection PyBroadException
    try:
        fval = int(num)
    except:
        print('Invalid Input')
        continue
    if highest is None and smallest is None:
        highest = fval
        smallest = fval
    elif highest < fval:
        highest = fval
    else:
        if smallest > fval:
            smallest = fval
print('Maximum', highest)
print('Minimum',smallest)
# # print("Done!!")



