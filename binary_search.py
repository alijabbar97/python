list=[1,5,9,4,5,6,7,8,2,10,12]
target=9
def binary(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        mid=(last+first)//2
        if mid==target:
            return target
        elif mid<target:
            first=mid+1
        else:
            first=mid-1


result=binary(list,target)
print(result)
