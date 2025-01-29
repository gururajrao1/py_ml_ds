import numpy as np

arr= np.array([[0,1,2],[3,5,6]],
dtype=np.float32)
print(repr(arr))

arr=np.array([0,0.1,2])
print(repr(arr))

a=np.array([0,1])
b=np.array([9,8])

c=a
print('array a:{}'.format(repr(a)))

c[0]=5
print('array a:{}'.format(repr(a)))

d=b.copy()
d[0]=6
print('array b:{}'.format(repr(b)))

ar1= np.array([0,1,2])
print(ar1.dtype)
ar2=ar1.astype(np.float32)
print(ar2.dtype)

arr=np.array([np.nan,1,2])