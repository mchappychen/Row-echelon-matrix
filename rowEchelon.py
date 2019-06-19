def multiply(a,b): #returns: [] of a x b[]
    if(a == 0):
        exit("Error in multiply(): You can't multiply matrix by 0")
    result = []
    for element in b:
        result.append(round(element * a,2))
    return result

def add(a,b): #returns [] of a[]+b[]
    result = []
    if(len(a) != len(b)):
        exit("Error in add(a,b): length of a[] not equal to length of b[]")
    for i in range(len(a)):
        result.append(round(a[i]+b[i],2))
    return result

def printMatrix(a): #prints a matrix
    for x in a:
        string = "|\t"
        for y in x:
            string += str(round(y,2)+0)+"\t"
        string += "|"
        print(string)
    print("")

def rowEchelon(a):
    """Plan:
        1. Start with pivot at a[i][j] where i=0 and j=0
        2. If it's 0, switch it with a row below where pivot won't become 0
            If all the rows below pivot are 0, increase j by 1, and repeat
        3. Multiply row i by 1/pivot to make pivot = 1
        4. Turn every element below the pivot (in column j) into 0
        5. Increase i and j by 1, repeat until j reaches out of range
    """
    i = 0 #1
    j = 0
    while(j < len(a[0])):
        operate = True
        if(a[i][j] == 0): #2 If it's 0, switch it with a row below where pivot won't become 0
            switched = False
            for x in range(i+1,len(a)):
                if(a[x][j] != 0):
                    temp = a[x].copy()
                    a[x] = a[i].copy()
                    a[i] = temp.copy()
                    switched = True
                    break
            if(not switched):
                j += 1
                operate = False
        if(operate):
            #3 Multiply row i by 1/pivot to make pivot = 1
            a[i] = multiply(1.0/a[i][j] , a[i])
            #4 Turn every element below the pivot (in column j) into 0
            for x in range (i+1,len(a)):
                if(a[x][j] != 0):
                    a[x] = add(multiply(-1 * a[x][j],a[i]),a[x])
            i += 1 #5
            j += 1
    return a

def checkMatrix(a): #checks if a[] is in correct format
    for x in range(len(a)):
        for y in range(len(x)):
            try:
                if(a[x][y] == None):
                    print("Error in checkMatrix(): (",x,",",y,") is empty")
                    return False
            except IndexError:
                print("Error in checkMatrix(): (",x,",",y,") is missing, matrix is not rectangle")
                return False
    return True
    
def main():
    """Plan:
        1. Give user option to input matrix manually, automatically, or exit
        2. Give user option to specifiy rows and columns (m,n)
        3. Call rowEchelon(a)
    """
    m = 0 #rows
    n = 0 #columns
    goodInput = False
    userInput = ""
    while(not goodInput): #1 Give user option to input matrix manually, automatically, or exit
        userInput = input("Type '1' for manual input, '2' for auto-input, '3' to exit :: ")
        if(userInput == '1'):
            goodInput = True
            userInput = "manual"
        elif(userInput == '2'):
            goodInput = True
            userInput = "auto"
        elif(userInput == '3'):
            goodInput = True
            return None
        else:
            print("Only enter 1, 2 or 3 you idiot, learn to read.")
    goodInput = False
    while(not goodInput): #2 Give user option to specify rows and columns (m,n)
        try:
            m = int(input("Enter rows :: "))
            if(not m>0):
                m = int("beef")
            goodInput = True
        except ValueError:
            print("Type in a positive natural number idiot, use your head")
    goodInput = False
    while(not goodInput):
        try:
            n = int(input("Enter columns :: "))
            if(not n>0):
                n = int("beef")
            goodInput = True
        except ValueError:
            print("Type in a positive natural number idiot, use your head")
    if(userInput == "manual"):
        matrix = []
        for x in range(m):
            row = []
            for y in range(n):
                goodInput = False
                while(not goodInput):
                    try:
                        row.append(float(input("Enter number :: ")))
                        goodInput = True
                    except ValueError:
                        print("Type in a number idiot, learn to read") 
            matrix.append(row)
        checkMatrix(matrix)
        print("\nMatrix looks like:")
        printMatrix(matrix)
        print("Row-Echelon matrix looks like:")
        printMatrix(rowEchelon(matrix)) #3 Call rowEchelon()
    elif(userInput == "auto"):
        pass
    else:
        print("Error in main(): This line should not have been executed")
        return None
    
if __name__ == "__main__":
    main()
