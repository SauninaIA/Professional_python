import os
from datetime import datetime


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='cp1251') as file:
                file.write(f'Время вызова функции: {datetime.now()} \n')
                file.write(f'Имя функции: {old_function.__name__} \n')
                file.write('Аргументы функции: \n')
                file.write(f'{args} \n')
                file.write(f'{kwargs} \n')
                result = old_function(*args, **kwargs)
                file.write(f'Результат: {result} \n')
            return result

        return new_function

    return __logger


@logger(path='main.log')
def check_doc(documents, num):
    for document in documents:
        if document['number'] == num:
            res = 'Есть такой документ'
            return res
    else:
        res = 'Нет такого документа'
        return res

# def test_1():
#
#     path = 'main.log'
#     if os.path.exists(path):
#         os.remove(path)
#
#     @logger
#     def summator(a, b=0):
#         return a + b
#
#     result = summator(2, 2)
#     assert isinstance(result, int), 'Должно вернуться целое число'
#     assert result == 4, '2 + 2 = 4'
#
#     assert os.path.exists(path), 'файл main.log должен существовать'
#
#     summator(4.3, b=2.2)
#     summator(a=0, b=0)
#
#     with open(path) as log_file:
#         log_file_content = log_file.read()
#
#     assert 'summator' in log_file_content, 'должно записаться имя функции'
#     for item in (4.3, 2.2, 6.5):
#         assert str(item) in log_file_content, f'{item} должен быть записан в файл'

# def test_2():
#     paths = ('log_1.log', 'log_2.log', 'log_3.log')
#
#     for path in paths:
#         if os.path.exists(path):
#             os.remove(path)
#
#         @logger(path)
#         def summator(a, b=0):
#             return a + b
#
#         @logger(path)
#         def div(a, b):
#             return a / b
#
#         result = summator(2, 2)
#         assert isinstance(result, int), 'Должно вернуться целое число'
#         assert result == 4, '2 + 2 = 4'
#         div(4, 2)
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'файл {path} должен существовать'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, 'должно записаться имя функции'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    check_doc(documents, "11-2")
    # test_1()
    # test_2()
