def matrix(m,n,r,s,c,mat):
    if m==r-1 and n==c-1:
        return s 
    elif m==r-1 or n==c-1:
        if m==r-1:
            s+=mat[m][n+1]
            return matrix(m,n,s,r,c,mat)
        elif n==c-1:
            s+=mat[m+1][n]
            return matrix(m,n,s,r,c,mat)
            
            
    else:
        if mat[m+1][n]>mat[m][n+1]:
            s+=mat[m+1][n]
            return matrix(m,n,s,r,c,mat)
        elif mat[m+1][n]<=mat[m][n+1]:
            s+=mat[m][n+1]
            return matrix(m,n,s,r,c,mat)
    



r,c=map(int,input().split())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split()[:c])))
s=mat[0][0]
print(matrix(0,0,s,r,c,mat))
