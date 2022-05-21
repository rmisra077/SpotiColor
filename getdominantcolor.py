from fengspct import ColorThief

def get_major_color(img):
    ct = ColorThief(img)

    return ct.get_color()