from PIL import Image


def image_filter(pixels, i, j):
    """Заменяет цвет исходного пикселя на усредненное относительно его окружения на 4 пикселя и увеличивает контраст"""
    global width, height
    r, g, b = 0, 0, 0
    for row in range(i - 4 if width >= i - 4 else width, i + 4 if width >= i + 4 else width):  
        for col in range(j - 4 if height >= j - 4 else height, j + 4 if height >= j + 4 else height):  
            if row != i and col != j:  
                r += pixels[row, col][0]
                g += pixels[row, col][1]  
                b += pixels[row, col][2]
    return min(int(r * 1.1 / 50), 255), min(int(g * 1.1 / 50), 255), min(int(b * 1.1 / 50), 255)

# im = Image.open("image.jpg")
# pixels = im.load()
# width, height = im.size
# for i in range(width):  
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = image_filter(pixels, i, j)

# im.show()