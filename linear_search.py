list=[1,5,9,4,5,6,7,8,2,10,12]
target=10

def linear(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return target
    print("not found")


result=linear(list,target)
print(result)
