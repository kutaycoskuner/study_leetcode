#
# ==== Permutations II
# . Template 2.1
# . leetcode: 47
# . level : medium
# . https://leetcode.com/problems/permutations-ii/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# Time complexity
# Space Complexity

# == Notes
# . 1 2 3 4 
# . 1 2 4 3  | son karaktere gel. bir oncekiyle degistir.
# . _ _ x x
# . 1 3 2 4  | bir onceki karaktere gec
# . _ x x x
# . 1 3 4 2  | bir onceki karakterden sonrakileri yer degistirerek butun olasiliklari dene
# . 1 4 2 3  | olasilik kalmadiginda kendi basamagini degistir
# . 1 4 3 2  | 24 4! 4 3 2 1 = 24
# . _ _ _ _ 

# . 1 2
# . 2 1
#  

# . 1 2 3 4 5  []           x0
# .  _ _ _ _ _  
# . 1 2 3 4 5  [5]          x1  1
# . _ _ _ _ x                                   
# . 1 2 3 5 4  [5,4]        x2  1 
# . _ _ _ x x               
# . 1 2 4 3 5  [5,4,3]      x3  4
# . _ _ x x x               
# . 1 2 4 5 3               x3
# . 1 2 5 3 4               x3
# . 1 2 5 4 3               x3
# . 1 3 2 4 5  [5,4,3,2]    x4  8
# . 1 3 2 5 4               
# . 1 3 4 2 5
# . 1 3 4 5 2
# . 1 3 5 2 4
# . 1 3 5 4 2


# . [1] 2 3 []
# == Classes

# == Functions

# == Libraries
    
# == Solution
# Python function to print permutations of a given list
def permutation(nums):
    # :: edge case: empty list
    if len(nums) == 0:
        return []
 
    # :: edge case one element
    if len(nums) == 1:
        return [nums]
  
    perms = set() # :: {} # :: list that keeps permutations
    for ii in range(len(nums)):
       curr = nums[ii]
       rest = nums[:ii] + nums[ii+1:]
 
       for perm in permutation(rest):
            perms.add(tuple([curr]) + tuple(perm))
            
    return perms


def permute(nums, curr = 0, perms = []):
    if curr == len(nums)-1:
        # perms.append(nums)
        print (perms)
        pass
    else:
        for ii in range(curr, len(nums)):
            nums[curr], nums[ii] = nums[ii], nums[curr]
            print(nums)
            # print("aa: ", nums)
            # :: unique check
            # unique = True
            # for jj in range(len(perms)):
            #     if perms[jj] == nums:
            #         unique = False
            # if unique:
            #     perms.append(nums)
            # :: unique check
                # print(perms)
            permute(nums, curr+1, perms)
            nums[curr], nums[ii] = nums[ii], nums[curr] # backtrack
            print(nums)

def solution(nums, perms):
    if len(nums) == 0:
        return perms
    
    perms = []
    rest = nums
    for ii in range(len(nums)):
        print(ii, " ", nums[ii])
        curr = nums[ii]
        # if rest[ii] != None:
        #     rest.pop(ii)
        solution(rest, perms.append(curr))

def Main():
    # ==== test solo
    listDataA = [1,2,3,4,5]             # :: 2,1,4,3
    listDataB = [[1,2],0]             # :: tail connects to node index 0
    listDataC = [[1], None]                 # :: no cycle

    
    # ==== test batch
    test1 = [
        [1,2],
        [1,1,2],
        [1,2,3],
        [1,2,3,4]
    ]

    expected1 = [
        [[1,2],[2,1]],
        [[1,1,2],[1,2,1],[2,1,1]],
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        []
    ]

    # ==== test solo
    # print(solution(test0))
    # for ii in range(len(test0)):
    #     print("Test "  + str(ii+1) + " Output: " + str(solution(test0[ii])))
    # !
    # string = "ABC"
    # n = len(string)
    # a = list(string)
    # permute(a)
    # # permute('abc',"")
    # solution(["a","b","c"],[])

    data = [1,2,2]
    print(permutation(data))
    return 0 
    # ==== test batch
    for ii in range(len(expected1)): # len(test1)
        print("Test "  + str(ii+1) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

    # ==== test specific
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test11[ii])) + " Expected: " + str(expected1[ii]))



# ==== Main
if __name__ == "__main__":
    Main()





