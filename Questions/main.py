#
# ==== Maximum Units on a Truck
# :: Template 1.9
# :: leetcode: 1710
# :: https://leetcode.com/problems/maximum-units-on-a-truck/

# == Procedure
# :: - template edit if any
# :: - change title
# :: - change leetcode number
# :: - link of the question
# :: - create test cases and test

# == Complexity Analysis
# :: M ..

# == Notes
#  10 7 9 5 

# == Classes

# == Functions
def mergeSort(arr):
    # == bol
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        # == recursion
        mergeSort(left)
        mergeSort(right)
        # == merge
        i = 0   # :: left array index
        j = 0   # :: right array index
        k = 0   # :: merged array index
        # -------
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
            else:
                    arr[k] = right[j]
                    j += 1
            k += 1
        # -------
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # -------
        while i < len(right):
            arr[k] = right[i]
            i += 1
            k += 1
    
    
def solution(boxTypes, truckSize):
    # :: kutulari icindeki obje sayilarina gore sort et 
    # dict = {}
    # for ii in range(0, len(boxTypes)):
    #     dict[boxTypes[ii][1]] = boxTypes[ii]

    
    
    # ii = 0
    # while ii < len(boxTypes)-1:
    #     if boxTypes[ii][1] < boxTypes[ii+1][1]:
    #         temp = boxTypes[ii]
    #         boxTypes[ii] = boxTypes[ii+1]
    #         boxTypes[ii+1] = temp
    #         ii = 0
    #         continue
    #     ii += 1
    # :: sorted kutu listesinde ilk kutu sayisi kapasiteden buyukse cikar; carp; ekle
    objeSayisi = 0
    ii = 0
    while 0 < truckSize and ii < len(boxTypes):
        if (truckSize - boxTypes[ii][0]) >= 0:
            truckSize = truckSize - boxTypes[ii][0]
            objeSayisi = objeSayisi + (boxTypes[ii][0] * boxTypes[ii][1])
        else:
            objeSayisi = objeSayisi + (truckSize * boxTypes[ii][1])
            truckSize = 0
        ii += 1
    return objeSayisi

def Main():
    # ==== test solo
    test0 = [[-1,0,0,0,0,3,3]]
    expected0 = [[-1,0,3]]
    
    # ==== test batch
    test1 = [
        [[1,3],[2,2],[3,1]],
        [[5,10],[2,5],[4,7],[3,9]]
    ]

    test11 = [
        4,
        10
    ]

    expected1 = [
        8,
        91
    ]

    # ==== test solo
    # for ii in range(len(test0)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test0[ii])) + " Expected: " + str(expected0[ii]))

    # ==== test batch
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

    # ==== test specific
    for ii in range(len(test1)):
        print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test11[ii])) + " Expected: " + str(expected1[ii]))



# ==== Main
if __name__ == "__main__":
    Main()





