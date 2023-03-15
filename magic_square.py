s = [[5,3,4],[1,5,8],[6,4,2]]

magic_squares = [
    [[8,1,6],[3,5,7],[4,9,2]], 
    [[6,1,8],[7,5,3],[2,9,4]],
    [[4,9,2],[3,5,7],[8,1,6]],             
    [[2,9,4],[7,5,3],[6,1,8]],
    [[8,3,4],[1,5,9],[6,7,2]],
    [[4,3,8],[9,5,1],[2,7,6]],
    [[6,7,2],[1,5,9],[8,3,4]],
    [[2,7,6],[9,5,1],[4,3,8]]]


min_ops = float('inf')

for magic_square in magic_squares:
    ops = 0
    for i in range(3):
        for j in range(3):
            ops += abs(s[i][j] - magic_square[i][j])

    if ops < min_ops:
        min_ops = ops    

print(min_ops)



        






    