#
# ==== Kth Largest Element in a Stream
# . Template 2.3
# . leetcode: 703
# . level : easy
# . https://leetcode.com/problems/kth-largest-element-in-a-stream/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# Time complexity       log n   | prev: n log n
# Space Complexity

# == Notes
# .   2 3 4 4 5 5 8 9 10
# .             x

# == Libraries
import heapq

# == Classes


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # self.nums = heapq.heapify(nums)
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums  # nums
        self.k = k

    def add(self, val):

        heapq.heappush(self.nums, val)
        if(len(self.nums) > self.k):
            heapq.heappop(self.nums)

        # print(self.nums[0])
        return self.nums[0]
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        if(len(self.nums) > self.k):
            self.nums.pop(0)
        print(self.nums[-self.k])
        # return self.nums[-self.k]

        # heappush(self.nums, val)
        # print(self.nums)
        # self.nums.sort()
        # heapq.heappush(self.nums, val)# self.nums.append(val)
        # for ii in range(self.k):
        #     heappop(self.nums)

# == Functions

# == Solution


def solution(stones):
    pass


def Main():
    # ==== test solo
    # :: variables
    input = [2, 8, 4, 5, 5, 7, 8, 9, 3, 4, -12]  # stream
    input2 = 3                 # k
    expected = 3

    # heapq.heapify(input)
    # heapq.heappush(input, 3)
    # heapq.heappush(input, 12)
    # print(input)

    item = KthLargest(input2, input)
    item.add(3)      # return 4
    item.add(5)      # return 5
    item.add(10)     # return 5
    item.add(11)      # return 8
    item.add(12)      # return 8

    # print("solution: ", solution(input), " expected: ", expected)
    return 0

    # ==== test batch
    input1 = [
        [2, 7, 4, 1, 8, 1],
        [1],
        [1, 3],
        [2, 2]
        # 012345678901234567890123
    ]

    output1 = [
        1,
        1,
        2,
        0
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
