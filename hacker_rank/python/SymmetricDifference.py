# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
a = set(map(int, input().split(" ")))

n = input()
b = set(map(int, input().split(" ")))

c = a.intersection(b)

ans = []

ans = list(a.difference(c))
ans.extend(list(b.difference(c)))

ans.sort()

for i in ans:
    print(i)
