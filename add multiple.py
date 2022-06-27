from unittest import result


def sum(*a):
    result=0
    for i in a:
        result=result+i
    return result

res=sum(1,2,3)
print(res)