if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    if len(tup) <= n:
        print(hash(tup))
    
