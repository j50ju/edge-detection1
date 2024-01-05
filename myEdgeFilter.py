import numpy as np
import math
from scipy import signal
from myImageFilter import myImageFilter

def myEdgeFilter(img0, sigma):
    h=int(2*(math.ceil(3*sigma))+1)
    get=signal.gaussian(h,sigma)
    gaus=np.matmul(get.reshape(-1,1),get.reshape(1,h))
    nor=np.sum(gaus)
    normal=gaus/nor
    smooth=myImageFilter(img0,normal)
    kH,kV=[[1,0,-1],[2,0,-2],[1,0,-1]],[[1,2,1],[0,0,0],[-1,-2,-1]]
    filteredR,filteredC=myImageFilter(smooth,np.array(kH)),myImageFilter(smooth,np.array(kV))
    calR,calC=np.square(filteredR),np.square(filteredC)
    mag=np.sqrt(calR+calC)
    gra=np.arctan2(filteredC,filteredR)
    final=nms(mag,gra)
    return final
def nms(mag,gra):
    res2=np.copy(mag)
    for row in range(1,np.shape(mag)[0]-1):
        for col in range(1,np.shape(mag)[1]-1):
            gra[row][col]=gra[row][col]%(2*np.pi)
            if 0<=gra[row][col]<np.pi/8: 
                if not(mag[row][col]>mag[row][col+1] and mag[row][col]>mag[row][col-1]):
                    res2[row][col]=0
            elif 7*np.pi/8<=gra[row][col]<=2*np.pi:
                if not(mag[row][col]>mag[row][col+1] and mag[row][col]>mag[row][col-1]):
                    res2[row][col]=0
            elif 1*np.pi/8<=gra[row][col]<3*np.pi/8:
                if not(mag[row][col]>mag[row+1][col+1] and mag[row][col]>mag[row-1][col-1]):
                    res2[row][col]=0
            elif 5*np.pi/8<=gra[row][col]<7*np.pi/8:
                if not(mag[row][col]>mag[row+1][col-1] and mag[row][col]>mag[row-1][col+1]):
                    res2[row][col]=0
            elif 3*np.pi/8<=gra[row][col]<5*np.pi/8:
                if not(mag[row][col]>mag[row+1][col] and mag[row][col]>mag[row-1][col]):
                    res2[row][col]=0
    return res2
