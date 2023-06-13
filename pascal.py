'''n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in  range(i+1):
        print("*",end=" ")
    print()'''

def generate(numRows):
    a=[[] for i in range(numRows)]
    for i in range(numRows):
        for j in range(i+1):
            if i<j:
                if j==0:
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j==i):
                a.append(1)
    return a
numRows=5
generate(numRows)
    