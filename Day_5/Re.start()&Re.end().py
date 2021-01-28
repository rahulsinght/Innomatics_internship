# Enter your code here. Read input from STDIN. Print output to STDOUT 
import re
str1 = input()
str2 = input()
p = re.compile(str2)
m = p.search(str1)
if not m:
    print((-1,-1))
else:
    while m:
        print((m.start(), m.end()-1))
        m = p.search(str1, m.start()+1)

        
