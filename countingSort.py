

def countingSort(a):
    print(a)
    numMax = max(a)                    # to find the highest 
    numMin = min(a)                     # find lowest 
    arr = [*range(numMin,numMax+1)]     # reference index for countArr array starting index numMin to numMax
    #print(arr)
    countArr = [0] * len(arr)           # count array 
    for i in range(len(a)):
        for j in range(len(arr)):        
            if a[i] == arr[j]:             
                countArr[j] = a.count(a[i])   
    #print(countArr)

    for i in range(1,len(countArr)):
        countArr[i] = countArr[i] + countArr[i-1]
    #print(countArr)

    Refarr = [*range(1,len(a)+1)]               # reference  index for newArr array (range depends on input)
    newArr = [0] * len(Refarr)
    for i in range(0,len(a)):
        for j in range(0,len(arr)):
            if a[i] == arr[j]:                # check wetheerr user input is equal to reference index
                for k in range(0,len(a)):
                    if countArr[j] == Refarr[k]:   # check countArray is equal to reference index
                        newArr[k] = a[i]            
                        countArr[j] = countArr[j]-1
    print(newArr)
    #print(len(newArr))
    #print(len(a))
                

arr = [4,13,33,14,3]

countingSort(arr)