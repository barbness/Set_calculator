import sys
import random
from unittest import case

saved_sets = {}

def main_menu():
    print("ГЛАВНОЕ МЕНЮ")
    print("-------------------------------------------")
    print("\n1. Создание множества.")
    print("2. Калькулятор множеств.")
    print("3. Просмотреть существующие множества.")
    print("\n-------------------------------------------")

def creation_menu():
    print("\nВыберите вариант создания:")
    print("1. Генерация случайного множества.")
    print("2. Пользовательское множество.")
    print("3. Создание множества по условиям.")

def condition_menu():
    print("\nВыберите следующие условия создания множества:")
    print("1. Только четные числа.")
    print("2. Только нечетные числа.")
    print("3. Отрицательные числа.")
    print("4. Положительные числа.")
    print("5. Числа, кратные N.")
    print("6. Задание диапазона.")

def calculator_menu():
    print("\nВыберите следующие действия со множествами:")
    print("1. Объединение.")
    print("2. Пересечение.")
    print("3. Вычитание.")
    print("4. Арифметическое вычитание.")
    print("5. Дополнение.")
    print("6. Калькулятор выражений.")

def rand_cr():
    num = int(input("Введите количество элементов множества:"))
    rand_set = set()
    while len(rand_set) < num:
        number = random.randint(-30, 30)
        rand_set.add(number)
    return rand_set

def per_cr():
    num = int(input("Введите количество элементов множества:"))
    per_set = set()
    print("Введите элементы множества")
    for i in range (num):
        number = int(input())
        per_set.add(number)
    while len(per_set) != num:
        print("О-оу, вы ввели не уникальные числа! Введите еще " + str((num- len(per_set))) + " элементов!")
        for j in range(num - len(per_set)):
            number2 = int(input())
            per_set.add(number2)
    return per_set

#def condition_cr():
#    while True:
#        choice2 = input("Выберите пункт меню: ").strip()
#        num = int(input("Введите количество элементов множества: "))
#        cond_set = set()
#        match choice2:
#            case "1":
#                while len(cond_set)<num:
#                    even_num = random.randrange(-30, 30, 2)
#                    cond_set.add(even_num)
#                return cond_set
#            case "2":
#                while len(cond_set)<num:
#                    odd_num = random.randrange(-29, 29, 2)
#                    cond_set.add(odd_num)
#            case "3":

def get_set_by_name(prompt):
    while True:
        available_names = ", ".join(saved_sets.keys())
        print(f"Доступные множества: {available_names}")

        name = input(prompt).strip()

        if name in saved_sets:
            return saved_sets[name]
        else:
            print(f"Ошибка: Множества с именем '{name}' не существует. Попробуйте еще раз.\n")

def saving(operation):
    name = input("Введите имя множества (например, A или B): ").strip()

    if name in saved_sets:
        print(f"Предупреждение: Множество '{name}' уже существует.")
        answer = input("Хотите перезаписать его? (да/нет): ").strip().lower()

        if answer != "да":
            print("Операция отменена. Возврат в главное меню.")
            return

    saved_sets[name] = operation
    print(f"Множество '{name}' сохранено!\n")

def main():

    while True:
        main_menu()

        # Получаем ввод от пользователя
        choice = input("Выберите пункт меню: ").strip()

        # Обрабатываем выбор с помощью конструкции match-case
        match choice:
            case "1":
                saving(creation())

            case "2":
                calculator()


def creation():
    while True:
        creation_menu()

        cr_ch = input("Выберите способ задания множества: ").strip()

        match cr_ch:
            case "1":
                my_set = rand_cr()
                print("Получившееся множество: ", my_set)
                if len(my_set) == 0:
                    return str("Ø")
                return my_set

            case "2":
                my_set = per_cr()
                print("Получившееся множество: ", my_set)
                if len(my_set) == 0:
                    return str("Ø")
                return my_set

def calculator():
    while True:
        calculator_menu()

        set1 = get_set_by_name("Введите имя первого множества: ")
        set2 = get_set_by_name("Введите имя второго множества: ")

        calc_choice = input("Выберите действие со множествами: ").strip()

        match calc_choice:
            case "1":
                print(f"Полученное множество: {union(set1, set2)}.")
                save_choice = input("Хотите ли вы сохранить его? ").strip().lower()
                if save_choice == "да":
                    saving(union(set1, set2))
            case "2":
                print(f"Полученное множество: {intersection(set1, set2)}")
                save_choice = input("Хотите ли вы сохранить его? ").strip().lower()
                if save_choice == "да":
                    saving(intersection(set1, set2))
            case "3":
                print(f"Полученное множество: {difference(set1, set2)}")
                save_choice = input("Хотите ли вы сохранить его? ").strip().lower()
                if save_choice == "да":
                    saving(difference(set1, set2))
            case "4":
                print(f"Полученное множество: {sym_difference(set1, set2)}")
                save_choice = input("Хотите ли вы сохранить его? ").strip().lower()
                if save_choice == "да":
                    saving(sym_difference(set1, set2))
            case "5":
                set_name = input("Над каким из множеств вы хотите выполнить операцию Дополнения?").strip()
                print(f"Полученное множество: {complement(saved_sets[set_name])}")
                save_choice = input("Хотите ли вы сохранить его? ").strip().lower()
                if save_choice == "да":
                    saving(complement(saved_sets[set_name]))



def union(a, b):
    result = a.copy()
    for item in b:
        result.add(item)
    if len(result) == 0:
        return str("Ø")
    return result

def intersection(a, b):
    result = set()
    for i in a:
        if i in b:
            result.add(i)
    if len(result) == 0:
        return str("Ø")
    return result

def difference(a, b):
    result = set()
    for i in a:
        if i not in b:
            result.add(i)
    if len(result) == 0:
        return str("Ø")
    return result

def sym_difference(a, b):
    result = set()
    for i in a:
        if i not in b:
            result.add(i)
    for j in b:
        if j not in a:
            result.add(j)
    if len(result) == 0:
        return str("Ø")
    return result

def complement(a):
    universe = set(range(-30, 30))
    result = set()

    for i in universe:
        if i not in a:
            result.add(i)
    if len(result) == 0:
        return str("Ø")
    return result


if __name__ == "__main__":
    main()