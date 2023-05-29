import numpy as np
import cv2
from PIL import Image

def rgb_of_pixel(img_path, x, y):
    img = Image.open(img_path).convert('RGB')
    r, g, b = img.getpixel((x, y))

    color = (r, g, b)
    return color

image_path = 'photo1.jpg'

image_file = cv2.imread(image_path)

image_width = image_file.shape[0]
image_height = image_file.shape[1]

array_css = []
array_html = []

contador = 0

array_html.append('<!DOCTYPE html>\n')
array_html.append('<html lang="en">\n')
array_html.append('<head>\n')
array_html.append('<meta charset="UTF-8">\n')
array_html.append('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
array_html.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
array_html.append('<title>Foto</title>\n')
array_html.append('<link rel="stylesheet" href="style.css">')
array_html.append('</head>\n')
array_html.append('<body>\n')

array_css.append('* { margin: 0; padding: 0; border: 0; box-sizing: border-box; }')
array_css.append('html, body { height: 100vh; width: 100vw; }')
array_css.append('body { display: flex; flex-direction: row; }')

for x in range(image_height):
    div_linha = '<div class="linha-{0}">\n'.format(x)

    array_html.append(div_linha)

    for y in range(image_width):
        div_pixel = '<div class="pixel-{0}"></div>\n'.format(contador)
        array_html.append(div_pixel)

        color_pixel = rgb_of_pixel(image_path, x, y)

        print('Posição no X: {0} | Posição no Y: {1}'.format(x, y))

        css_color = '.pixel-{0} (width: 1px; height: 1px; background-color: rgb{1};)\n'.format(contador, color_pixel)
        array_css.append(css_color)

        contador += 1
    
    array_html.append('</div>')
    array_html.append('\n')
    array_css.append('\n')

array_html.append('</body>')
array_html.append('</html>')

with open('index.html', 'w') as file:
    file.writelines(array_html)

with open('style.css', 'w') as file:
    file.writelines(array_css)
