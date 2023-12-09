with open('input.txt', 'r') as file:
    N = int(file.read().strip())

x, y = 0, 0
step = 0
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)] 

while step < N:
    dx, dy = direction[step // 2 % 4]  
    x += dx
    y += dy
    step += 1

with open('output.txt', 'w') as file:
    file.write(f"{x} {y}")
