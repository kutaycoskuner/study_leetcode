#
# ==== Remove duplicates from sorted array
# :: Template 1.8
# :: leetcode: 26
# :: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# == Procedure
# :: - template edit if any
# :: - change title
# :: - change leetcode number
# :: - link of the question
# :: - create test cases and test

# == Complexity Analysis
# :: M ..

# == Notes
# ::    in      0,0,1,1,1,2,2,3,3,4
# ::    ex      0,1,2,3,4,.,.,.,.,.
# ::    ===========================
# ::    in      0,0,1,1,1,2,2,3,3,4 
# ::            x x                   current en buyuk = index 0; compare  
# ::    in      0,0,1,1,1,2,2,3,3,4 
# ::                                 comparisondaki ikinciyi al, daha buyugunu ara replace et 
# ::    in      0,0,1,1,1,2,2,3,3,4 
# ::                                 current = buldugu daha buyuk olan
# ::    in      0,1,0,1,1,2,2,3,3,4 
# ::                                 ucuncuden compare
# ::    in      0,1,0,1,1,2,2,3,3,4 
# ::                x    
# :: ite 1      0,1,0,1,1,2,2,3,3,4
# ::                -     +       
# :: ite 2      0,1,2,1,1,0,2,3,3,4
# ::                  -       +       
# :: ite 3      0,1,2,3,1,0,2,1,3,4

# == Classes

# == Functions
def solution(nums):
    seq = 1
    biggest = nums[0]
    #
    for ii in range(1, len(nums)):
        if nums[ii] > biggest:
            biggest = nums[ii]
            nums[seq] = nums[ii]
            seq += 1 

    return seq, nums


    # k = len(nums)
    # ii = 0
    # # :: her biri uzerinden teker teker gec
    # while ii < k:
    #     isUnique = True
    #     # :: karakterin unique olup olmadigini kontrol et 
    #     for yy in range(ii+1, k):
    #         if nums[ii] == nums[yy]:
    #             isUnique = False
    #             k -= 1
    #             for yy in range(ii, k):
    #                 nums[yy] = nums[yy] + nums[yy+1]
    #                 nums[yy+1] = nums[yy] - nums[yy+1]
    #                 nums[yy] = nums[yy] - nums[yy+1]
    #             break
    #     # :: unique degil ise alip sona kadar teker teker tasi
    #     if not isUnique:
    #         continue
    #     ii +=1
    # return k, nums

def Main():
    # ==== test solo
    test0 = [[-1,0,0,0,0,3,3]]
    expected0 = [[-1,0,3]]
    
    # ==== test batch
    test1 = [
        [1,2,3],
        [-1,0,0,0,0,3,3],
        [1,2,2,3],
        [1],
        [1,2],
        [1,1,2],
        [0,0,1,1,2,2,3,3,4],
        [0,0,1,1,1,2,2,3,3,4],
        [0,0,1,1,1,1,2,2,3,3,4]
    ]
    expected1 = [
        [1,2,3],
        [-1,0,3],
        [1,2,3],
        [1],
        [1,2],
        [1,2,"_"],
        [0,1,2,3,4,"_","_","_","_"],
        [0,1,2,3,4,"_","_","_","_","_"],
        [0,1,2,3,4,"_","_","_","_","_","_"]
    ]

    # ==== test solo
    # for ii in range(len(test0)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test0[ii])) + " Expected: " + str(expected0[ii]))

    # ==== test batch
    for ii in range(len(test1)):
        print("Test "  + str(ii) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

# ==== Main
if __name__ == "__main__":
    Main()





