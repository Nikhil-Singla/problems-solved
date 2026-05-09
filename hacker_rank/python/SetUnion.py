# Enter your code here. Read input from STDIN. Print output to STDOUT
input()

val = list(map(int, input().rstrip().split()))
a = set(val)

input()

val = list(map(int, input().rstrip().split()))
a.update(set(val))

print(len(a))
