#
# ==== Pascals Triangle II
# :: leetcode: 119
# :: problem: leetcode kabul etmiyor | array olarak degil linked list olarak cozmeliymisim | linked list data structures coz

# == Procedure
# :: - change title
# :: - change leetcode number
# :: - rename function
# :: - create test cases and test

# == Complexity Analysis
# :: M : liste boyutu
# :: N : longest string length
# todo ogren: time complexity
# todo ogren: space complexity

# == Functions
def pascalTriangle(rowIndex):
    row = [1]
    iteration = len(row) + 1
    # :: row kadar iterasyon 
    for ii in range(rowIndex):
        newRow = [1]
        for yy in range(iteration-1):     
            # :: son eleman yoksa 1 ekle
            if yy+1 == iteration-1:
                newRow.append(1)
            # :: 1,2; 2,3; 3,4; topla insert et
            else:
                item = row[yy] + row[yy+1]
                newRow.append(item)
        row = newRow    
        iteration = len(row) + 1
    # :: 1 2 1 
    return row


def Main():
    # ==== test cases
    n0 = 0                                # :: istenilen: [1] 
    n1 = 1                                # :: istenilen: [1,1] 
    n3 = 3                                # :: istenilen: [1,3,3,1] 
    n6 = 6                                # :: istenilen: [1,6,15,20,15,6,1] 


    # ==== testpy 
    print(pascalTriangle(n0))
    print(pascalTriangle(n1))
    print(pascalTriangle(n3))
    print(pascalTriangle(n6))
  
# ==== Main
if __name__ == "__main__":
    Main()


