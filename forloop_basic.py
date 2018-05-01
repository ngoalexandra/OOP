# # biggie size
def positivesToStr(arr):
    for i in range(len(arr)):
        num = arr[i]
        if (num > 0):
            num == "big"
    return arr
    
print(positivesToStr([1,3,-1,-2,-3,10]))

# # count positives

def countPositives(arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            count = count + 1
    arr[len(arr)-1] == count
    return arr
print(countPositives([-1,1,1,1]))

# sum total
def totalSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
print(totalSum([1,2,3,4]))

# average
def getAvg(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    return avg
print(getAvg([1,2,3,4]))

#length
def length(arr):
    lengthOfArr = 0
    for i in range(len(arr)):
        lengthOfArr += 1
    return lengthOfArr
print(length([1,2,3,4]))

#min

def minimum(arr):
    min = arr[0]
    if (arr == []):
        return false
    for i in range(len(arr)):
        if(arr[i] < min):
            min = arr[i]
    return min
print(minimum([1,2,3,4]))
print(minimum([-1,-2,-3]))
        
# max 

def maximum(arr):
    max = arr[0]
    if (arr == []):
        return false
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max
print(maximum([1,2,3,4,5]))

# minmaxavg
def minMaxAvg(arr):
    min = arr[0]
    max = arr[0]
    sum = 0

    for i in range(len(arr)):
        if (arr[i]> max):
            max = arr[i]
        if (arr[i]< min):
            min = arr[i]
        sum += arr[i]
    avg = sum / len(arr)
    return [min, max, avg]
print(minMaxAvg([1,2,3,4]))

#reverse arr
def reverse(arr):
    end = len(arr) -1
    limit = int(end/2) + 1
    for i in range(limit):
        arr[i], arr[end] = arr[end], arr[i]
        end -= 1
    return arr
print(reverse([1,2,3,4,5,6]))






