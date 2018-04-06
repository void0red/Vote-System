from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from hashlib import md5

def get_md5(tar):
    return md5(bytes(str(tar), encoding='utf-8')).hexdigest()

def rand_char():
    i = random.randint(1, 3)
    if i == 1:
        an = random.randint(97, 122)
    elif i == 2:
        an = random.randint(65, 90)
    else:
        an = random.randint(48, 57)
    return chr(an)


def rand_dis():
    d = ['^', '-', '~', '_', '.']
    i = random.randint(0, len(d)-1)
    return d[i]


def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create(width=60 * 4, height=60, num=4):
    image = Image.new('RGB', (width, height), (192, 192, 192))
    font = ImageFont.truetype('static/fonts/arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(0, width, 20):
        for y in range(0, height, 10):
            draw.point((x, y), fill=rand_color())
    _str = ''
    for t in range(num):
        c = rand_char()
        _str = '{}{}'.format(_str, c)
        h = random.randint(1, height-30)
        w = width/num * t + 10
        draw.text((w, h), c, font=font, fill=rand_color2())
        for j in range(0, width, 30):
            dis = rand_dis()
            w = t * 15 + j
            h = random.randint(1, height-30)
            draw.text((w, h), dis, font=font, fill=rand_color())
    image.filter(ImageFilter.BLUR)
    image.save('static/pic/verify.png', 'png')
    return _str


def check(x1, x2):
    tmp = get_md5(x1.upper())[0:5]
    if tmp == x2:
        return True
    else:
        return False
