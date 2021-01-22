n=int(input())
a=set()
if 0<n<1000:
    for i in range(n):
        a.add(input())
print(len(a))