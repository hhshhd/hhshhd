import matplotlib.pyplot as mpl
import time

def insertion_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i):
#            print(alist[i],alist[j])
            if alist[i] < alist[j]:
                alist.insert(j,alist.pop(i))
#                print(alist)
                break
    return alist

def selection_sort(blist):
    n = len(blist)
    for i in range(n):
        min_ = i
        for j in range(i+1,n):
            if blist[j] < blist[min_]:
                min_ = j
        temp = blist[i]
        blist[i] = blist[min_]
        blist[min_] = temp
    return blist

def bubble_sort(clist):
    n = len(clist)
    for i in range(n):
        for j in range(i):
            if clist[i] < clist[j]:
                clist[i],clist[j] = clist[j],clist[i]
    return clist

def merge_sort_part2(lef,righ):
    result = []
    temp = Temp = 0
    while Temp < len(lef) and temp < len(righ):
        if lef[Temp] < righ[temp]:
            result.append(lef[Temp])
            Temp += 1
        else:
            result.append(righ[temp])
            temp += 1

    if Temp == len(lef):
        for i in righ[temp:]:
            result.append(i)
    else:
        for i in lef[Temp:]:
            result.append(i)

    return result
        
    
def merge_sort_part1(dlist):
    n = len(dlist)
    if n <= 1:
        return dlist
    mid = n//2
    left = merge_sort_part1(dlist[:mid])
    right = merge_sort_part1(dlist[mid:])
    return merge_sort_part2(left,right)

def quick_sort(elist):
   quickSortRecursion(elist,0,len(elist)-1)

def quickSortRecursion(elist,first,last):
   if first<last:

       splitpoint = partition(elist,first,last)

       quickSortRecursion(elist,first,splitpoint-1)
       quickSortRecursion(elist,splitpoint+1,last)


def partition(elist,first,last):
   pivotvalue = elist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and elist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while elist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = elist[leftmark]
           elist[leftmark] = elist[rightmark]
           elist[rightmark] = temp

   temp = elist[first]
   elist[first] = elist[rightmark]
   elist[rightmark] = temp


   return rightmark

def speedTest(n):
    timeList = []
    lengthList = [i for i in range(1000,6000,200)]
    for i in lengthList:
        temp = [j for j in range(i,0,-1)]
        #shuffle(temp)
        start = time.clock()
        n(temp)
        end = time.clock()
        timeList.append(end-start)
    return timeList

def illustrate():
    func = [selection_sort,bubble_sort,insertion_sort,merge_sort_part1,quick_sort]
    funcName = ['selectSort','bubbleSort','insertSort','mergeSort','quick_sort']
    for i in range(5):
        mpl.plot([i for i in range(1000,6000,200)],speedTest(func[i]), label = funcName[i])
    mpl.xlabel('length of step list')
    mpl.ylabel('running time(s)')
    mpl.legend()
    mpl.show()

a = illustrate()
a
#def timing(f,l):
#    a=list(numpy.random.random_sample(l))
#    start=time.clock()
#    f(a)
#    end=time.clock()
#    return end-start
#
#def drawing():
#    fig=mpl.figure()
#    fig.suptitle('Running time for four sorting alg')
#    num=itertools.count(0,1000)
#    ts=itertools.takewhile(lambda x: x<=10000,num)
#    x=[2000,4000,6000,8000,10000]
#    data=[[],[],[],[]]
#    for i in ts:
#        data[0].append(timing(insertion_sort,i))
#        data[1].append(timing(selection_sort,i))
#        data[2].append(timing(bubble_sort,i))
#        data[3].append(timing(merge_sort_part1,i))
#    l1,=mpl.plot(x,data[0],color="red",label="insection")
#    l2,=mpl.plot(x,data[1],color="black",label="selection")
#    l3,=mpl.plot(x,data[2],color="grey",label="bubble")
#    l4,=mpl.plot(x,data[3],color="pink",label="merge")