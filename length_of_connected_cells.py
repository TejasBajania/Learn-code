# Finding length of connected cells of 1s (regions) in a matrix of 0s and 1s

# Sample input : [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[1,0,0,0,0],[0,1,0,1,1]]
# Expected output: 5

def get_val(A,i,j, L, H):

    if i<0 or i >= L or j > 0 or j >= H :
        return 0
    else:
        return A[i][j]
    

def find_max_block(A,r,c,L,H,size):

    global maxsize
    global cntrr

    if r >= L or c >= H :

        return
    
    cntrr[r][c] = 1 
    size +=1
    if size > maxsize:
        maxsize = size
    # Search in eight directions
    
    directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

    for i in range(0,7):

        newi = r+directions[i][0]
        newj = c+directions[i][1]
        val = get_val(A,newi,newj,L,H)
        if val > 0 and cntrr[newi][newj] == 0:
            find_max_block(A,newi, newj,L,H, size)     
    
    cntrr[c][r] = 0 

def get_max_ones(A,rmax,colmax):

    global maxsize
    global size
    global cntrr
    for i in range(0,rmax):
        for j in range(0,colmax):

            if A[i][j] == 1:
                find_max_block(A,i,j,rmax, colmax, 0)
    return maxsize
zarr = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[0,0,0,1,1],[0,1,0,1,1]]

rmax = 5
colmax = 5 
maxsize = 0 
size = 0
cntrr = rmax * [colmax * [0]]
print('Number of 1\'s are')
print(get_max_ones(zarr, rmax, colmax))

