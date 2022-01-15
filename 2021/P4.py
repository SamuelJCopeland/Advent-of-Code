def print_winner(board_num, board, marker, last):
    print("We have a winner!\t" + str(board_num))
    total = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if marker[i][j] == "":
                total += int(board[i][j])
    total *= last
    print(total)

with open("P4.txt", "r") as file:
    first = True
    numbers = []
    markers = []
    boards = []
    board = []
    marker = []
    n = 0
    for line in file:
        if first:
            first = False
            numbers = line[:-1].split(",")
        elif line == "\n":
            if len(board) > 0:
                boards.append(board)
                markers.append(marker)
            board = []
            marker = []
            n = 0
        else:
            board.append(line[:-1].split())
            marker.append([])
            for i in range(0, len(board[n])):
                marker[n].append("")
            n += 1
    winning_board = 1000
    winners = []
    winner = False
    for i in numbers:
        board_num = 0
        for b in boards:
            line_num = 0
            for l in b:
                for j in range(0, 5):
                    if l[j] == i:
                        markers[board_num][line_num][j] = "*"
                        winnner = True
                        #Check horizontal
                        for a in range(0, 5):
                            if markers[board_num][line_num][a] != "*":
                                winner = False
                                break
                        if winner:
                            winnning_board = board_num
                            print_winner(board_num, boards[board_num], markers[board_num], int(i))
                        #Check vertical
                        winner = True
                        for a in range(0, 5):
                            if markers[board_num][a][j] != "*":
                                winner = False
                                break
                        
                        if winner:
                            winnning_board = board_num
                            winners.append(board_num)
                            print_winner(board_num, boards[board_num], markers[board_num], int(i))
                            winner = False
                        break
                line_num += 1
            board_num += 1
        winners = sorted(winners, reverse=True) 
        for w in winners:
            boards.pop(w)
            markers.pop(w)
        print(len(boards))
        winners = []
        
    