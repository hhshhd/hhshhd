def TestOne(K=3,P=1):
    while K > 1 :
        print (K) # here we cannot use return coz if we use return the function is done
        K -= 1
        P *= K
    return(P)

class DDL(): # Double Dimensional lists (arrays)
    ''' Test on 31/Oct/2018 '''
    def __init__(self, n=7):
        self.n = n
    def check(self, array=[[17,24,1,8,15],
                           [23,5,7,14,16],
                           [4,6,13,20,22],
                           [10,12,19,21,3],
                           [11,18,25,2,9]]):
        ''' check whether the array is suitable to
            the algorithm(sum of each line and row
            is same) is true or not.
        '''
        temp = 0
        m = len(array)
        for k in range(m):
            temp += array[0][k]
        sum_ = temp
        sum__ = temp
        for i in range(m):
            if sum_ != temp or sum__ != temp :
                print('laji')
            else :
                sum_ = 0
                sum__ = 0
            for j in range(m):
                sum_ += array[i][j]
                sum__ += array[j][i]
        print ('good')
    def create(self):
        ''' create an array which is suitable to
            the algorithm(each sum of the line
            and row is same).
        '''
        z = 1
        t = 0
        temp = 0
        a = [0] * self.n
        for i in range(self.n):
            a[i] = [0] * self.n
        for j in range(self.n//2,self.n+self.n//2):
            for i in range(self.n,0,-1):
        ##        if z < 10:
        ##            z = float(z)
        ##        else:
        ##            z = int(z)
                a[(i+2*t)%self.n][(j-2*t)%self.n] = z
                z += 1
                j += 1
                temp += 1
                if temp == self.n:
                    t +=1
                    temp = 0
        for row in a:
            print(' '.join([str(elem) for elem in row]))

test = DDL(9)
test.check()
test.create()
