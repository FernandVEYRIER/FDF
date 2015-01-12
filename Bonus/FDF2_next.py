import sfml as sf


def reverse(tab):
    new_tab = [([0] * len(tab[0])) for tableau in range(0, len(tab))]
    x = 0
    y1 = 0
    while x < len(tab[0]):
        y = 0
        x1 = 0
        while y < len(tab):
            new_tab[y1][x1] = tab[y][x]
            y += 1
            x1 += 1
        x += 1
        y1 += 1
    return new_tab


def draw_line_1(img, array_x, array_y, w):
    x1 = array_x[0]
    x2 = array_x[1]
    y1 = array_y[0]
    y2 = array_y[1]
    x = x1
    while x <= x2:
        if 0 < x + w.width / 2 < w.width and 0 < y1 + ((y2 - y1) * (x - x1)) / (x2 - x1) \
                + w.width / 2 - 100 < w.height:
            img[x + w.width / 2, y1 + ((y2 - y1) * (x - x1)) / (x2 - x1)
                + w.width / 2 - 100] = sf.Color.WHITE
        x += 1


def draw_line_2(img, array_x, array_y, w):
    x1 = array_x[0]
    x2 = array_x[1]
    y1 = array_y[0]
    y2 = array_y[1]
    y = y1
    while y <= y2:
        if 0 < x1 + ((x2 - x1) * (y - y1)) / (y2 - y1) + 333 < w.width \
                and 0 < y + 233 < w.height:
            img[x1 + ((x2 - x1) * (y - y1)) / (y2 - y1) + 333, y + 233] = sf.Color.WHITE
        y += 1
    x = x1
    while x >= x2:
        if 0 < x + 333 < w.width and 0 < y1 + ((y2 - y1)
                                     * (x - x1)) / (x2 - x1) + 233 < w.height:
            img[x + 333, y1 + ((y2 - y1) * (x - x1)) / (x2 - x1) + 233] = sf.Color.WHITE
        x -= 1