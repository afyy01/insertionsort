
#insertion sort
#time complexity: 0(n&2)

mylist=[12,7,1,3,9,10]

for i in range(0, len(mylist)):
    minElement = 1000000 #minimum
    minLocation = -1
    for j in range(i, len(mylist)):
        if minElement>mylist[j]:
            minElement = mylist[j]
            minLocation = j
            mylist[i],mylist[j] = mylist[j], mylist[i]
print(mylist)
