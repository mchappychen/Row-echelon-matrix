Start with i = 1, j = 1.
1. If aij = 0 swap the i-th row with some other row below to guarantee that a[i][j] = 0.
The non-zero entry in the (i, j)-position is called a pivot. If all entries in the column
are zero, increase j by 1.
2. Divide the i-th row by aij to make the pivot entry = 1.
3. Eliminate all other entries in the j-th column by subtracting suitable multiples of the
i-th row from the other rows.
4. Increase i by 1 and j by 1 to choose the new pivot element. Return to Step 1.
The algorithm stops after we process the last row or the last column of the matrix

https://www.csun.edu/~panferov/math262/262_rref.pdf
