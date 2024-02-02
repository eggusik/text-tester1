import unittest
from io import StringIO
import sys

def run_tests(test_file_path, user_code_file_path):
    # Создаем временный поток вывода для захвата результатов тестирования
    output_stream = StringIO()
    sys.stdout = output_stream

    # Читаем содержимое файла с пользовательским кодом
    with open(user_code_file_path, 'r') as user_code_file:
        user_code = user_code_file.read()

    # Выполняем пользовательский код в текущем пространстве имен
    exec(user_code, globals())

    # Читаем содержимое файла с тестами
    with open(test_file_path, 'r') as test_file:
        test_code = test_file.read()

    # Добавляем тесты из файла в текущее пространство имен
    exec(test_code, globals())

    # Запускаем тесты
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(stream=output_stream, verbosity=2).run(suite)

    # Восстанавливаем стандартный поток вывода
    sys.stdout = sys.__stdout__

    # Получаем результаты тестирования из временного потока вывода
    test_results = output_stream.getvalue()

    # Возвращаем результаты тестирования
    return test_results

# Пример использования функции
results = run_tests("test.txt", "user.txt")
print(results)
