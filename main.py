import numpy as np
from PIL import Image


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        with Image.open(f'{canvas}.png') as image:
            data = np.asarray(image)
            data = data.copy()
            data[self.y:self.y+self.side, self.x:self.x+self.side] = self.color
            img = Image.fromarray(data, 'RGB')
            img.save(f'{canvas}.png')



class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        with Image.open(f'{canvas}.png') as image:
            data = np.asarray(image)
            data = data.copy()
            data[self.y:self.y + self.height, self.x:self.x + self.width] = self.color
            img = Image.fromarray(data, 'RGB')
            img.save(f'{canvas}.png')


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        if self.color == 'white':
            data[:] = [255, 255, 255]
        img = Image.fromarray(data, 'RGB')
        img.save(f'{imagepath}.png')
