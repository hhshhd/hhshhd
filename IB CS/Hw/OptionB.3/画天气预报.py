import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

import math

def Gauss(k):
    
    x=np.linspace(-10,10,1000)
    
    y=np.linspace(-10,10,1000)
    
    X,Y=np.meshgrid(x,y)
    
    var = 3
    
    Z = (1/(2*math.pi*var**2))*np.exp(-(X**2+Y**2)/(2*var**2))


    fig=plt.figure()
    
    ax=fig.gca(projection='3d')
    
    ax.plot_wireframe(X,Y,Z,color='k', rcount=25,ccount=25) if k==0 else ax.plot_surface(X,Y,Z,cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)

    plt.show()

def Ball_3D(k):
    
    C = [0,0,0]
    
    R = 10

    u = np.linspace(0, 2 * np.pi, 1000)
    
    v = np.linspace(0, np.pi, 1000)
    
    X = R * np.outer(np.cos(u), np.sin(v)) + C[0]
    
    Y = R * np.outer(np.sin(u), np.sin(v)) + C[1]
    
    Z = R * np.outer(np.ones(np.size(u)), np.cos(v)) + C[2]

    fig=plt.figure()
    
    ax=fig.gca(projection='3d')
    
    ax.plot_wireframe(X,Y,Z,color='k', rcount=25,ccount=25) if k==0 else ax.plot_surface(X,Y,Z,cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)

    plt.show()


def CO2(k):
    
    x=np.linspace(0,10,100)
    
    y=np.linspace(0,10,100)
    
    X,Y=np.meshgrid(x,y)
    
    R = np.sqrt(X**1.7 + Y**0.7)
    
    Z = np.cos(R) 

    fig=plt.figure()
    
    ax=fig.gca(projection='3d')
    
    ax.plot_wireframe(X,Y,Z,color='k', rcount=25,ccount=25) if k==0 else ax.plot_surface(X,Y,Z,cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)

    plt.show()

CO2(1)
