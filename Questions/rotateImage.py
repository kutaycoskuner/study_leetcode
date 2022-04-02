#
# ==== Rotate Image
# . Template 2.2
# . leetcode: 48
# . level : medium
# . https://leetcode.com/problems/rotate-image/

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
# .. 1 2 3   |   7 4 1
# .. 4 5 6   |   8 5 2
# .. 7 8 9   |   9 6 3

# .. [1,1] [1,3] :: [1,2] [2,3] :: [1,3] [3,3]
# .. [2,1] [1,2] :: [2,2] [2,2] :: [2,3] [3,2]
# .. [3,1] [1,1] :: [3,2] [2,1] :: [3,3] [3,1]

# .. 1,1 -> 1,3 | 1,3 -> 3,3 | 3,3 -> 3,1 | 3,1 -> 1,1
# ..  a      b     b      c     c      d     d      a
# .. 1,2 -> 2,3 | 2,3 -> 3,2 | 3,2 -> 2,1 | 2,1 -> 1,2 

# .. a = [0, 0]; b = [0, n-1]; c = [n-1, n-1]; d = [n-1, 0]
# .. a = [0, i]; b = [i, n-1]; c = [n-1, n-1]; d = [n-1, i]

# .. a b c d  | n j e a 
# .. e f g h  | p k f b
# .. j k l m  | r l g c
# .. n p r s  | s m h d

# .. [1,1] [1,4] :: [1,2] [2,4] :: [1,3] [3,4] :: [1,4] [4,4]
# .. [2,1] [1,3] :: [2,2] [2,3] :: [2,3] [3,3] :: [2,4] [4,3]
# .. [3,1] [1,2] :: [3,2] [2,2] :: [3,3] [3,2] :: [3,4] [4,2]
# .. [4,1] [1,1] :: [4,2] [2,1] :: [4,3] [3,1] :: [4,4] [4,1]

# .. donguye basla
# .. 1,1 -> 1,4 | 1,4 -> 4,4 | 4,4 -> 4,1 | 4,1 -> 1,1
# .. 1,2 -> 2,4 | 2,4 -> 4,3 | 4,3 -> 3,1 | 3,1 -> 1,2
# .. 1,3 -> 3,4 | 3,4 -> 4,2 | 4,2 -> 2,1 | 2,1 -> 1,3
# .. bir ic katmana gir (n-2 > 1) 
# .. 2,2 -> 2,3 | 2,3 -> 3,3 | 3,3 -> 3,2 | 3,2 -> 2,2

# == Classes

# == Functions

# == Libraries
    
# == Solution
def printMatrix(matrix0, matrix1, matrix2):
    for ii in range(len(matrix0)):
        print(matrix0[ii], "    ", matrix1[ii], "    ", matrix2[ii])

def fourVar(a,b,c,d):
    arr = [a,b,c,d] # temp = a 
    # a, b, c
    
    for ii in reversed(range(len(arr)-1)):
        temp = arr[ii] # c  
        arr[ii] = arr[ii+1] # c <- d
        arr[ii+1] = temp # d <- temp
    # temp = a
    # a = b
    # b = temp
    print(arr)




def solution(matrix):    
    # :: variable matris boyu
    n = len(matrix)
    k = 0 # katman

    # .. a = [0, 0]; 
    # .. b = [0, n-1];
    # .. c = [n-1, n-1];
    # .. d = [n-1, 0]

    # for ii in reversed(range(len(matrix)-1)):
    #     temp = matrix[n-1][n-1]
    #     matrix[n-1][n-1] = matrix[n-1][0]
    #     matrix[n-1][0] = temp
        # break

    # ::  1 den buyuk oldugu surece gir
    while n-k > 1:
        # :: matris boyu -1 den rotasyona basla
        for ii in range(k, n-k-1):
            # :: 4 degeri cevir
            a = matrix[k][ii] # [0,0] [1,1]
            b = matrix[ii][n-k-1] # [0,3] [1,2]
            c = matrix[n-k-1][n-ii-1] # [3,3] [2,2]
            d = matrix[n-ii-1][k] # [3, 0] [2,1]
            #
            matrix[k][ii] = d
            matrix[ii][n-k-1] = a
            matrix[n-k-1][n-ii-1] = b
            matrix[n-ii-1][k] = c
            # print('a')
            #
            # .. 1,1 -> 1,3 | 1,3 -> 3,3 | 3,3 -> 3,1 | 3,1 -> 1,1
            # ..  a      b     b      c     c      d     d      a
            # .. 1,2 -> 2,3 | 2,3 -> 3,2 | 3,2 -> 2,1 | 2,1 -> 1,2 
            # .. a = [0, i]; b = [i, n-1]; c = [n-1, n-1]; d = [n-1, i]
        k += 1

    return matrix

        # n = len(matrix)
        # k = 0
        # while n-k > 1:
        #     for ii in range(k, n-k-1):
        #         matrix[k][ii], matrix[ii][n-k-1], matrix[n-k-1][n-ii-1], matrix[n-ii-1][k] = matrix[n-ii-1][k], matrix[k][ii], matrix[ii][n-k-1], matrix[n-k-1][n-ii-1] 
        #     k += 1

def Main():
    # ==== test solo
    # :: variables
    # input = [[1,2,3],[4,5,6],[7,8,9]]
    # input2 = [[1,2,3],[4,5,6],[7,8,9]]
    # expected = [[7,4,1],[8,5,2],[9,6,3]]
    input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print('Solution: ' , '\n')
    # solution(input)
    printMatrix(input, solution(input2), expected)
    # fourVar(1,2,3,4) # .. 4 1 2 3
    return 0 
    # :: display

    # ==== test batch
    input1 = [
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        "a",
        "a, a, a, a, b,b,b,c, c",
        "j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?"
    ]

    input2 = [
        ["hit"],
        [],
        ["a"],
        ["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"]
    ]

    output1 = [
        "ball",
        "a",
        "b",
        "y"
    ]

    # :: test batch
    for ii in range(len(output1)): # len(test1)
        print("Test "  + str(ii+1) + " Output: " + str(solution(input1[ii],input2[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()





