#
# ==== Merge two sorted lists
# :: leetcode: 26
# :: problem: leetcode kabul etmiyor | array olarak degil linked list olarak cozmeliymisim | linked list data structures coz

# == Procedure
# :: 1. change title
# :: 2. rename function
# :: 3. create test cases and test

# == Complexity Analysis
# :: M : liste boyutu
# :: N : longest string length
# todo ogren: time complexity
# todo ogren: space complexity

# == Functions
def mergeTwoSortedLists(list1,list2):
    mergedList = list1 + list2
    whileCounter = 0
    # #:: ikili karsilastir her seferinde basa don
    # while whileCounter < len(mergedList)-1:
    #     if mergedList[whileCounter] > mergedList[whileCounter+1]:
    #         temp = mergedList[whileCounter+1]
    #         mergedList[whileCounter+1] = mergedList[whileCounter]
    #         mergedList[whileCounter] = temp
    #         whileCounter = 0
    #     whileCounter += 1            
    
    # ::  her bir elemani teker teker geri kalanla karsilastir
    for ii in range(0, len(mergedList)-1):
        for yy in range(ii, len(mergedList)-1):
            if mergedList[ii] > mergedList[yy]:
                temp = mergedList[yy]
                mergedList[yy] = mergedList[ii]
                mergedList[ii] = temp
            

    return mergedList

def Main():
    # ==== test cases
    list11 = [1,2,4]                                # :: istenilen: [1,1,2,3,4,4] 
    list12 = [1,3,4]                           
    #
    list21 = []                                     # :: istenilen: []
    list22 = []
    #
    list31 = []                                     # :: istenilen: [0]
    list32 = [0]

    # ==== testpy 
    print(mergeTwoSortedLists(list11,list12))
    print(mergeTwoSortedLists(list21,list22))
    print(mergeTwoSortedLists(list31,list32))
  
# ==== Main
if __name__ == "__main__":
    Main()


