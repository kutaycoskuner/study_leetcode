#
# ==== Best Time to Buy and Sell Stock
# . Template 2.6
# . Start Date 18-Apr-2022
# . leetcode: 121
# . level : easy
# . https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

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
# . dictionary index | value
# . dictionary ye ekle
# . onceki indexleri current value dan cikar eger daha yuksekse o indexi tut

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(prices):
    # dict = {}               # :: key = index, value = value
    maxProfit = 0           # :: day difference, profit
    currLowest = prices[0]  # :: current lowest
    for ii in range(len(prices)):
        # :: kontrol
        if prices[ii] - currLowest > maxProfit:
            maxProfit = prices[ii] - currLowest
        # # :: insert
        # dict[ii] = prices[ii]
        # :: eger current en dusuk ise 
        if prices[ii] <= currLowest:
            currLowest = prices[ii]
    return maxProfit

def solution1(prices):
    dict = {}            # :: key = index, value = value
    maxProfit = 0        # :: day difference, profit
    for ii in range(len(prices)):
        # :: kontrol
        for jj in range(ii):
            if prices[ii]-prices[jj] > maxProfit:
                maxProfit = prices[ii]-prices[jj]
        # :: insert
        # dict[ii] = prices[ii]
    return maxProfit


def Main():

    # :: argument identification
    if len(sys.argv) >= 2:
        args = int(sys.argv[1])
    else:
        args = None

    # ==== test batch
    input1 = [
        [7,1,5,3,6,4],
        [7,6,4,3,1]
    ]
    input2 = [
        [2,2],
        [9,4,9,8,4],
        [1,1],
        [1,2]
    ]

    output1 = [
        5,
        0
    ]

    # :: test batch
    if args == None:
        for ii in range(len(output1)):  # len(test1)
            print("Test " + str(ii+1) + " Output: " +
                str(solution(input1[ii])) + "\t Expected: " + str(output1[ii]))
    else:
        print("Test " + str(args) + " Output: " +
                str(solution(input1[args-1])) + "\t Expected: " + str(output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
