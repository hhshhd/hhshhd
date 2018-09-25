def reverse_file():
    '''
    Write a program that reads a file and writes out a new file with the lines in reversed order 
    (i.e. the first line in the old file becomes the last one in the new file.)
    '''
    reverse=open('reverse.txt','w')
    test=open('test.txt','r')
    a=test.readlines()
    for i in range(len(a)-1):
        b=a[-i-1]
        g.write(str(b))
    g.close()

def snake_file():
    '''
    Write a program that reads a file and prints only those lines that contain the substring 'snake'.
    '''
    snake=open('test.txt','r')
    a=snake.readlines()
    for i in a:
        if 'snake' in i:
            print(i)
    snake.close()

def num_file():
    '''
    Write a program that reads a text file and produces an output file which is a copy of the file,
    except the first five columns of each line contain a four digit line number, 
    followed by a space. Start numbering the first line in the output file at 1. 
    Ensure that every line number is formatted to the same width in the output file. 
    Use one of your Python programs as test data for this exercise: 
    your output should be a printed and numbered listing of the Python program.
    '''
    testnum=open('testnum.txt','w')
    test=open('test.txt','r')
    x=0001
    line=test.readlines()
    for i in line:
        x.write(str(x)+' '+i)
        x+=1
    testnum.close()
    
def renum_file():
    '''
    Write a program that undoes the numbering of the previous exercise:
    it should read a file with numbered lines and produce another file without line numbers.
    '''
    reducenum=open('reducenum.txt','w')
    test=open('testnum.txt','r')
    a=test.readlines()
    b=0
    for i in a:
        for j in i:
            while i.isdigit():
                b+=1
        reducenum.write(a[b:])
    reducenum.close()
    
