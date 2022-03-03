#
# ==== Maximum Units on a Truck
# . Template 2.0
# . leetcode: 193
# . https://leetcode.com/problems/valid-phone-numbers/

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
    
    
def solution(telNo):
    # :: remove /n
    telNo = telNo.strip()
    # :: baslagic karakterini kontrol et ona gore islem yap
    if telNo[0] == '(':
        # :: ( ile basliyor ise (xxx) xxx-xxxx
        for ii, char in enumerate(telNo):
            if ii == 0 and char != '(':
                return False
            if ii == 4 and char != ')':
                return False
            if ii == 5 and char != ' ':
                return False
            if ii == 9 and char != '-':
                return False
            if ((5 < ii and ii < 9) or (9 < ii and ii < 14)):
                if not char.isdigit():
                    return False
            if 14 < ii:
                return False
    else:
        # :: digit ile basliyor ise; xxx-xxx-xxxx
        for ii, char in enumerate(telNo):
            if (ii < 3 or (3 < ii and ii < 7) or (7 < ii and ii < 12)):
                if not char.isdigit():
                    return False
            if (ii == 3 or ii ==7) and char != '-':
                return False
            if 12 < ii:
                return False
    return telNo

def Main():
    # ==== test solo
    with open('../Data/validPhoneNumbers.txt') as data:
        test0 = data.readlines() 

    # test0 = [[-1,0,0,0,0,3,3]]
    expected0 = [[-1,0,3]]
    
    # ==== test batch
    test1 = [
        [[1,3],[2,2],[3,1]],
        [[5,10],[2,5],[4,7],[3,9]]
    ]

    test11 = [
        4,
        10
    ]

    expected1 = [
        8,
        91
    ]

    # ==== test solo
    # print(solution(test0))
    for ii in range(len(test0)):
        print("Test "  + str(ii+1) + " Output: " + str(solution(test0[ii])))

    # ==== test batch
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

    # ==== test specific
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test11[ii])) + " Expected: " + str(expected1[ii]))



# ==== Main
if __name__ == "__main__":
    Main()





