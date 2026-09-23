# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
a = set(map(int, input().split(" ")))

n = input()
b = set(map(int, input().split(" ")))

c = a.intersection(b)

ans = []

for i in a:
    if i not in c:
        ans.append(i)
        
for i in b:
    if i not in c:
        ans.append(i)
        
ans.sort()
for i in ans:
    print(i)
