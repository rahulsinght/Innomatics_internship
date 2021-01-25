def split_and_join(line):
    r = '-'.join(line.split(' '))
    return r

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)