n = [1,2,3,4,4,5,5,7,5,9,10]
m = [10,111,23,2,3,4,5,9,45]

hash_list = [0]*12
for num in n:
    hash_list[num]+=1

for num in m:
    if num<1 or num>12:
        print(0)
    
    else:
        print(hash_list[num])