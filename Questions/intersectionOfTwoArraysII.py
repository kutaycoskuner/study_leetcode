#
# ==== Intersection of Two Arrays II
# . Template 2.5
# . Start Date 18-Apr-2022
# . leetcode: 350
# . level : easy
# . https://leetcode.com/problems/intersection-of-two-arrays-ii/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# . Time complexity       log n   | prev: n log n
# . Space Complexity

# . optimal cozumu goremiyorsan brute force
# . complexity analysis | time ve space
# . gorsellestir redundant work ara | veri yapisi | adim
# . redundancy yi kod uzerinde tespit et (pattern recognition)
# . cozum ara

# == Notes


# == Libraries

# == Classes

# == Functions

# == Solution
def solution(nums1, nums2):
    intersection = []
    ii = 0
    jj = 0
    while ii < len(nums1):
        noMatch = True
        jj = 0
        while jj < len(nums2):
            if nums1[ii] == nums2[jj]:
                # print(nums1, nums2)
                intersection.append(nums1[ii])
                nums1.pop(ii)
                nums2.pop(jj)
                ii, jj = 0, 0
                noMatch = False
                break
            jj += 1
        if noMatch:
            ii += 1
    return intersection

def solution1(nums1, nums2):
    ii = 0              #:: iterator
    isBreak = False      #:: tam eslesme var mi yok mu?
    intersection = []  #:: kesisim
    biggestIntersection = [] #::
    #
    # :: hay loopa basla
    while ii < len(nums1):
        for jj in range(len(nums2)):
            intersection = []
            if nums1[ii] == nums2[jj] and len(nums1)- ii > len(biggestIntersection):
                isBreak = False
                intersection.append(nums2[jj])
                # :: geri kalan karakterleri karsilastir
                if len(nums1) - ii > 1 and len(nums2) - jj > 1: # :: defensive
                    for yy in range(jj+1, len(nums2)):
                        if nums1[ii+yy-jj] == nums2[yy]:
                            intersection.append(nums2[yy])
                        else:
                            isBreak = True
                            break
            if len(intersection) > len(biggestIntersection):
                biggestIntersection = intersection
            if isBreak:
                break
        ii += 1
    return biggestIntersection

def Main():
    # ==== test solo
    # :: variables
    input1 = [1,2,2,1]
    input2 = [2,2]
    # input3 = [-1,-1,0,0,1,2]
    # input4 = 6
    output = [2,2]

    # print("solution: ", solution(input1, input2), "\t expected: ", output)
    # return 0

    # ==== test batch
    input1 = [
        [1,2,2,1],
        [4,9,5],
        [1],
        [2,1]
    ]
    input2 = [
        [2,2],
        [9,4,9,8,4],
        [1,1],
        [1,2]
    ]

    output1 = [
        [2,2],
        [4,9],
        [1],
        [1,2]
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii])) + "\t Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
