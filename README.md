# first_script
This script is a very easy script that just for choose a `account` that sees not bad.

###### 补充生成验证码程序
'''
# coding:utf-8
'''
Created on 2017年8月22日
@author: Administrator
'''

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

_letter_cases = 'abcdefghjkmnpqrstuvwxy'
_upper_cases = _letter_cases.upper()
_numbers = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))


def creat_validata_code(size=(120, 30), chars=init_chars, img_type='jpg',
                        mode='RGB', bg_color=(255, 255, 255), fg_color=(0, 0, 255),
                        font_size=16, font_type='arial.ttf',
                        length=6, draw_lines=False, n_line=(1, 2),
                        draw_points=False, point_chance=2):
    width, height = size;
    img = Image.new(mode, size, bg_color)

    draw = ImageDraw.Draw(img)

    def get_chars():
        return random.sample(chars, length)

    def creat_line():
        line_num = random.randint(*n_line)  # sign that the param is a list

        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                  strs, font=font, fill=fg_color)
        return ''.join(c_chars)

    if draw_lines:
        creat_line()
    if draw_points:
        create_points()
    strs = create_strs()

    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, strs

from io import BytesIO
img, strs = creat_validata_code()
jpeg_image_buffer = BytesIO()
img.save(jpeg_image_buffer, format="png")
## (jpeg_image_buffer.getvalue()) 可以直接作为一个 img 对象传出了
with open("a.png", "wb") as f:
    f.write((jpeg_image_buffer.getvalue()))
    f.close()

print(strs)
'''

