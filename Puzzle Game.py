# brief introduction
print('''
Welcome to this sliding puzzle program!
You need to choose either the 8 or 15-puzzle to play with!
You move the tiles with the keyboard using any 4 letters of your
own choice such as letters 'l', 'r', 'u', 'd' for left, right, up
and down moves respectively.
''')
while True:
    letters = input('Enter the 4 letters for left, right, up and down: ')
    lst = list(''.join(filter(str.isalpha, letters)))                      # ignore the items that are not letters
    direction = []
    for i in lst:
        if i not in direction:                                             # avoid repeated letters
            direction.append(i)
    if len(direction) == len(lst) == 4:                                    # make sure there are four letters
        break
    else:
        print('Please enter four different letters!')
        continue
left = direction[0]
right = direction[1]
up = direction[2]                                                         # the four letters correspond four directions
down = direction[3]
print('Use letters',left,right,up,'and',down,'for left, right, up and down moves.')

# global variable
time = 0                                          # the times of moving   

def end_the_game():
        end = 'Good bye!'
        return end
# print the puzzle in standard form
def print_puzzle(puzzle_list):
    n = 0
    for i in puzzle_list:
        n = n+1
        print('%4s'%i,end='')
        if n%N == 0:            # N numbers a line
            print('')
    return
# four directions to move
def move_up(i,N):
    global time
    puzzle_list[i],puzzle_list[i-N] = puzzle_list[i-N],puzzle_list[i]
    print_puzzle(puzzle_list)
    time+=1
def move_down(i,N):
    global time
    puzzle_list[i],puzzle_list[i+N] = puzzle_list[i+N],puzzle_list[i]
    print_puzzle(puzzle_list)
    time+=1
def move_left(i):
    global time
    puzzle_list[i],puzzle_list[i-1] = puzzle_list[i-1],puzzle_list[i]
    print_puzzle(puzzle_list)
    time+=1
def move_right(i):
    global time
    puzzle_list[i],puzzle_list[i+1] = puzzle_list[i+1],puzzle_list[i]
    print_puzzle(puzzle_list)
    time+=1
# there are nine ways to move
def move(puzzle_list):
    global time
    if puzzle_list.index(' ') == 0:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (down-'+down+',right-'+right+'): ')
            if direction == down:
                move_down(i,N)
                break
            elif direction == right:
                move_right(i)
                break
            else:
                continue
    elif 0 < puzzle_list.index(' ') < N-1:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (down-'+down+',right-'+right+',left-'+left+'): ')
            if direction == down:
                move_down(i,N)
                break   
            elif direction == right:
                move_right(i)
                break
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    elif puzzle_list.index(' ') == N-1:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (down-'+down+',left-'+left+'): ')
            if direction == down:
                move_down(i,N)
                break   
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    elif N-1 < puzzle_list.index(' ') < N+1 or N**2-2*N-1 < puzzle_list.index(' ') < N**2-2*N+1:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (down-'+down+',right-'+right+',up-'+up+'): ')
            if direction == down:
                move_down(i,N)
                break   
            elif direction == right:
                move_right(i)
                break
            elif direction == up:
                move_up(i,N)
                break
            else:
                continue
    elif 2*N-2 < puzzle_list.index(' ') < 2*N or N**2-N-2 < puzzle_list.index(' ') < N**2-N:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (down-'+down+',up'+up+',left-'+left+'): ')
            if direction == down:
                move_down(i,N)
                break   
            elif direction == up:
                move_up(i,N)
                break
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    elif puzzle_list.index(' ') == N**2-N:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (up-'+up+',right-'+right+'): ')
            if direction == up:
                move_up(i,N)
                break   
            elif direction == right:
                move_right(i)
                break
            else:
                continue
    elif N**2-N < puzzle_list.index(' ') < N**2-1:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (up-'+up+',right-'+right+',left-'+left+'): ')
            if direction == up:
                move_up(i,N)
                break   
            elif direction == right:
                move_right(i)
                break
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    elif puzzle_list.index(' ') == N**2-1:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (up-'+up+'left-,'+left+'): ')
            if direction == up:
                move_up(i,N)
                break   
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    else:
        i=puzzle_list.index(' ')
        while True:
            direction=input('Enter move (up-'+up+',down-'+down+',right-'+right+',left-'+left+'): ')
            if direction == up:
                move_up(i,N)
                break
            elif direction == down:
                move_down(i,N)
                break   
            elif direction == right:
                move_right(i)
                break
            elif direction == left:
                move_left(i)
                break
            else:
                continue
    return
# produce solvable puzzle list
def solvable(puzzle_list):
    import random
    if N == 3:
        while True:
            random.shuffle(puzzle_list)
            if inversion(puzzle_list)%2 == 0:
                solvable_list=puzzle_list
                break
            else:
                continue
    if N == 4:
        while True:
            random.shuffle(puzzle_list)
            if puzzle_list.index(' ') in [0,1,2,3,8,9,10,11]:
                if inversion(puzzle_list)%2 != 0:
                    solvable_list=puzzle_list
                    break
                else:
                    continue
            else:
                if inversion(puzzle_list)%2 == 0:
                    solvable_list=puzzle_list
                    break
                else:
                    continue
    puzzle_list=solvable_list
    return puzzle_list
# count the number of inversions
def inversion(puzzle_list):
    num=0
    no_space_list=list(puzzle_list)
    no_space_list.remove(' ')
    for i in no_space_list:
        for j in no_space_list[no_space_list.index(i):]:
            if i > j:
                num+=1
    return num

while True:
    choice = input('Enter 1 for 8-puuzle, 2 for 15-puzzle or q to end the game: ')
    if choice == 'q':
        print(end_the_game())
        break
    # 8-puzzle
    if choice == '1':
        N=3
        puzzle_list = ['1','2','3','4','5','6','7','8',' ']
        puzzle_list=solvable(puzzle_list)
        print_puzzle(puzzle_list)
        while True:
            if puzzle_list == ['1','2','3','4','5','6','7','8',' ']:
                print('Congratulations! You solved the puzzle in '+str(time)+' moves')
                break
            else:
                move(puzzle_list)
                continue
    # 15-puzzle
    if choice == '2':
        N=4
        puzzle_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',' ']
        puzzle_list=solvable(puzzle_list)
        print_puzzle(puzzle_list)
        while True:
            if puzzle_list == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',' ']:
                print('Congratulations! You solved the puzzle in '+str(time)+' moves')
                break
            else:
                move(puzzle_list)
                continue
    continue