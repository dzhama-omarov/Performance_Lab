import sys


def walking_func(n: int, m: int) -> int:
    '''Выводит путь, по которому, двигаясь интервалом длины
m по заданному массиву, концом будет являться первый элемент.
Началом одного интервала является конец предыдущего.
Путь - массив из начальных элементов полученных интервалов.

    <b>Пример</b>

n = 5, m = 4

Круговой массив: 12345

При длине обхода 4 получаем интервалы: 1234, 4512, 2345, 5123, 3451

Полученный путь: 14253'''

    if n < 1 or m < 1:
        raise ValueError("Значение аргументов не может быть ниже 1")

    num = 1
    path = "1"
    iteration = 1

    while (num == 1 and (iteration % m) == 0) is False:
        if (iteration % m) == 0:
            path += (str(num))
        else:
            num = (num + 1) // (n + 1) + (num + 1) % (n + 1)
        iteration += 1
    return int(path)


def main(args):
    if len(args) != 3:
        print("Пожалуйста, введите только 2 числа")
        sys.exit(1)
    else:
        try:
            n = int(args[1])
            m = int(args[2])

            print(walking_func(n, m))
        except ValueError:
            print("Ошибка: аргументы должны быть числами")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
