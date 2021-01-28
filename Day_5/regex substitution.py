# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def convert(match):
    if match.group(0) == '&&':
        return 'and'
    return 'or'
T = int(input())
for _ in range(T):
    s = input()
    print(re.sub(r"(?<= )((&&)|(\|\|))(?= )", convert, s))
    
    
  