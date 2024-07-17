num = 8
ways = (2**num) - 1

column = {
    'A':list(range(num, 0, -1)),
    'B':[],
    'C':[]
}
 
def move(r1, r2):
    forward = False
    if not column[r2]:
        forward = True
    elif column[r1] and column[r1][-1] < column[r2][-1]:
        forward = True
    if forward == True:
        print(f'move disk {column[r1][-1]} from {r1} to {r2}')
        column[r2].append(column[r1].pop())
    else:
        print(f'move disk {column[r2][-1]} from {r2} to {r1}')
        column[r1].append(column[r2].pop())
    print(column, '\n')


def col(new, start, by, target):
    for item in range(ways):
        rem = (item + 1) % 3
        if rem == 0:
            if new % 2 != 0:
                print(f'move {item + 1} allowed {by} to {target}')
                move(by, target)
            else:
                print(f'move {item + 1} allowed {by} to {target}')
                move(by, target)
        elif rem == 1:
            if new % 2 != 0:
                print(f'move {item + 1} allowed {start} to {target}')
                move(start, target)
            else:
                print(f'move {item + 1} allowed {start} to {by}')
                move(start, by)
        elif rem == 2: 
            if new % 2 != 0:
                print(f'move {item + 1} allowed {start} to {by}')
                move(start, by)
            else:
                print(f'move {item + 1} allowed {start} to {target}')
                move(start, target)

#col(num, 'A', 'B', 'C')

A = list(range(num, 0, -1))
B = []
C = []
def move(n, begin, tour, end):
    if n <= 0:
        return
    move(n-1, begin, end, tour)
    end.append(begin.pop())
    print(f'{A}, {B}, {C}')
    move(n-1, tour, begin, end)


move(num, A, B, C)