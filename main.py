import random

saved_sets = {}


def main_menu():
    print("\nГЛАВНОЕ МЕНЮ")
    print("-------------------------------------------")
    print("1. Создание множества.")
    print("2. Калькулятор множеств.")
    print("3. Просмотреть существующие множества.")
    print("0. Выход.")
    print("-------------------------------------------")


def creation_menu():
    print("\nВыберите вариант создания:")
    print("1. Генерация случайного множества.")
    print("2. Пользовательское множество.")
    print("3. Создание множества по условиям.")
    print("-------------------------------------------")


def condition_menu():
    print("\nУсловия создания множества (можно комбинировать, например: 13, 245):")
    print("1. Только четные числа.")
    print("2. Только нечетные числа.")
    print("3. Отрицательные числа.")
    print("4. Положительные числа.")
    print("5. Числа, кратные N.")
    print("-------------------------------------------")


def calculator_menu():
    print("\nВыберите следующие действия со множествами:")
    print("1. Объединение.")
    print("2. Пересечение.")
    print("3. Вычитание.")
    print("4. Симметрическая разность.")
    print("5. Дополнение.")
    print("6. Калькулятор выражений.")
    print("0. Выход.")
    print("-------------------------------------------")


def cool_calc_menu():
    print("\n---------------------------------------------")
    print("|         Правила введения операций:        |")
    print("| 1. Скобки: ()            (A+B)            |")
    print("| 2. Дополнение: !          !A              |")
    print("| 3. Пересечение: *         А*В             |")
    print("| 4. Объединение: +         А+В             |")
    print("| 5. Разность: -            А-В             |")
    print("| 6. Симметрическая разность: ^     А^В     |")
    print("---------------------------------------------\n")


# Вспомогательная функция для красивого вывода множеств
def format_set(s):
    if not s:
        return "Ø"
    return str(sorted(list(s)))


def rand_cr():
    num = int(input("Введите количество элементов множества: "))
    rand_set = set()
    while len(rand_set) < num:
        number = random.randint(-30, 30)
        rand_set.add(number)
    return rand_set


def per_cr():
    num = int(input("Введите количество элементов множества: "))
    per_set = set()
    print(f"Введите {num} уникальных элементов:")
    while len(per_set) < num:
        try:
            number = int(input("> "))
            if number in per_set:
                print("Это число уже есть! Введите другое.")
            else:
                per_set.add(number)
        except ValueError:
            print("Ошибка: введите целое число.")
    return per_set


def condition_cr():
    condition_menu()
    choice2 = input("Выберите пункты меню: ").strip()
    num = int(input("Введите количество элементов множества: "))

    a = int(input("Введите верхнее значение диапазона: "))
    b = int(input("Введите нижнее значение диапазона: "))
    if b > a:
        a, b = b, a  # Защита от перепутанных границ

    n = 1
    if '5' in choice2:
        n = int(input("Введите число для проверки кратности: "))

    # Собираем все числа, которые подходят под выбранные условия
    valid_nums = []
    for x in range(b, a + 1):
        valid = True
        if '1' in choice2 and x % 2 != 0: valid = False
        if '2' in choice2 and x % 2 == 0: valid = False
        if '3' in choice2 and x >= 0: valid = False
        if '4' in choice2 and x < 0: valid = False
        if '5' in choice2 and x % n != 0: valid = False

        if valid:
            valid_nums.append(x)

    # Проверяем, хватает ли подходящих чисел
    if num > len(valid_nums):
        print(f"Ошибка: в данном диапазоне подходящих значений всего {len(valid_nums)}.")
        return set()

    # Берем случайные уникальные числа из отфильтрованного списка
    return set(random.sample(valid_nums, num))


def get_set_by_name(prompt):
    if not saved_sets:
        print("Ошибка: Нет сохраненных множеств. Сначала создайте их!")
        return None

    while True:
        available_names = ", ".join(saved_sets.keys())
        print(f"Доступные множества: {available_names}")
        name = input(prompt).strip()

        if name in saved_sets:
            return set(saved_sets[name])
        print(f"Ошибка: Множества '{name}' не существует.\n")


