from PIL import Image, ImageDraw
# Depth-First Search

a = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

start_i = 1
start_j = 1
end_i = 7
end_j = 12

zoom = 20
borders = 6
images = []

def draw_matrix(a, the_path=[]):
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
            if a[i][j] == 2:
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



path = []
def goto(i,j):
    global path, end_i, end_j, a
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a[i])-1:
        return
    if (i,j) in path or a[i][j] > 0:
        return
    path.append((i,j))
    a[i][j] = 2
    draw_matrix(a, path)
    if (i,j) == (end_i, end_j):
        print("Found!!!", path)
        for animate in range(10):
            if animate%2 == 0:
                draw_matrix(a)
            else:
                draw_matrix(a,path)
        path.pop()
        return
    else:
        goto(i-1, j)
        goto(i+1, j)
        goto(i, j+1)
        goto(i, j-1)
    path.pop()
    draw_matrix(a,path)
    return


goto(start_i, start_j)

images[0].save('maze.gif',
               save_all=True, append_images=images[1:],
               optimize=False, duration=60, loop=0)


