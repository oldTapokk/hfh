class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.year = year
        self.color = color
    def show_info(self):
        print('model:', self.model)
        print('year:', self.year)
        print('color:', self.color)

    def set_color(self, newColor):
        self.color = newColor


myCar = Car('audi', '2021', 'red')
myCar.color = 'red'
myCar.show_info()

myCar2 = Car('lamborgini', '1986', 'black')
myCar2.color = 'black'
myCar2.show_info()