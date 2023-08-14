def insertionSort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j>=0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    print(custom_list)



cl = [2,3,5,4,1,7,6,9,8,10,11,12]
insertionSort(cl)