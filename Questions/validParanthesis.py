#
# ==== Valid Paranthesis

# == Procedure
# 1. change title
# 2. rename function
# 3. create test cases and test

# == Complexity Analysisis
# M : liste boyutu
# N : longest string length

# == Functions
def validateParanthesis(s):
    arr = list(s)
    sequence = []
    open = ['(', '[', '{']
    close = [')', ']', '}']
    cont = False
    # :: loop characters
    for char in arr:
        cont = False
        # :: kapali parantezle basliyorsa kapat cik
        if sequence == []:
            for closeChar in close:
                if char == closeChar:
                    return False
        # :: acik karakter olup olmadigini kontrol et
        for ii in range(0, len(open)):
            # :: karakter bulduysa kapatma karakterini pushla
            if char == open[ii]:
                sequence.append(close[ii])
                cont = True
                continue
        if cont:
            continue
        # :: kapama karakterinin dogrulugu kontrol
        for closeChar in close:
            if char == closeChar:
                if char != sequence[len(sequence)-1]:
                    return False   
                else:
                    sequence.pop(-1)     
    return sequence == []

def Main():
    # ==== test cases
    s = "()"            # :: true                      
    s1 = "()[]{}"       # :: true
    s2 = "([{}])"       # :: true
    s3 = "(]"           # :: false
    s4 = "(x+[y*z])"    # :: true
    s5 = "(x+[y*z})"    # :: false
    s6 = "]()"          # :: false
    s7 = "["            # :: false

    # ==== testpy 
    print(validateParanthesis(s))
    print(validateParanthesis(s1))
    print(validateParanthesis(s2))
    print(validateParanthesis(s3))
    print(validateParanthesis(s4))
    print(validateParanthesis(s5))
    print(validateParanthesis(s6))
    print(validateParanthesis(s7))

# ==== Main
if __name__ == "__main__":
    Main()


