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
        else: #3 Multiply row i by 1/pivot to make pivot = 1
            a[i] = multiply(1.0/a[i][j] , a[i])
            #4 Turn every element below the pivot (in column j) into 0
            
def main():
    """Plan:
        1. Give user option to input matrix manually, automatically, or exit
        2. Matrix inputted should be rounded to 2 decimals
    """
    print("Hi idiot")
    
if __name__ == "__main__":
    main()
