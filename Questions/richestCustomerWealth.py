#
# ==== Richest Customer Wealth
# :: Template 1.2
# :: leetcode: 1672
# :: https://leetcode.com/problems/richest-customer-wealth/

# == Procedure
# :: - change title
# :: - template edit if any
# :: - change leetcode number
# :: - link of the question
# :: - rename function
# :: - create test cases and test

# == Complexity Analysis
# :: M : liste boyutu
# :: N : longest string length
# todo ogren: time complexity
# todo ogren: space complexity

# == Functions
def solution(accounts):
    bezos = 0
    # :: customer loop
    for ii in range(len(accounts)):
        # :: account loop topla
        customer = 0
        for yy in range(len(accounts[ii])):
            customer +=accounts[ii][yy]
        # :: account comaccountse et buyuk olani tut
        if customer > bezos:
            bezos = customer
    return bezos


def Main():
    # ==== test cases
    t0 = [[1,2,3],[3,2,1]]                                # :: istenilen: 6 
    t1 = [[1,5],[7,3],[3,5]]                              # :: istenilen: 10 
    t2 = [[2,8,7],[7,1,3],[1,9,5]]                        # :: istenilen: 17 

    # ==== testpy 
    print(solution(t0))
    print(solution(t1))
    print(solution(t2))
  
# ==== Main
if __name__ == "__main__":
    Main()


