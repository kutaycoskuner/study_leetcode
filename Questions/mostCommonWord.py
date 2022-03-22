#
# ==== Most Common Word
# . Template 2.2
# . leetcode: 819
# . level : easy
# . https://leetcode.com/problems/most-common-word/

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

# == Classes

# == Functions

# == Libraries
    
# == Solution
def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 0 in [c in str for c in set]

def solution(paragraph, banned):
    punktSet = {"'",",",":",";",".","?","!"}
    banSet = set(banned)
    wordSet = {}
    # :: split line with empty space
    paragraph = paragraph.split(" ")
    # :: loop
    for ii in range(len(paragraph)):
        # :: iterate over each character to clear , . ; etc.
        word = paragraph[ii].lower()
        punkt = {c for c in paragraph[ii] if c in punktSet}
        if len(punkt) > 0:
            for pp in punkt:
                word = word.split(pp)
        if isinstance(word, list):
            for jj in range(len(word)):
                # :: if banned continue
                if word[jj] in banSet or word[jj] == '':
                    continue
                # :: register it to dictionary, if is there existent increase one
                if not word[jj] in wordSet:
                    wordSet[word[jj]] = 1
                else:
                    wordSet[word[jj]] += 1
        else: 
            # :: if banned continue
            if word in banSet:
                continue
            # :: register it to dictionary, if is there existent increase one
            if not word in wordSet:
                wordSet[word] = 1
            else:
                wordSet[word] += 1

     # :: get max value within dictionary; return key
    maxValue = max(wordSet, key=lambda key: wordSet[key])
    print(wordSet)
    return(maxValue)

def Main():
    # ==== test solo
    # :: variables
    input = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    expected = "ball"

    # print(solution(input, banned))
    # return 0 
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





