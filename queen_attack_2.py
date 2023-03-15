def queensAttack(n, k, r_q, c_q, obstacles):
    # n =  int n: the number of rows and columns in the board
    # k = nt k: the number of obstacles on the board
    # r_q = int r_q: the row number of the queen's position
    # c_q = int c_q: the column number of the queen's position     
    # obstacles = int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

    top = n - r_q
    bottom = r_q - 1
    left = c_q - 1
    right = n - c_q

    top_left = min(top, left)
    top_right =  min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)


    for i in obstacles:
        #bottom
        if i[0] < r_q and i[1] == c_q:
            bottom = min(bottom,(r_q - i[0]) - 1)
        #top
        if i[0] > r_q and i[1] == c_q:
            top = min(top, (i[0] - r_q) - 1)
        #left
        if i[1] < c_q and i[0] == r_q:
            left = min(left,(c_q - i[1]) - 1)         
        #right
        if i[1] > c_q and i[0] == r_q:
            right = min(right, (i[1] - c_q) - 1)
        ##top_left
        if i[0] > r_q and i[1] < c_q and abs(r_q - i[0]) == abs(c_q - i[1]):
            top_left = min(top_left, abs(r_q - i[0])-1)
        ##top_right
        if i[0] > r_q and i[1] > c_q and abs(i[0] - r_q) == abs(c_q - i[1]):
            top_right = min(top_right, abs(i[0] - r_q) -1)
        ##bottom_left
        if i[0] < r_q and i[1] < c_q and abs(r_q - i[0]) == abs(c_q - i[1]):
            bottom_left = min(bottom_left, abs(r_q - i[0])-1)   
        ##bottom_right
        if i[0] < r_q and i[1] > c_q and abs(i[0] - r_q) == abs(c_q - i[1]):
            bottom_right = min(bottom_right, abs(i[0] - r_q)-1)   

    n_squares = top + bottom + left + right + top_left + top_right + bottom_left + bottom_right
    return n_squares

print(queensAttack(4, 0, 4, 4, []))
print(queensAttack(5, 3, 4, 3, [[5,5],[4,2], [2,3]]))
print(queensAttack(8, 0, 4, 4, []))
print(queensAttack(8, 1, 4, 4, [[3,5]]))
print(queensAttack(8, 8, 4, 4, [[3,5],[6,6], [7,4], [7,1],[4,2],[2,2], [1,4], [4,7]]))

#9
#10
#27
#24
#11
