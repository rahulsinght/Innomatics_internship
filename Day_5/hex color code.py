for _ in range(int(input())):
    hexcodes = re.findall(r'(?<!^)(#[0-9a-f]{6}|#[0-9a-f]{3})',input(),re.I)
    
    for hexcode in hexcodes:
        print(hexcode)