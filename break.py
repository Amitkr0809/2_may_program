for i in range(1,10):
    if i > 5:
        break
    else:
        print(i)


for num in range(10):
    if num < 5:
        continue
    elif num > 8:
        break
    print(num, end = " ")