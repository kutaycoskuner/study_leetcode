#
# ==== Valid Sudoku
# . Template 2.6
# . Start Date 22-Apr-2022
# . leetcode: 36
# . level : medium
# . https://leetcode.com/problems/valid-sudoku/

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
# . dictinary 1-9
# . her row dictionary check iterasyonu
# . her row un i. elemani iteraasyon
# . 33 36 39, 63 66 69, 93 96 99 check

# . 00 22, 03 25, 06 28
# . 30 52, 33 55, 36 58
# . 50 82, 53 85, 56 88
# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(board):
    pass
    # # :: create set
    # dict_r = {".": False}
    # for ii in range(1, 10):
    #     dict_r[str(ii)] = False
    # dict_c = dict_r
    # dict_s = dict_r

    # # :: Check row
    # for ii in range(3):
    #     dict_r = dict_r.fromkeys(dict_r, False)
    #     dict_c = dict_c.fromkeys(dict_c, False)
    #     dict_s = dict_s.fromkeys(dict_s, False)

    #     mc, mr = 3, 3
    #     for jj in range(9):
    #         # :: check rows
    #         if dict_r[board[ii][jj]] == False:
    #             dict_r[board[ii][jj]] = True
    #         elif board[ii][jj] != ".":
    #             return False
    #         # :: check cols
    #         if dict_c[board[jj][ii]] == False:
    #             dict_c[board[jj][ii]] = True
    #         elif board[jj][ii] != ".":
    #             return False
    #         # :: check squares
    #         # print(jj%mr, jj%mc)
    #         # if dict_s[board[jj%mr][jj%mc]] == False:
    #         #     dict_s[board[jj%mr][jj%mc]] = True
    #         # elif board[ii%mr][jj%mc] != ".":
    #         #     return False 
    #     # inc += 1
    #     # print('---------', inc)

    # # :: check square
    # inc_r = 0
    # inc_c = 0
    # while inc_r < 9:
    #     inc_c = 0
    #     while inc_c < 9:
    #         dict_s = dict_s.fromkeys(dict_s, False)
    #         for ii in range(3):
    #                 for jj in range(3):
    #                     if dict_s[board[ii%3+inc_r][jj%3+inc_c]] == False:
    #                         dict_s[board[ii%3+inc_r][jj%3+inc_c]] = True
    #                     elif board[ii%3+inc_r][jj%3+inc_c] != ".":
    #                         return False 
    #         inc_c += 3
    #     inc_r += 3
    # return True

def solution1(board):
    # :: create set
    dict = {".": False}
    for ii in range(1, 10):
        dict[str(ii)] = False

    # :: Check row
    for ii in range(9):
        dict = dict.fromkeys(dict, False)
        for jj in range(9):
            if dict[board[ii][jj]] == False:
                dict[board[ii][jj]] = True
            elif board[ii][jj] != ".":
                return False 

    # :: check column
    for ii in range(9):
        dict = dict.fromkeys(dict, False)
        for jj in range(9):
            if dict[board[jj][ii]] == False:
                dict[board[jj][ii]] = True
            elif board[jj][ii] != ".":
                return False

    # :: check square
    inc_r = 0
    inc_c = 0
    while inc_r < 9:
        inc_c = 0
        while inc_c < 9:
            dict = dict.fromkeys(dict, False)
            for ii in range(3):
                    for jj in range(3):
                        if dict[board[ii%3+inc_r][jj%3+inc_c]] == False:
                            dict[board[ii%3+inc_r][jj%3+inc_c]] = True
                        elif board[ii%3+inc_r][jj%3+inc_c] != ".":
                            return False 
            inc_c += 3
        inc_r += 3
    return True 

def Main():
    # ==== test batch
    input1 = [
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."] # . 3
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]],
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    ]

    output1 = [
        True,
        False
    ]

    # :: argument identification
    if len(sys.argv) >= 2:
        args = int(sys.argv[1])
    else:
        args = None
    # :: test batch
    if args == None:
        for ii in range(len(output1)):  # len(test1)
            print("Test " + str(ii+1) + " Output: " +
                str(solution(input1[ii])) + "\t Expected: " + str(output1[ii]))
            # print(str((solution(input1[ii]) == output1[ii])))
    else:
        answer = solution(input1[args-1])
        print("Test " + str(args) + " Output: " +
                str(answer) + "\t Expected: " + str(output1[args-1]) + '\n' + str(answer == output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
