def hanoi(n, source, spare, target):
    if n == 0:
        #no disks left
        return

    global count
    count += 1

    # move n-1 discs from source to spare
    hanoi(n-1, source, target, spare)

    if source:
        # move disc from source to target
        target.append(source.pop())
        print(tower_A, tower_B, tower_C)

    # move n-1 discs from spare to target
    hanoi(n-1, spare, source, target)

n = 3
tower_A = list(range(n,0,-1)) #source tower
tower_B, tower_C = [], [] #spare and target towers

print(tower_A, tower_B, tower_C)
count = 0
hanoi(n, tower_A, tower_B, tower_C) #call function and let recurrsion solve the problem
print( "number of steps taken to solve",count)