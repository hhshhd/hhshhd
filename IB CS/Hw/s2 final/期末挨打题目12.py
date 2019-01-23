import random
length = int(input("length:"))
array = []
for i in range(length):
    array.append([])
    for j in range(length):
        array[i].append(random.randint(0,5))
# array = [[7,0,0,0,0,0],[0,0,0,0,0,0],[0,0,-3,0,9,0],[0,0,0,0,0,0],[0,0,-1,0,0,0],[0,-6,0,0,-5,1]]
# length = 6
for i in range(length):
    print(array[i])
count = 0
values=[]
rowc=[]
col=[]
for i in range(length):
    for j in range(length):
        if array[i][j]!=0:
            values.append(array[i][j])
            col.append(j)
            count += 1
    rowc.append(count)
print('values:',values)
print('rowc:',rowc)
print('col:',col)
