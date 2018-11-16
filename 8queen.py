import random
import copy

def rand_pos():
    seq = []
    while len(seq) <= 8:
        x,y = len(seq)-1,random.randint(0,7)
        #if state not in seq:
        seq.append((x,y))
    return seq

def restart_state():
    seq = rand_pos()
    state = []
    for i in range(8):
        state.append([0]*8)
    for positions in seq:
        state[positions[0]][positions[1]] = 1
    return state

def calc_cost(board):
    totalhcost = 0
    totaldcost = 0
    for i in range(0,8):
      for j in range(0,8):
        if board[i][j] == 1:
          totalhcost -= 2
          for k in range(0,8):
            if board[i][k] == 1:
              totalhcost += 1
            if board[k][j] == 1:
              totalhcost += 1
          k, l = i+1, j+1
          while k < 8 and l < 8:
            if board[k][l] == 1:
              totaldcost += 1
            k +=1
            l +=1
          k, l = i+1, j-1
          while k < 8 and l >= 0:
            if board[k][l] == 1:
              totaldcost += 1
            k +=1
            l -=1
          k, l = i-1, j+1
          while k >= 0 and l < 8:
            if board[k][l] == 1:
              totaldcost += 1
            k -=1
            l +=1
          k, l = i-1, j-1
          while k >= 0 and l >= 0:
            if board[k][l] == 1:
              totaldcost += 1
            k -=1
            l -=1
    return ((totaldcost + totalhcost)/2)

def new_state(board):
    current_cost = calc_cost(board)
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                for x in range(8):
                    #for y in range(8):
                    new_board = copy.deepcopy(board)
                    new_board[i][j],new_board[i][x] = 0,1
                    if calc_cost(new_board) < current_cost:
                        board = new_board
    return board

    
def print_state(state):
    for x in state:
        print(x)

board = restart_state()
print_state(board)
print('Initail Cost: ',calc_cost(board))
starting_cost = calc_cost(board)
restart = 0
changes = 0
last = 0
while True:    
    new_board = new_state(board)
    if calc_cost(new_board) == 0:
        print('Restarts: ',restart)
        print('Changes In Last Restart: ',last)
        print('Total Changes: ',changes)
        print_state(new_board)
        print('Final Cost: ',calc_cost(new_board))
        break
    if starting_cost == calc_cost(new_board):
        board = restart_state()
        restart += 1
        last = 0
    else:
        starting_cost = calc_cost(new_board)
        board = new_board
        last += 1
        changes += 1
        

    
