def done_or_not(board): 
    xmp=[n for n in range (1,10)]
    cont=0
    trp=[[0 for x in range(9)]for y in range(9)]
    sqr=[[]for y in range(9)]
    
    for i in range(9):
        for j in range(9):
            trp[i][j]=board[j][i]
            if i<3:
                if j<3:
                    sqr[0].append(board[i][j])
                elif j<6:
                    sqr[1].append(board[i][j])
                elif j<9:
                    sqr[2].append(board[i][j])
            elif i<6:
                if j<3:
                    sqr[3].append(board[i][j])
                elif j<6:
                    sqr[4].append(board[i][j])
                elif j<9:
                    sqr[5].append(board[i][j])
            elif i<9:
                if j<3:
                    sqr[6].append(board[i][j])
                elif j<6:
                    sqr[7].append(board[i][j])
                elif j<9:
                    sqr[8].append(board[i][j])
    
    for i in range(9):
        if sorted(board[i])==xmp and sorted(trp[i])== xmp and sorted(sqr[i])==xmp:
            cont+=1
    
    if cont==9:
        return "Finished!"
    else:
        return "Try again!"
