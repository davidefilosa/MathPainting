from main import Canvas, Square, Rectangle

while True:
    try:
        canvas_width = int(input('Enter canvas width: '))
        canvas_height = int(input('Enter a canvas height: '))
    except ValueError:
        print('Width and height must be numbers')
        continue
    canvas_color = input('Enter a canvas color (black or white): ')
    if canvas_color == 'black' or canvas_color == 'white':
        canvas = Canvas(canvas_width, canvas_height, canvas_color)
        canvas.make('canvas')
        break
    else:
        print('Canvas color must be black or white')
        continue

while True:
    shape = input('What would you like to draw? (rectangle or square) Enter quit to quit ')
    if shape == 'quit':
        break
    elif shape == 'rectangle':
        try:
            x = int(input('Enter the x: '))
            y = int(input('Enter the y: '))
            width = int(input('Enter the width: '))
            height = int(input('Enter the height: '))
            r = int(input('How much red? Enter a number from 0 to 255: '))
            g = int(input('How much green? Enter a number from 0 to 255: '))
            b = int(input('How much blue? Enter a number from 0 to 255: '))
            rectangle = Rectangle(x, y, width, height, [r, g, b])
            rectangle.draw('canvas')
        except ValueError:
            print('You must enter a numbers')
            continue
    elif shape == 'square':
        try:
            x = int(input('Enter the x: '))
            y = int(input('Enter the y: '))
            side = int(input('Enter the side length: '))
            r = int(input('How much red? Enter a number from 0 to 255: '))
            g = int(input('How much green? Enter a number from 0 to 255: '))
            b = int(input('How much blue? Enter a number from 0 to 255: '))
            square = Square(x, y, side, [r, g, b])
            square.draw('canvas')
        except ValueError:
            print('You must enter a numbers')
            continue
    else:
        continue





