import sys
import math
import os


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    try:
        coef = float(coef_str)
    except ValueError:
        print('У вас ошибка, попробуйте ввести правильные данные(число)')
        return get_coef(index, prompt)
    return coef

 


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    
    result = []
    if a == 0:
        if b != 0:
            root = -c / b
            if root == 0:
                result.append(root)
            elif root > 0:
                result.append(-round(math.sqrt(root), 2))
                result.append(round(math.sqrt(root), 2))
        return result
    D = b*b -4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root == 0:
            result.append(root)
        elif root > 0:
            result.append(-round(math.sqrt(root), 2))
            result.append(round(math.sqrt(root), 2))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        if root1 == 0.0:
            result.append(root1)
        elif root1 > 0.0:
            result.append(-round(math.sqrt(root1), 2))
            result.append(round(math.sqrt(root1), 2))
        if root2 == 0.0:
            result.append(root2)
        elif root2 > 0.0:
            result.append(-round(math.sqrt(root2), 2))
            result.append(round(math.sqrt(root2), 2))
    return result        

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a == 0 and b == 0 and c == 0:
        print('Бесконечное число корней')
    else:
        # Вычисление корней
        roots = get_roots(a,b,c)
        # Вывод корней
        len_roots = len(roots)
        if len_roots == 0:
            print('Нет корней')
        elif len_roots == 1:
            print('Один корень: {}'.format(roots[0]))
        elif len_roots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif len_roots == 3:
            print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))    
        elif len_roots == 4:
            print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
        
    
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4

os.system("pause")
