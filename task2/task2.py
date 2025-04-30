import sys


def where_is_dot(cent_coord: list, radius: int, dot_coord: list) -> int:
    """Принимает координаты центра круга и его радиус,
    а также координаты точки. Возвращает 1 - если точка внутри круга,
    2 - если вне круга, и 0 - если точка лежит на окружности"""
    try:
        dot_cent_distance_squared = (
            (cent_coord[0] - dot_coord[0]) ** 2
            + (cent_coord[1] - dot_coord[1]) ** 2
        )
        if dot_cent_distance_squared < (radius ** 2):
            return 1
        elif dot_cent_distance_squared == (radius ** 2):
            return 0
        else:
            return 2
    except IndexError:
        return (
            "Index error. Исходные данные точек не соответсвуют формату"
            " 'число число'"
        )


def main(args):
    if len(args) < 3:
        print("Недостаточно аргументов")
        sys.exit(1)

    try:
        circle_filepath = args[1]
        dots_filepath = args[2]
        try:
            with open(circle_filepath, "r") as circ_file:
                lines = circ_file.readlines()
                circ_coord = list(map(int, lines[0].split()))
                circ_radius = int(lines[1])
        except ValueError:
            return (
                "Value error. Исходные данные круга не соответсвуют формату:"
                "\n'число число\nчисло'"
            )
    except FileNotFoundError:
        print("Ошибка. Файл с данными круга не найден")
        sys.exit(1)

    try:
        with open(dots_filepath, "r") as circ_file:
            lines = circ_file.readlines()
            for line in lines:
                try:
                    if line == ["\n"]:
                        continue
                    print(where_is_dot(
                        circ_coord,
                        circ_radius,
                        list(map(int, line.split()))
                    ))
                except ValueError:
                    print(
                        "Value error."
                        "Исходные данные точек не соответсвуют формату"
                        " 'число число'"
                    )
    except FileNotFoundError:
        print("Ошибка. Файл с данными точек не найден")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
