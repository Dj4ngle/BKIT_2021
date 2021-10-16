from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import os
import pandas as pd

N = 20

def main():


    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    print()
    

    tab = pd.DataFrame(
        { "Фигура": [r.get_name, c.get_name, s.get_name], 
        "Цвет": [r.fc.colorproperty, c.fc.colorproperty, s.fc.colorproperty], 
        "Высота": [r.height, '-', s.height], 
        "Ширина": [r.width, '-', s.width],
        "Радиус": ['-', c.r, '-'],
        "Площадь": [r.square(), c.square(), s.square()]
        }) 
    print(tab)

if __name__ == "__main__":
    main()

os.system('pause')
