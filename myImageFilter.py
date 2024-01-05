import numpy as np
def myImageFilter(img0, h):
    addSize=np.shape(h)[0]
    addSize//=2
    enlarge=[addSize]
    extra=np.pad(img0,enlarge,'edge')
    newM=np.zeros((np.shape(img0)[0],np.shape(img0)[1]))
    for row in range(np.shape(newM)[0]):
        for col in range(np.shape(newM)[1]):
            mul=np.multiply(h,extra[row:row+len(h),col:col+len(h)])
            newM[row][col]=np.sum(mul)
    return newM