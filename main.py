from composition_equation import CompositionEquation
from solver import Solver


def main(solver_obj):
    """
    Основная функция для выполнения ряда шагов.
    """
    # Формируем матрицу и ответы
    solver_obj.form_matrix()
    solver_obj.form_answers()
    solver_obj.solve()

    # Преобразуем данные в объект
    suitable_data = solver_obj.transform_data_to_obj()

    intervals = []

    # Создаем интервалы для каждого выражения
    for i in range(len(suitable_data["expressions"])):
        interval = CompositionEquation(
            suitable_data["expressions"][i],
            suitable_data["answers"][i]
        )
        intervals.append(
            interval.get_solutions_list()
        )

    # Находим пересечения интервалов
    intersections = solver_obj.find_intersection_of_intervals(intervals)

    # Выводим результат
    solver_obj.log(intersections)


if __name__ == "__main__":
    solver = Solver([['y1', 0.7], ['y2', 0.3], ['y3', 0.2]], [
        [[['x1', 'y1'], 0.7], [['x1', 'y2'], 0.1], [['x1', 'y3'], 0.2]],
        [[['x2', 'y1'], 0.7], [['x2', 'y2'], 0.3], [['x2', 'y3'], 0.1]]
    ])
    main(solver_obj=solver)
