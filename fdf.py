import sfml as sf
import sys
import FDF2_next


def init_window(sprite, w):
    while w.is_open:
        for events in w.events:
            if type(events) is sf.CloseEvent:
                w.close()
            if type(events) is sf.KeyEvent:
                if events.code is sf.Keyboard.ESCAPE:
                    w.close()
        w.draw(sprite)
        w.display()


def draw_horizontal(img, tab, w, CST):
    compteur_x = 0
    compteur_y = 0
    for y in tab:
        for x in y:
            if compteur_x is not 0:
                x2 = CST * compteur_x - CST * compteur_y
                y2 = -int(x) * (CST + 0.3) + (CST / 2) * compteur_x + (CST / 2) * compteur_y
                array_x = [0, 0]
                array_y = [0, 0]
                array_x[0] = x1
                array_x[1] = x2
                array_y[0] = y1
                array_y[1] = y2
                FDF2_next.draw_line_1(img, array_x, array_y, w)
                FDF2_next.draw_line_2(img, array_x, array_y, w)
            y1 = -int(x) * (CST + 0.3) + (CST / 2) * compteur_x + (CST / 2) * compteur_y
            x1 = CST * compteur_x - CST * compteur_y
            compteur_x += w.width / len(tab[0])
        compteur_y += w.height / len(tab)
        compteur_x = 0


def draw_vertical(img, tab, w, CST):
    compteur_x = 0
    compteur_y = 0
    tab = FDF2_next.reverse(tab)
    for y in tab:
        for x in y:
            if compteur_x is not 0:
                x2 = CST * compteur_y - CST * compteur_x
                y2 = -int(x) * (CST + 0.3) + (CST / 2) * compteur_y + (CST / 2) * compteur_x
                array_x = [0, 0]
                array_y = [0, 0]
                array_x[0] = x1
                array_x[1] = x2
                array_y[0] = y1
                array_y[1] = y2
                FDF2_next.draw_line_2(img, array_x, array_y, w)
            y1 = -int(x) * (CST + 0.3) + (CST / 2) * compteur_y + (CST / 2) * compteur_x
            x1 = CST * compteur_y - CST * compteur_x
            compteur_x += w.width / len(tab[0])
        compteur_y += w.height / len(tab)
        compteur_x = 0


def init_drawing(tab, img, CST, w):
    draw_horizontal(img, tab, w, CST)
    draw_vertical(img, tab, w, CST)
    tex = sf.Texture.from_image(img)
    sprite = sf.Sprite(tex)
    init_window(sprite, w)


def main(CST):
    file_name = "elem2.fdf"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("File not valid.")
        exit()
    try:
        f = open(file_name, 'r')
    except IOError:
        print("Error opening file.")
        exit()
    lines = f.readlines()
    result = []
    for line in lines:
        tab = line.split()
        result.append(tab)
    if len(result) != len(result[0]):
        print("Tab is not a square.")
        exit()
    tab = result
    w = sf.RenderWindow(sf.VideoMode(666, 666), "FDF")
    img = sf.Image.create(666, 666, sf.Color(0, 0, 0))
    init_drawing(tab, img, CST, w)

main(0.5)
