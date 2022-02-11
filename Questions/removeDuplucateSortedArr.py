#
# ==== Remove Duplicates from Sorted ArrayValid Paranthesis
# :: leetcode: 26
# :: problem: istedigi output type ve complexity sonuclarini veremiyorum onu ogrenmem lazim

# == Procedure
# 1. change title
# 2. rename function
# 3. create test cases and test

# == Complexity Analysisis
# M : liste boyutu
# N : longest string length

# == Functions
def removeDuplicateFromSortedArray(nums):
    k = 0
    a = 0
    arr = []
    for ii in range(0, len(nums)):
        isUnique = True
        for yy in range(0, len(arr)):
            if nums[ii] == arr[yy]:
                isUnique = False
        if isUnique:
            a += nums[ii]
            arr.append(nums[ii])

    return arr

def Main():
    # ==== test cases
    nums = [1,1,2]                                  # :: 2 [1,2,_] 
    nums1 = [0,0,1,1,1,2,2,3,3,4]                   # :: 5 [0,1,2,3,4,_,_,_,_,_]
      

    # ==== testpy 
    print(removeDuplicateFromSortedArray(nums))
    print(removeDuplicateFromSortedArray(nums1))
  
# ==== Main
if __name__ == "__main__":
    Main()