def saving(operation_result):
    if operation_result is None or not isinstance(operation_result, set):
        return

    save_choice = input("Хотите ли вы сохранить результат? (да/нет): ").strip().lower()
    if save_choice == "да":
        name = input("Введите имя множества (например, A или B): ").strip()

        if name in saved_sets:
            print(f"Предупреждение: Множество '{name}' уже существует.")
            answer = input("Хотите перезаписать его? (да/нет): ").strip().lower()
            if answer != "да":
                print("Отмена сохранения.")
                return

        saved_sets[name] = operation_result
        print(f"Множество '{name}' сохранено!\n")


def creation():
    while True:
        creation_menu()
        cr_ch = input("Выберите способ задания множества: ").strip()

        my_set = set()
        match cr_ch:
            case "1":
                my_set = rand_cr()
            case "2":
                my_set = per_cr()
            case "3":
                my_set = condition_cr()
            case _:
                print("Неверный выбор.")
                continue

        print("Получившееся множество:", format_set(my_set))
        return my_set


def calculator():
    if not saved_sets:
        print("\nУ вас пока нет ни одного сохраненного множества!")
        return

    while True:
        calculator_menu()
        calc_choice = input("Выберите действие со множествами: ").strip()

        if calc_choice == "0":
            break

        if calc_choice in ["1", "2", "3", "4"]:
            set1 = get_set_by_name("Введите имя первого множества: ")
            if set1 is None: return
            set2 = get_set_by_name("Введите имя второго множества: ")

            result = set()
            if calc_choice == "1":
                result = set1.union(set2)
            elif calc_choice == "2":
                result = set1.intersection(set2)
            elif calc_choice == "3":
                result = set1.difference(set2)
            elif calc_choice == "4":
                result = set1.symmetric_difference(set2)

            print(f"Результат: {format_set(result)}")
            saving(result)

        elif calc_choice == "5":
            set_name = get_set_by_name("Над каким из множеств выполнить Дополнение? ")
            if set_name is not None:
                result = complement(set_name)
                print(f"Результат: {format_set(result)}")
                saving(result)

        elif calc_choice == "6":
            cool_calc_menu()
            expression = input("Напишите выражение: ").strip()
            try:
                result = calculating(expression)
                print(f"Результат: {format_set(result)}")
                saving(result)
            except Exception as e:
                print(f"Ошибка вычисления выражения: {e}")


def complement(a):
    universe = set(range(-30, 31))  # Универсум от -30 до 30 включительно
    return universe.difference(a)


PRECEDENCE = {'!': 5, '*': 4, '+': 3, '-': 2, '^': 1}


def apply_operator(op, stack):
    if op == '!':
        a = stack.pop()
        stack.append(complement(a))
    elif op in ('+', '*', '-', '^'):
        b = stack.pop()
        a = stack.pop()
        if op == '+':
            stack.append(a.union(b))
        elif op == '*':
            stack.append(a.intersection(b))
        elif op == '-':
            stack.append(a.difference(b))
        elif op == '^':
            stack.append(a.symmetric_difference(b))


def calculating(expression):
    expression = expression.replace(" ", "")
    values = []
    ops = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isalpha():
            if char in saved_sets:
                values.append(set(saved_sets[char]))
            else:
                raise ValueError(f"Переменная '{char}' не найдена!")
        elif char == '(':
            ops.append(char)
        elif char == ')':
            while ops and ops[-1] != '(':
                apply_operator(ops.pop(), values)
            ops.pop()  # Удаляем '('
        elif char in PRECEDENCE:
            while (ops and ops[-1] != '(' and
                   PRECEDENCE.get(ops[-1], 0) >= PRECEDENCE.get(char, 0)):
                apply_operator(ops.pop(), values)
            ops.append(char)
        i += 1

    while ops:
        apply_operator(ops.pop(), values)

    return values[0]


def main():
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ").strip()

        match choice:
            case "1":
                saving(creation())
            case "2":
                calculator()
            case "3":
                if not saved_sets:
                    print("\nМножеств пока нет.")
                else:
                    print("\nСохраненные множества:")
                    for k, v in saved_sets.items():
                        print(f"{k} = {format_set(v)}")
            case "0":
                print("Завершение программы.")
                break


if __name__ == "__main__":
    main()