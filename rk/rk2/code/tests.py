import unittest
from main import *

class Test(unittest.TestCase):
    def setUp(self):
        self.Libraries = [
        Library(1, "Ленинка"),
        Library(2, "Питерская библиотека"),
        Library(3, "Библиотека 11"),

        Library(11, "Библиотека им. Макса"),
        Library(22, "Библиотека Кубани"),
        Library(33, "ВНДХ"),
        ]
        self.Books = [
            Book(1, "Сказки", "Артамонов", 1),
            Book(2, "Тихое утров", "Петров", 2),
            Book(3, "Богатые люди", "Иваненко", 3),
            Book(4, "Мир и война", "Иванов", 3),
            Book(5, "Громкий Дон", "Иванин", 3),
        ]
        self.Books_Librarys = [
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
    def test_task_1(self):

        key_fot_test = [
            ("Богатые люди", "Иваненко", "Библиотека 11"),
            ("Громкий Дон", "Иванин", "Библиотека 11"),
            ("Мир и война", "Иванов", "Библиотека 11"),
            ("Сказки", "Артамонов", "Ленинка"),
            ("Тихое утров", "Петров", "Питерская библиотека"),
        ]

        self.assertEqual(task_1(self.Books, self.Libraries), key_fot_test)

    def test_task_2(self):

        key_fot_test = [
            ("Библиотека 11", 3),
            ("Ленинка", 1),
            ("Питерская библиотека", 1),
        ]

        self.assertEqual(task_2(self.Books, self.Libraries), key_fot_test)

    def test_task_3(self):

        key_fot_test = {
            "Тихое утров": ["Питерская библиотека"],
        }

        self.assertEqual(task_3(self.Books, self.Libraries, self.Books_Librarys), key_fot_test)

if __name__ == "__main__":
    unittest.main()