#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:59:51 2018

@author: hhshhd
"""
import random
whole = []
person = '  '
n = int(input('line:'))
for i in range(n-1):
    for j in range (n-2):
        person = random.choice('OX ')
        print(' '+person+' |',end='')
        whole.append(person+str(i)+str(j))
    person = random.choice('OX ')
    print(' '+person+' |',end='')
    whole.append(person+str(i)+str(j+1))
    person = random.choice('OX ')
    print(' '+person+' |')
    whole.append(person+str(i)+str(j+2))
    print('---',end='')
    for k in range(n-1):
        print('----',end='')
    print('')
for q in range (n-1):
    person = random.choice('OX ')
    print(' '+person+' |',end='')
    whole.append(person+str(n-1)+str(q))
person = random.choice('OX ')
print(' '+person+' |')
whole.append(person+str(q+1)+str(j+2))
def algorithm():
    for q in range(len(whole)):
        count = 0
        space = []
        alot = []
        lot = []
        if q == 0:
            alot.extend([whole[0][0],whole[1][0],whole[n][0],whole[n+1][0]])
            lot.extend([whole[0],whole[1],whole[n],whole[n+1]])
        elif 0<q<n-1:
            alot.extend([whole[q-1][0],whole[q][0],whole[q+1][0],whole[q+n-1][0],whole[q+n][0],whole[q+n+1][0]])
            lot.extend([whole[q-1],whole[q],whole[q+1],whole[q+n-1],whole[q+n],whole[q+n+1]])
        elif q == n-1:
            alot.extend([whole[q-1][0],whole[q][0],whole[q+n-1][0],whole[q+n][0]])
            lot.extend([whole[q-1],whole[q],whole[q+n-1],whole[q+n]])
        elif q == len(whole)-n:
            alot.extend([whole[q-n][0],whole[q-n+1][0],whole[q][0],whole[q+1][0]])
            lot.extend([whole[q-n],whole[q-n+1],whole[q],whole[q+1]])
        elif q%n == 0:
            alot.extend([whole[q-n][0],whole[q-n+1][0],whole[q][0],whole[q+1][0]])
            lot.extend([whole[q-n],whole[q-n+1],whole[q],whole[q+1],whole[q+n],whole[q+n+1]])
        elif q == len(whole)-1:
            alot.extend([whole[q-n-1][0],whole[q-n][0],whole[q-1][0],whole[q][0]])
            lot.extend([whole[q-n-1],whole[q-n],whole[q-1],whole[q]])
        elif q%n == n-1:
            alot.extend([whole[q-n-1][0],whole[q-n][0],whole[q-1][0],whole[q][0]])
            lot.extend([whole[q-n-1],whole[q-n],whole[q-1],whole[q],whole[q+n-1],whole[q+n]])
        elif len(whole)-n<q<len(whole)-1:
            alot.extend([whole[q-n-1][0],whole[q-n][0],whole[q-1][0],whole[q][0]])
            lot.extend([whole[q-n-1],whole[q-n],whole[q-n+1],whole[q-1],whole[q],whole[q+1]])
        else:
            alot.extend([whole[q-n-1][0],whole[q-n][0],whole[q-n+1][0],whole[q-1][0],whole[q][0],whole[q+1][0],whole[q+n-1][0],whole[q+n+1][0]])
            lot.extend([whole[q-n-1],whole[q-n],whole[q-n+1],whole[q-1],whole[q],whole[q+1],whole[q+n-1],whole[q+n],whole[q+n+1]])
        test = whole[q][0]
        test1 = whole[q]
        if test == 'X' or test == 'O':
            for m in range(len(alot)):
                if alot[m] == test:
                    count+=1
                elif alot[m] == ' ':
                    space.append(m)
            if space ==[]:
                continue
            elif count/(len(alot)-len(space)) >= 0.5 :
                continue
            else:

                temp = test1
                whole[q] = ' '+whole[q][1:]
                p = random.choice(space)
                for i in range(len(whole)):
                    if whole[i] == lot[p]:
                        whole[i] = temp
                whole[q] = ' '+whole[q][1:]

    print('!')      
    for i in range(len(whole)):
        print(' '+whole[i][0]+' |',end='')   
        if (i+1)%(n) == 0 :
            print('')
            for k in range(n):
                print('----',end='')
            print('')
algorithm()
algorithm()
algorithm()
algorithm()
algorithm()
