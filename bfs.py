from PIL import Image, ImageDraw


a = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

zoom = 20
borders = 6
images = []

def draw_matrix(a, m, the_path=[]):
    im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == start_j and j == start_j:
                color = (0, 255, 0)
                r = borders
            if i == end_i and j == end_j:
                color = (0, 255, 0)
                r = borders
            draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)
            if m[i][j] > 0:
                r = borders
                draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                               fill=(128, 128, 128))
    for u in range(len(the_path)-1):
        y = the_path[u][0]*zoom + int(zoom/2)
        x = the_path[u][1]*zoom + int(zoom/2)
        y1 = the_path[u+1][0]*zoom + int(zoom/2)
        x1 = the_path[u+1][1]*zoom + int(zoom/2)
        draw.line((x,y,x1,y1), fill=(255, 0, 0), width=5)
    draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0, 255, 0), width=2)
    images.append(im)




def printer(matr, lab):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            num = matr[i][j]
            if num > 0:
                print(f"{num:3}", end=" ")
            else:
                if lab[i][j] == 1:
                    print(f"...", end=" ")
                else:
                    print(f"   ", end=" ")

        print()


def step(k,a,m):
    changed = False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if m[i][j] == k:
                if j < len(a[i])-1 and a[i][j+1] == 0 and m[i][j+1] == 0:  # Right
                    m[i][j+1] = k+1
                    changed = True
                if j > 0 and a[i][j-1] == 0 and m[i][j-1] == 0:  # Left
                    m[i][j-1] = k+1
                    changed = True
                if i < len(a)-1 and a[i+1][j] == 0 and m[i+1][j] == 0:  # Down
                    m[i+1][j] = k+1
                    changed = True
                if i > 0 and a[i-1][j] == 0 and m[i-1][j] == 0:  # Up
                    m[i-1][j] = k+1
                    changed = True
    return changed

m = []
for i in range(len(a)):
    m.append([0 for i in range(len(a[i]))])

start_i = 1
start_j = 1
end_i = 1
end_j = len(a[0])-2

m[start_i][start_j] = 1

changed = True
k = 0
while changed and m[end_i][end_j] == 0:
    k += 1
    changed = step(k, a, m)
    draw_matrix(a,m,[])


if m[end_i][end_j] > 0:
    print(f"Found! We can get there in {m[end_i][end_j]} steps!")
    k = m[end_i][end_j]
    i,j = end_i, end_j
    path = [(i,j)]
    while k > 1:
        if j < len(a[i]) - 1 and m[i][j + 1] == k-1:  # Right
            j = j + 1
        elif j > 0 and m[i][j - 1] == k-1:  # Left
            j = j - 1
        elif i < len(a) - 1 and m[i + 1][j] == k-1:  # Down
            i = i + 1
        elif i > 0 and m[i - 1][j] == k-1:  # Up
            i = i - 1
        path.append((i,j))
        k -= 1
        draw_matrix(a, m, path)
    print("Path:", path)

    for i in range(10):
        draw_matrix(a, m, path)
else:
    print("No way")

printer(m,a)

images[0].save('maze.gif',
               save_all=True, append_images=images[0:],
               optimize=False, duration=50, loop=0)

