from operator import itemgetter
 
class Book:
    """Книги"""
    def __init__(self, id, name, auth, lb_id):
        self.id = id
        self.name = name
        self.auth = auth
        self.lb_id = lb_id
 
class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class BooksL:
    """
    'Книги библиотеки' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lb_id, book_id):
        self.lb_id = lb_id
        self.book_id = book_id
 
def task_1(Books, Libraries):
    # Соединение данных один-ко-многим 
    one_to_many = [
        (b.name, b.auth, l.name) 
        for l in Libraries 
        for b in Books 
        if l.id == b.lb_id
    ]
    return sorted(one_to_many, key=itemgetter(0))

def task_2(Books, Libraries):
    one_to_many = [
        (b.name, b.auth, l.name) 
        for l in Libraries 
        for b in Books 
        if b.lb_id == l.id
    ]
    res = list()
    # Перебираем все библиотеки
    for lb in Libraries:
        # Список книг в библиотеке
        lb_books = list(filter(lambda i: i[2] == lb.name, one_to_many))
        # Если библиотека не пуста
        if len(lb_books) > 0:
            res.append((lb.name, len(lb_books)))
    return sorted(res, key=itemgetter(1), reverse=True)

def task_3(Books, Libraries, Books_Librarys):
    # Соединение данных многие-ко-многим
    many_to_many = [
        (b.name, b.auth, l.name)
        for l in Libraries 
        for b in Books 
        for relation in Books_Librarys
        if b.id == relation.lb_id and l.id == relation.lb_id
    ]
    res = dict()
    for b in Books:
        if b.name.endswith("ов"):
            # Ищем библиотеки, в которых есть эта книга
            b_libraries = list(filter(lambda x: x[0] == b.name, many_to_many))
            # Получаем их названия
            b_libraries_names = [x[2] for x in b_libraries]
            res[b.name] = b_libraries_names
    return res

def main():
    # Библиотеки
    Libraries = [
        Library(1, 'Ленинка'),
        Library(2, 'Питерская библиотека'),
        Library(3, 'Библиотека 11'),

        Library(11, 'Библиотека им. Макса'),
        Library(22, 'Библиотека Кубани'),
        Library(33, 'ВНДХ'),
    ]
 
    # Книги
    Books = [
        Book(1, 'Сказки', 'Артамонов', 1),
        Book(2, 'Тихое утров', 'Петров', 2),
        Book(3, 'Богатые люди', 'Иваненко', 3),
        Book(4, 'Мир и война', 'Иванов', 3),
        Book(5, 'Громкий Дон', 'Иванин', 3),
    ]
    
    # Книги и библиотеки
    Books_Librarys = [
        BooksL(1,1),
        BooksL(2,2),
        BooksL(3,3),
        BooksL(3,4),
        BooksL(3,5),
    
        BooksL(11,1),
        BooksL(22,2),
        BooksL(33,3),
        BooksL(33,4),
        BooksL(33,5),
    ]

    print("Задание Б1")
    res_1 = task_1(Books, Libraries)
    [print(el) for el in res_1]

    print("\nЗадание Б2")
    res_2 = task_2(Books, Libraries)
    [print(el) for el in res_2]

    print("\nЗадание Б3")
    res_3 = task_3(Books, Libraries, Books_Librarys)
    [print(k, v) for k, v in res_3.items()]

if __name__ == "__main__":
    main()