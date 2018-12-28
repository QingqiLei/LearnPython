import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
b =  a.shape # return the shape of the ndarray as a tuple
print(type(b)) # a tuple
print(a.ndim) # return the numbers of axes, 返回维度
print(a.dtype.name) #the type of elements in the ndarray, 数组中的元素类型
print(a.itemsize) # return the bytes of a element
print(type(a))
print(a.size) # return the numbers of elements == multipity of returns of shape()
""" slice"""
B = np.array([1,2,3,4]).reshape(2,2)
print(B[0:1]) # row range
print(B[:,0:1]) # column range
print(B[0:1,0:1]) # row range and column range
print(B[1:]) # one row
''' np.exp()'''
B = np.array([1,2,3,4])
bwxp = np.exp(B) # e with the power of n
print(bwxp)
''' common calculation '''
x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.array([[1,6],[7,8]], dtype = np.float64)
print(x[0:1]) # row
print(x[:,0:])
print(x[:,:-1])
print(x[:,-1:])
print(x + y) # must have the same shape
print(x - y)
print(x*y)
print(x/y)
print(x.dot(y)) #????????????

''' broadcast'''
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([10,0,10])
t = x + y
print(t)
'''random'''
ran = np.random.rand(4,4)
ran
ran **10
1/ran
np.cov(ran)
np.corrcoef(ran)
ran[:,0] # first column
