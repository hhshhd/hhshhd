import random
import matplotlib.pyplot as plt
import numpy as np
import time

class KMeans():

    def __init__(self, k=1):
        '''
        :param k: k represents classification
        '''
        self.__k = k
        self.__data = None         # Store raw data and convert to numpy type
        self.__pointCenter = None  # Store the center point, the first obtained center point is randomly randomized in __data, numpy type
        self.__result = []       # Store classification results
        for i in range(k):
            self.__result.append([])  # [[],[],[],[],[]]
            

    def fit(self, data, threshold, times=80):
        '''
        Model training
        :param data: training data
        :return:
        '''
        self.__data = data    #Get test data
        self.randomCenter()   #Get the centroid
        #print(self.__pointCenter)
        centerDistance = self.calPointCenterDistance(self.__pointCenter, self.__data)  
        #Calculate the distance between the center point and each point

        # Classify the raw data and assign each point to its nearest center
        i = 0
        for temp in centerDistance:
            index = np.argmin(temp)  
            self.__result[index].append(self.__data[i])  #sort
            i += 1
        # Print classification results
        # print(self.__result)
        oldCenterPoint = self.__pointCenter
        newCenterPoint = self.calNewPointCenter(self.__result)

        while np.sum(np.sum((oldCenterPoint -  newCenterPoint)**2, axis=1)**0.5)/self.__k > threshold:
        #Judging the difference between the old and new center points
            times -= 1
            result = []
            for i in range(self.__k):
                result.append([])
            # Save the last center point
            oldCenterPoint = newCenterPoint
            centerDistance = self.calPointCenterDistance(newCenterPoint, self.__data)

            # Classify the raw data and assign each point to its nearest center
            i = 0
            for temp in centerDistance:
                index = np.argmin(temp)
                result[index].append(self.__data[i]) 
                i += 1

            newCenterPoint = self.calNewPointCenter(result)

            self.__result = result
        self.__pointCenter = newCenterPoint
        return newCenterPoint, self.__result
        
	#Calculate the distance between the center point and each point
    def calPointCenterDistance(self, center, data):
        centerDistance = []
        flag = False
        for temp in data:
            centerDistance.append([np.sum((center - temp) ** 2, axis=1) ** 0.5])#使用numpy广播
            pass
        # print(centerDistance)
        return np.array(centerDistance)
        pass

    def calNewPointCenter(self, result):
        '''
        Calculate the new center point
        '''
        newCenterPoint = None
        flag = False
        for temp in result:
            temps = np.array(temp)  #Change to numpy type
            point = np.mean(temps, axis=0)   #Find the average value, axis=0, then average the row axis
            if not flag:
                newCenterPoint = np.array([point])
                flag = True
                pass
            else:
                newCenterPoint = np.vstack((newCenterPoint, point))  #Add the generated center point
            pass
        # print(newCenterPoint)
        return newCenterPoint
        pass

    def randomCenter(self):

        if not self.__pointCenter:
            index = random.randint(0, len(self.__data) - 1)  #Generate random numbers
            self.__pointCenter = np.array([self.__data[index]])  #Generate the first center point
            pass

        while len(self.__pointCenter) < self.__k:
            # Random index
            index = random.randint(0, len(self.__data) - 1)
            # Determine if the center point is duplicated, if not, add the center point list
            if self.__data[index] not in self.__pointCenter:
                self.__pointCenter = np.vstack((self.__pointCenter, self.__data[index]))
                #self.__pointCenter There must be a value, the np.vstack method will add a new element, otherwise a syntax error

if __name__ == "__main__":
    data = np.random.randint(0, 100, 200000).reshape(100000, 2)
    # print(data)
    startTime = time.time()
    kmeans = KMeans(k=5)
    centerPoint, result = kmeans.fit(data, 0.0001)
    print(time.time() - startTime)
    print(centerPoint)
    plt.plot()
    plt.title("KMeans Classification")
    i = 0
    tempx = []
    tempy = []
    color = []
    for temp in result:
        temps = [[temp[x][i] for x in range(len(temp))] for i in range(len(temp[0]))]
        color += [i] * len(temps[0])
        tempx += temps[0]
        tempy += temps[1]

        i += 2
    plt.scatter(tempx, tempy, c=color, s=30)
    plt.show()
