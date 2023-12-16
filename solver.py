class Solver:
    def __init__(self, logical_conclusion, rules):
        # Конструктор класса, инициализирующий свойства logical_conclusion, rules, matrix и answers.
        self.logical_conclusion = logical_conclusion
        """
        logical_conclusion = [['y1', 0.7], ['y2', 0.3], ['y3', 0.2]]
        """

        self.rules = rules
        """
        rules = [
            [[['x1','y1'], 0.7], [['x1','y2'], 0.1], [['x1','y3'], 0.2]],
            [[['x2','y1'], 0.7], [['x2','y2'], 0.3], [['x2','y3'], 0.1]]
        ]
        """

        self.matrix = []  # Пустая матрица, которая может быть заполнена в процессе вычислений
        self.answers = []  # Пустой список для хранения результатов

    def form_matrix(self):
        """
        Формирует матрицу на основе правил.
        """
        # Проходим по элементам первого правила
        for el in self.rules[0]:
            newRow = [el]  # Создаем новую строку с текущим элементом
            variable = el[0][1]  # Получаем переменную из текущего элемента

            # Проходим по остальным правилам, начиная с индекса 1
            for i in range(1, len(self.rules)):
                # Находим элемент с той же переменной в текущем правиле
                found_element = next((e for e in self.rules[i] if e[0][1] == variable), None)
                newRow.append(found_element)  # Добавляем найденный элемент в строку

            self.matrix.append(newRow)  # Добавляем сформированную строку в матрицу

    def form_answers(self):
        """
        Формирует список ответов на основе матрицы.
        """
        # Проходим по строкам матрицы
        for row in self.matrix:
            # Проходим по элементам первой ячейки текущей строки
            for el in row[0]:
                # Если элемент является числом, пропускаем его
                if isinstance(el, (int, float)):
                    continue

                variable = el[1]  # Получаем переменную из текущего элемента
                # Находим соответствующий элемент в логическом выводе
                answer = next((el for el in self.logical_conclusion if el[0] == variable), None)
                self.answers.append(answer)  # Добавляем найденный элемент в список ответов

    def solve(self):
        """
        Выполняет решение на основе матрицы.
        """
        # Создаем массив максимальных значений, инициализированный нулями
        maxes = [0] * len(self.matrix[0])

        # Проходим по элементам матрицы
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                # Если значение в текущей ячейке больше соответствующего максимального значения, обновляем максимум
                if self.matrix[i][j][1] > maxes[j]:
                    maxes[j] = self.matrix[i][j][1]

        # В этой точке у вас есть массив maxes с максимальными значениями для каждого столбца матрицы

    @staticmethod
    def print_answer(maxes):
        """
        Выводит ответ на основе массива максимальных значений.
        """
        string = ""

        # Проходим по элементам массива maxes
        for el in maxes:
            # Здесь вы можете формировать строку или выполнять другие действия в зависимости от вашей логики вывода
            # Например, добавить значение el к строке
            string += f"{el} "

        # Выводим сформированную строку
        print(string)

    def transform_data_to_obj(self):
        """
        Преобразует данные в объект.
        """
        expressions = []
        answers = []

        # Проходим по строкам матрицы
        for row in self.matrix:
            expression = {}

            # Формируем объект выражения для каждой строки
            for i in range(len(row)):
                expression[row[i][0][0]] = row[i][1]

            expressions.append(expression)

        # Преобразуем ответы в отдельный список
        for el in self.answers:
            answers.append(el[1])

        # Возвращаем объект с выражениями и ответами
        return {
            "expressions": expressions,
            "answers": answers
        }

    @staticmethod
    def log(intersections):
        """
        Выводит информацию о пересечениях.
        """
        string = "<"
        index = 0

        # Формируем строку с именами переменных в пересечении
        for key in intersections[0]:
            if index != len(intersections[0]) - 1:
                string += f"C({key}),"
            else:
                string += f"C({key})"
            index += 1

        string += "> ∈ "

        counter2 = 0

        # Формируем строку с интервалами для каждого пересечения
        for intersection in intersections:
            string += "("
            counter = 0

            for key in intersection:
                if counter != len(intersection) - 1:
                    string += f"[{intersection[key].left},{intersection[key].right}]x"
                else:
                    string += f"[{intersection[key].left},{intersection[key].right}]"

                counter += 1

            string += ")"

            if counter2 != len(intersections) - 1:
                string += "U"

            counter2 += 1

        print(string)

    @staticmethod
    def find_intersection_of_intervals(intervals):
        """
        Находит пересечение интервалов.
        """
        keys = list(intervals[0][0].keys())
        count_of_intersections = 0
        index = 0
        intersections = []

        # Находим индекс строки с максимальным количеством интервалов
        for i in range(len(intervals)):
            if len(intervals[i]) > count_of_intersections:
                count_of_intersections = len(intervals[i])
                index = i

        # Находим пересечение для каждого интервала
        for i in range(count_of_intersections):
            max_interval = dict(intervals[index][i])

            # Проходим по остальным строкам
            for j in range(len(intervals)):
                if index != j:
                    for interval in intervals[j]:
                        for key in keys:
                            if interval[key].left > intervals[index][i][key].left:
                                max_interval[key].left = interval[key].left
                            if interval[key].right < intervals[index][i][key].right:
                                max_interval[key].right = interval[key].right

            intersections.append(max_interval)

        return intersections

