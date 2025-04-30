import json
import sys


def go_through_dict(tests_data: list, values_data: list):
    """Проходит по словарю и заполнет поле 'value'
    значениями из предоставленного файла. Использует рекурсию для
    прохождения по вложеным спискам ключа 'values'. Возвращает заполненный
    словарь из файла со структурой тестов"""
    for test in tests_data:
        for value_data in values_data:
            if test["id"] == value_data["id"]:
                test["value"] = value_data["value"]
                break
        if "values" in test:
            go_through_dict(test["values"], values_data)
    return {"tests": tests_data}


def main(args):
    if len(args) < 4:
        print("Недостаточно аргументов")

    try:
        with open(args[1], "r") as file:
            tests_data = json.load(file)["tests"]
        with open(args[2], "r") as file:
            values_data = json.load(file)["values"]
        with open(args[3], "w") as file:
            json.dump(go_through_dict(tests_data, values_data), file, indent=4)
    except FileNotFoundError:
        print("Ошибка названия пути до файла")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)
