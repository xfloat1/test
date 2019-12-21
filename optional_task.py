points = []


def go(x, y, step=0):
    if step == 2:
        points.append(str(y) + str(x))

    else:
        if x > 1 and y > 2: go(x - 1, y - 2, step + 1)
        if x > 2 and y > 1: go(x - 2, y - 1, step + 1)

        if x < 8 and y > 2: go(x + 1, y - 2, step + 1)
        if x < 7 and y > 1: go(x + 2, y - 1, step + 1)

        if x < 7 and y < 8: go(x + 2, y + 1, step + 1)
        if x < 8 and y < 7: go(x + 1, y + 2, step + 1)

        if x > 1 and y < 7: go(x - 1, y + 2, step + 1)
        if x > 2 and y < 8: go(x - 2, y + 1, step + 1)


x0, y0 = list(input('Введите позицию коня: ').upper())
x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
y0 = int(y0)

go(x0, y0)

points = ["ABCDEFGH"[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]

print(*points)
