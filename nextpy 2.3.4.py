# 2.3.4
################


class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x_coordinate = x
        self._y_coordinate = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x_coordinate = x
        self._y_coordinate = y

    def set_grayscale(self):
        avg = sum([self._red, self._green, self._blue])/3
        [self._red, self._green, self._blue] = map(lambda element: avg, [self._red, self._green, self._blue])

    def print_pixel_info(self):
        x_string = 'X: ' + str(self._x_coordinate) + ','
        y_string = 'Y: ' + str(self._y_coordinate) + ','
        color_string = 'Color: ' + '('
        red_string = str(self._red) + ', '
        green_string = str(self._green) + ', '
        blue_string = str(self._blue) + ') '
        if not (self._red + self._green) and self._blue:
            pure_color = 'BLUE'
        elif not (self._green + self._blue) and self._red:
            pure_color = 'RED'
        elif not (self._red + self._blue) and self._green:
            pure_color = 'GREEN'
        else:
            pure_color = ''
        print(x_string + y_string + color_string + red_string + green_string + blue_string + pure_color)


if __name__ == "__main__":
    my_pixel = Pixel()
    my_pixel.print_pixel_info()

    my_pixel._x_coordinate = 5

    my_pixel._red = 250
    my_pixel.print_pixel_info()

    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

