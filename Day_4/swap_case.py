def swap_case(s):
    r = ''
    for letter in s:
        if letter == letter.upper():
            r += letter.lower()
        else:
            r += letter.upper() 
    return r

if __name__ == '__main__':