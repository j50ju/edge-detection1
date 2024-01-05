import numpy as np
from scipy.ndimage import maximum_filter
def myHoughLines(H, nLines):
    change=maximum_filter(H,(10,10))
    ind=np.argwhere((H==change))
    sind=np.array(sorted(ind,key=lambda x:H[x[0],x[1]],reverse=True))
    rhoValues=sind[:nLines,0]
    thetaValues=sind[:nLines,1]
    return rhoValues,thetaValues
