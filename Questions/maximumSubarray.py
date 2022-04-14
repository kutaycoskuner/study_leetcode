#
# ==== Maximum Subarray
# . Template 2.4
# . leetcode: 53
# . level : easy
# . https://leetcode.com/problems/maximum-subarray/

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
# . ----------------
# . for: i array boyunca iterasyon
# .     for: sabit tutulan sayidan sonrakileri teker teker arttirarak topla [a] [a,b] [a,b,c] en yuksek degeri Baslangic ve Bitis noktalariyla tu
# . ---- Algoritma 1
# . -> a, b, c, d, e 
# . a b c d e
# . a b c d
# . a b c
# . a b 
# . a
# . ---
# . b c d e
# . b c d
# . b c
# . b
# . ---
# . c d e
# . c d                 
# . c                   
# . ---
# . d e                 
# . d                   
# . --- 
# . e  
# . ----------------
# . n = kume boyu;
# . for i n |
    
# . ---- Algoritma 2
# . ----------------
# . -> a, b, c, d, e
# . 5 | 1 | [a b c d e]
# . 4 | 2 | [a b c d] [b c d e]
# . 3 | 3 | [a b c] [b c d] [c d e]
# . 2 | 4 | [a b] [b c] [c d] [d e]
# . 1 | 5 | [a] [b] [c] [d] [e]

# . ---- Algoritma 3
# . ----------------
# . -> a, b, c, d, e
# . max
# . a = max
# . ab if ab >  then max = ab
# . abc if abc > max
# == Libraries

# == Classes

# == Functions

# == Solution
def solution(nums):
    currSum = 0
    maxSum = 0
    reseted = False
    for x in nums:
        if currSum + x > 0:
            currSum += x
        else: 
            reseted = True
            currSum = 0
        print('curr sum ', currSum)
        if currSum > maxSum:
            reseted = False
            maxSum = currSum
    if reseted and maxSum == 0:
        maxSum = max(nums)
    return maxSum

def solution1(nums):
    subArr = []                 # .  [begin, end]
    largest = min(nums)         # . en buyuk degeri tutan var
    kk = 0
    jj = 0
    while kk < len(nums):
        n = len(nums)
        while jj < n:
            # :: butun arrayi toplama a, b, c, d
            control = 0
            for ii in range(kk, n):
                control += nums[ii]
            # :: largest check
            if kk < n:
                if control > largest:
                    # print(kk, n)
                    largest = control
                    subArr = [kk, n]
            n -= 1
        kk += 1
    return largest

def solution2(nums):
    n = len(nums)               # . sub array boyu
    m = 1                       # . reverse counter
    max = min(nums)         # . largest sub array count holder
    subArrays = []
    # :: array boyu kadar iterasyon
    for ii in range(len(nums)):    # . n
        # :: array boyundan her bir cikardiginda iterasyon sayisi bir artacak sekilde array    
        for jj in range(m):        # . n
            sum = 0
            # :: array topa
            # for kk in range(jj, n + jj):
            #     sum += nums[kk]
            # if sum > max:
            #     max = sum
            subArrays.append(nums[jj: n+jj])            
        m += 1
        n -= 1
    return [subArrays, max]

def solution3(nums):
    max = min(nums)                      # . largest sub array count holder
    # :: array boyu kadar iterasyon
    for ii in range(len(nums)):          # . n
        sum = 0
        # :: array boyundan her bir cikardiginda iterasyon sayisi bir artacak sekilde array    
        for jj in range(ii, len(nums)):  # . n
            sum += nums[jj]
            if sum > max:
                max = sum    
    return max

# todo command line parametr

def Main():
    # ==== test solo
    # :: variables
    input = [-2,1,-3,4,-1,2,1,-5,4]
    # input = [1, 2, -5, 4, 5]
    expected = 6

    # print("solution: ", solution(input), "\t\t expected: ", expected)
    # return 0

    # ==== test batch
    input1 = [
        [1,2,3,4,5],
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
        [-1, -5, -7],
        [1,2,-1,-2,2,1,-2,1]
    ]

    output1 = [
        15,
        6,
        1,
        23,
        -1,
        3
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii])) + "\t\t Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
