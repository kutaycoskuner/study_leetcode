#
# ==== Longest common prefix

# M : liste boyutu
# N : longest string length

def lonString(strs):
    # :: variables
    longest = ""
    for ii in range(1): # O(M)
        longest = strs[ii]
        for yy in range(ii+1, len(strs)): # O(M)
            first =  list(strs[ii])
            second = list(strs[yy])
            loop = first
            if len(second) < len(first):
                loop = second
            prefix = "" 
            for jj in range(0, len(loop)): # O(N)
                if first[jj] == second[jj]:
                    prefix += first[jj]
                else:
                    break
            if len(prefix) < len(longest):
                longest = prefix
    return longest

def Main():
    # ==== test
    # O(M² + MN)     
    strs = ["c","acc","ccc"]                        # :: ""
    strs1 = ["flower","flow","flight"]              # :: "fl"
    strs2 = ["flower","flow","flight","pakize"]     # :: ""
    strs3 = ["dog","racecar","car"]                 # :: ""
    strs4 = ["korcanin","korpan", "kor"]            # :: "kor"
    # ==== logic
    print(lonString(strs))
    print(lonString(strs1))
    print(lonString(strs2))
    print(lonString(strs3))
    print(lonString(strs4))



# ==== Main
if __name__ == "__main__":
    Main()


