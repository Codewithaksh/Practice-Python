n = [1,2,3,4,4,5,5,7,5,9,10]
m = [10,111,23,2,3,4,5,9,45]

for num in m:
    count = 0
    for x in n:
        if x==num:
            count+=1
    print(count)