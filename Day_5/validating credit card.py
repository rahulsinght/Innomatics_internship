N = int(input())
import re

cons = re.compile(r"(\d)(\1){3}")
f = re.compile(r"\d{4}\-?\d{4}\-?\d{4}\-?\d{4}")

for _ in range(N):
    n = input()
    if len(n) != 16 and len(n) != 19:
        print("Invalid")
        continue
    if n[0] not in "456":
        print("Invalid")
        continue
        
    if not f.match(n):
        print("Invalid")
        continue
        
    n = n.replace("-", "")
        
    if cons.search(n):
        print("Invalid")
        continue
        
    print("Valid")
        
  
    
    