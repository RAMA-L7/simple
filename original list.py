from re import A


a=[1,2,2,3,3,4,5,6,7,8,6,7,4,8,9]
print(a)
a=list(set(a))
print(a)
from re import A


a=[1,1,1,1,2,2,3,3,4,5,6,7,8,6,7,4,8,9]
print(a)
a=max(list(a),key=a.count)
print(a)