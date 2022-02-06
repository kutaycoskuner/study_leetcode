#
# ==== Longest common prefix
def Main():
    # ==== test
    strs = ["flower","flow","flight"]
    
    # ==== logic
    # :: variables
    longest = ""
    # :: logic
    for ii in range(0, len(strs)):
        for yy in range(ii+1, len(strs)):
            first =  list(strs[ii])
            second = list(strs[yy])
            loop = first
            if len(second) < len(first):
                loop = second
            prefix = "" 
            for jj in range(0, len(loop)):
                if first[jj] == second[jj]:
                   prefix += first[jj]
                else:
                    break
            if len(prefix) < len(longest) or len(longest) == 0:
                longest = prefix

    print(longest)

# ==== Main
if __name__ == "__main__":
    Main()