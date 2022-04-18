#
# ==== Merge Sorted Array
# . Template 2.5
# . Start Date 15-Apr-2022
# . leetcode: 88
# . level : easy
# . https://leetcode.com/problems/merge-sorted-array/

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
# . a  b  c  d  e
# .   ii+1   len-2
# . a _ b c d
#.      ii+2 

# . algoritma 1
# . -----------
# . - eger ikinci arrayin su anki degeri birinci arrayden kucukse
# .     - birinci arrayi bir kaydir
# .     - birinci arrayin su anki degerine ekle

# . - birinci arrayin sonuna geldiyse



# . - ikinci arrayin sonuna geldiyse

# . birincinin veya ikincinin hepsinin yerlesmesi durumunda problem yok
# . 

# == Libraries

# == Classes

# == Functions

# == Solution
from stringprep import in_table_a1


def solution(nums1, m, nums2, n):
    iter_1 = 0
    iter_2 = 0
    shifted = 0
    notShifted = 0
    if m != 0:
        # print(nums1, shifted)
        if len(nums2) != 0:
            while iter_1 < m and iter_2 < n:
                if nums1[iter_1] > nums2[iter_2]:
                    # :: shift
                    nums1[iter_1+1:len(nums1)] = nums1[iter_1:len(nums1)-1]
                    nums1[iter_1] = nums2[iter_2]
                    iter_2 += 1
                    shifted += 1
                else:
                    notShifted += 1
                iter_1 += 1

            # print(nums1, shifted)
            while iter_2 < n:
                # print(iter_1, iter_2, nums1(iter_1), nums2(iter_2))
                if nums1[iter_1] > nums2[iter_2]:
                    # :: shift
                    nums1[iter_1+1:len(nums1)] = nums1[iter_1:len(nums1)-1]
                    nums1[iter_1] = nums2[iter_2]
                    # shifted += 1
                    iter_1 += 1
                    iter_2 += 1
                else: # :: nums 2 degeri simdiki nums1 degerinden buyuk veya esit ise
                    # if nums1[iter_1] < nums2[iter_2]:
                    #     iter_1 += 1
                    if shifted != 0:
                        iter_1 += 1
                        shifted -= 1
                        continue
                    nums1[iter_1] = nums2[iter_2]
                    iter_1 += 1
                    iter_2 += 1
                    # shifted -= 1
            # print(nums1, shifted)
    else: # :: birincinin boyu sifir ise dogrudan ikinciyi birinciye esitle
        for ii in range(len(nums2)):
            nums1[ii] = nums2[ii]
    # print(n- m-shifted)
    return nums1

def Main():
    # ==== test solo
    # :: variables
    input1 = [-1,0,0,0,3,0,0,0,0,0,0]
    input2 = 5
    input3 = [-1,-1,0,0,1,2]
    input4 = 6
    output = [-1,-1,-1,0,0,0,0,0,1,2,3]

    # print("solution: ", solution(input1, input2, input3, input4), "\t expected: ", output)
    # return 0

    # ==== test batch
    input1 = [
        [1,2,4,5,6,0],
        [1,2,3,0,0,0],
        [1,2,3,0,0,0],
        [-1,0,1,1,0,0,0,0,0],
        [-1,0,0,0,3,0,0,0,0,0,0]
    ]
    input2 = [
        5,
        3,
        3,
        4,
        5
    ]
    input3 = [
        [3],
        [4,5,6],
        [2,5,6],
        [-1,0,2,2,3],
        [-1,-1,0,0,1,2]
    ]
    input4 = [
        1,
        3,
        3,
        5,
        6
    ]

    output1 = [
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,2,3,5,6],
        [-1,-1,0,0,1,1,2,2,3],
        [-1,-1,-1,0,0,0,0,0,1,2,3]
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii], input3[ii], input4[ii])) + "\t Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
