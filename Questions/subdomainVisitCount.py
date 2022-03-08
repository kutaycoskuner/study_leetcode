#
# ==== Subdomain Visit Count
# . Template 2.1
# . leetcode: 811
# . level : medium
# . https://leetcode.com/problems/subdomain-visit-count/

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
    
    
def solution(cpdomains):
    # :: get string
    dspace = [[],[],[]] # :: [[d1],[d2],[d3]] 
    visit = 0
    for ii in range(len(cpdomains)):
        # :: split string by " "
        domain = cpdomains[ii].split(" ")
        visit = int(domain[0])
        domain = domain[1].split(".")
        
        # :: domain size 2 ise birer kaydir
        if len(domain) < 3:
            domain.insert(0, "")      

        # :: split string by '.' set d1, d2, d3 :: d1 d2 d3 icin listeler tut, iki arraylerde her birine ekle
        for jj in range(len(domain)):
            for kk in range(jj+1, len(domain)):
                if domain[jj] != "":
                    domain[jj] = domain[jj] + '.' + domain[kk]
        # print(domain)

        # :: duplicate check yapip ilgili d ye ekle
        for jj in range(len(domain)):
            dup = False
            for kk in range(len(dspace[jj])):
                if dspace[jj][kk][1] == domain[jj]:
                    dspace[jj][kk] = [dspace[jj][kk][0] + visit, domain[jj]]
                    dup = True
            if not dup and domain[jj] != "":
                dspace[jj].append([visit, domain[jj]]) 

    # :: set output
    output = []
    for ii in range(len(dspace)):
        for jj in range(len(dspace[ii])):
            output.append(str(dspace[ii][jj][0]) + " " + dspace[ii][jj][1])   
    return output

def Main():
    # ==== test solo
    # with open('../Data/validPhoneNumbers.txt') as data:

    test0 = [["9001 discuss.leetcode.com"]]
    expected0 = [["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]]
    
    # ==== test batch
    test1 = [
            ["9001 discuss.leetcode.com"],
            ["900 google.mail.com", "900 intel.mail.com"],
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ]

    expected1 = [
        ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"],
        ["900 google.mail.com", "900 intel.mail.com", "1800 mail.com", "1800 com"],
        ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    ]

    # ==== test solo
    # print(solution(test0))
    # for ii in range(len(test0)):
    #     print("Test "  + str(ii+1) + " Output: " + str(solution(test0[ii])))

    # ==== test batch
    for ii in range(2,3): # len(test1)
        print("Test "  + str(ii+1) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

    # ==== test specific
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test11[ii])) + " Expected: " + str(expected1[ii]))



# ==== Main
if __name__ == "__main__":
    Main()





