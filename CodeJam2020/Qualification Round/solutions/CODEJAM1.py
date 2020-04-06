import numpy as np
def solve(n,mat):
    k = mat.trace()
    repro, repcol = 0, 0
    for i in range(n):
        row = list(set(mat[i]))
        col = list(set(mat[:,i]))
        if len(row)<n:
            repro += 1
        if len(col)<n:
            repcol += 1
        
    return (k,repro,repcol)


tests = int(input())
mem = []
for x in range(1,tests+1):
    n = int(input())
    mat = []
    for i in range(n):
        row = list(map(int,input().split()))
        mat.append(row)
    mat = np.array(mat)
    k,r,c = solve(n,mat)
    mem.append([x,k,r,c])
for i in range(tests):
    x,k,r,c = mem[i]
    print("Case #{0}: {1} {2} {3}".format(x,k,r,c))
