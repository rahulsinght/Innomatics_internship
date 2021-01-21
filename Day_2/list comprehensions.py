if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x += 1
    y += 1
    z += 1
    
    l = [[X,Y,Z] for X in range (x) for Y in range (y) for Z in range (z) if X+Y+Z != n ]
    print(l)

 

