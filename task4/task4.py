import sys


def count_n_of_steps(nums_list: list) -> int:
    """Считает минимальное количество ходов, требуемых для
    приведения всех элементов к одному числу. """
    average = int(round(sum(nums_list) / len(nums_list), 0))
    n_of_steps = 0
    for number in nums_list:
        n_of_steps += abs(number - average)
    return n_of_steps


def main(args) -> int:
    if len(args) < 2:
        return "Недостаточное количество аргументов"
    try:
        with open(args[1], "r") as file:
            try:
                data = list(map(int, file.readlines()))
            except ValueError:
                return "Ошибка данных. Проверьте числа"
        return count_n_of_steps(data)
    except FileNotFoundError:
        return "Ошибка названия пути файла"


if __name__ == "__main__":
    print(main(sys.argv))
