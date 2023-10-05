a, b, c = map(int, input().split())
if a <= b <= c or c <= b <= a:
    median = b
elif b <= a <= c or c <= a <= b:
    median = a
else:
    median = c
print(median)
