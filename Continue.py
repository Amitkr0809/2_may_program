for i in range (1,10):
    if i == 5:
        continue
    else:
        print(i)



numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i % 2 == 0:
        continue
    print (i ** 2, end=" ")