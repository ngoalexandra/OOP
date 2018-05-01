# # countdown 
def countdown(num):
    newarr = []
    for i in range(num, 0-1, -1):
        newarr.append(i)
    return newarr
print(countdown(10))

# print and return
def printAndReturn(arr):
   for i in range(len(arr)):
       print(arr[0])
       lastVal = len(arr) -1
    return lastVal
print(printAndReturn([1,5]))

# def firstPlus(arr):
    sum = 0
    for i in range(len(arr)):
        sum = arr[0] + len(arr)
    return sum
print(firstPlus([1,2,3,4,5]))
print(firstPlus([10,33,43,50]))

#  values greater than second
def greaterThan(arr):
    newarr = []
    count = 0
    if (len(arr) < 2):
        return false
    for i in range(len(arr)):
        if(arr[i] > arr[1]):
            count += 1
            print(count)
            newarr.append(arr[i])
    return newarr
    
print(greaterThan([2,3,5,6]))

# this length, that value
def lengthAndVal(num1, num2):
    arr = []
    if(num1 == num2):
        return "Jinx"
    for i in range(0, num1, +1):
        arr.append(num2)
    return arr
print(lengthAndVal(4,3))
    
       
        



