my_list = list(range(0,50))

for x in my_list:
    if x == 13:
        continue
    elif x == 39:
        break
    else:
        print(x)
