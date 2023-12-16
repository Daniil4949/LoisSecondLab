from interval import Interval


class CompositionEquation:
    def __init__(self, expression, result):
        # Конструктор класса, инициализирующий свойства expression и result.
        self.expression = expression  # Выражение, связанное с уравнением.
        self.result = result  # Результат, соответствующий выражению.

    def get_solutions_list(self):
        # Получаем список переменных, которые могут быть зафиксированы
        possible_fixed_vars = [var_name for var_name in self.expression if self.expression[var_name] >= self.result]

        # Если нет переменных для фиксации, возвращаем пустой список решений
        if not possible_fixed_vars:
            return []

        # Инициализируем список решений
        solutions_list = []

        # Обходим каждую зафиксированную переменную
        for fixed_var in possible_fixed_vars:
            solution = {}

            # Создаем решение для каждой переменной в выражении
            for var_name in self.expression:
                if var_name != fixed_var:
                    # Если переменная не зафиксирована, создаем интервал на основе выражения и результата
                    solution[var_name] = Interval(
                        max(self.expression[var_name], self.result),
                        1.0
                    )
                else:
                    # Если переменная зафиксирована, создаем интервал от 0 до 1
                    solution[var_name] = Interval(0.0, 1.0)

            # Добавляем текущее решение в список решений
            solutions_list.append(solution)

        # Возвращаем список решений
        return solutions_list
