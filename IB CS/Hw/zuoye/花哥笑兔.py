import matplotlib.pyplot as p
import numpy
import time
import itertools

def insertion_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(i):
            print(a[i],a[j])
            if a[i]<a[j]:
                a.insert(j,a.pop(i))
                print(a)
                break
    return a

def selection_sort(list):
    
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        temp=list[i]
        list[i]=list[min]
        list[min]=temp
    return list

def bubblesort(a):
    for i in range(len(a)):
        for j in range(i):
            if a[i]<a[j]:
                a[i],a[j]=a[j],[i]

def alg(c,b):
    result=[]
    while len(c) and len(b):
        if c[0]<=b[0]:
            result.append(c.pop(0))
        elif b[0]<=c[0]:
            result.append(b.pop(0))
    if len(c)!=0:
        result+=a
    elif len(b)!=0:
        result+=b
    return result
        
    
def merge_sort(a):
    if len(a)==1:
        return a
    mid=len(a)//2
    a=merge_sort(a[:mid])
    b=merge_sort(a[mid:])
    return alg(c,b)

def timing(f,l):
    a=list(numpy.random.random_sample(l))
    start=time.clock()
    f(a)
    end=time.clock()
    return end-start

def drawing():
    f=open("times.txt","w")
    fig=p.figure()
    fig.suptitle('Running time for four sorting alg')
    num=itertools.count(0,1000)
    ts=itertools.takewhile(lambda x: x<=10000,num)
    x=[2000,4000,6000,8000,10000]
    data=[[],[],[],[]]
    for i in ts:
        data[0].append(timing(insertion_sort,i))
        data[1].append(timing(selection_sort,i))
        data[2].append(timing(bubble_sort,i))
        data[3].append(timing(merge_sort,i))
    l1,=p.plot(x,data[0],color="red",label="insection")
    l2,=p.plot(x,data[1],color="black",label="selection")
    l3,=p.plot(x,data[2],color="grey",label="bubble")
    l4,=p.plot(x,data[3],color="pink",label="merge")
