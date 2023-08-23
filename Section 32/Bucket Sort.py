import math




def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in customList:
        index_b = math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b -1].append(j)

    for i in range( numberOfBuckets):
        arr[i]= sorted(arr[i])

    k = 0

    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList



cl = [2,3,5,4,1,7,6,9,8,10,11,12,20]

print(bucketSort(cl))

    