import numpy as np
import math
def myHoughTransform(Im, rhoRes, thetaRes):
    h=np.shape(Im)[0]
    w=np.shape(Im)[1]
    h_c,w_c=np.square(h),np.square(w)
    count,pi=np.sqrt(h_c+w_c),2*math.pi
    scaleR,scaleT=np.arange(0,count,rhoRes),np.arange(0,pi,thetaRes)
    sR,sT=count/rhoRes,pi/thetaRes
    initial=np.zeros((int(np.ceil(sR)),int(np.ceil(sT))))
    for r in range(h):
        for c in range(w):
            if Im[r][c]!= 0:
                for ind in range(int(np.ceil(sT))):
                    get=(math.sin(thetaRes*ind)*r)+(math.cos(thetaRes*ind)*c)
                    i=int(round(get/rhoRes) ) 
                    if 0<=i<np.shape(initial)[0]:
                        initial[i][ind]=1+initial[i][ind]
    return initial,scaleR,scaleT


