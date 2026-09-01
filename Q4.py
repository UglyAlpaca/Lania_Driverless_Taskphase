import sys
def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        print("number of columns in first matrix must be equal to number of rows in second matrix")
        exit()

    result = []

    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            pro = 0

            for k in range(len(B)):
                pro += (A[i][k] * B[k][j])

            row.append(pro)

        result.append(row)

    return result

# Input first matrix
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

A = []

for i in range(r1):
    row = []
    print("Enter the {} elements of row {}: ".format(c1, i + 1))
    for j in range(c1):
        row.append(int(input()))

    A.append(row)

# Input second matrix
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))
    
B = []

for i in range(r2):
    row = []
    print("Enter the {} elements of row {}: ".format(c2, i + 1))
    for j in range(c2):
        row.append(int(input()))

    B.append(row)

print("The first matrix is:\n")
#print first matrix    
for row in A:
    print(row)

print("The second matrix is:\n")
#print second matrix    
for row in B:
    print(row)

print("The resultant matrix is:\n")
#print resultant matrix
result = matrix_multiply(A, B)

for row in result:
    print(row)
