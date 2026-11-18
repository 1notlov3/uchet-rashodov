import csv
import os
from datetime import date

FILE_NAME = "rashody.csv"
CATEGORIES = ["Еда", "Транспорт", "Учёба", "Связь", "Развлечения", "Другое"]


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, encoding="utf-8") as f:
        return list(csv.reader(f, delimiter=";"))


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";").writerows(expenses)


def add_expense(expenses):
    day = input("Дата (ДД.ММ.ГГГГ, Enter - сегодня): ")
    if day == "":
        day = date.today().strftime("%d.%m.%Y")

    for number, name in enumerate(CATEGORIES, 1):
        print(number, name)
    choice = input("Номер категории: ")
    if not choice.isdigit() or not 1 <= int(choice) <= len(CATEGORIES):
        print("Нет такой категории")
        return
    category = CATEGORIES[int(choice) - 1]

    try:
        amount = float(input("Сумма, руб.: ").replace(",", "."))
    except ValueError:
        print("Сумма должна быть числом")
        return

    comment = input("Комментарий: ")
    expenses.append([day, category, str(amount), comment])
    save_expenses(expenses)
    print("Расход сохранён")


def show_expenses(expenses):
    if not expenses:
        print("Расходов пока нет")
        return
    for day, category, amount, comment in expenses:
        print(day, category, amount, "руб.", comment)


def totals(expenses, by_month=False):
    result = {}
    for day, category, amount, comment in expenses:
        # для месяца берём из даты "ДД.ММ.ГГГГ" только "ММ.ГГГГ"
        key = day[3:] if by_month else category
        result[key] = result.get(key, 0) + float(amount)
    return result


def show_totals(result):
    for key, amount in result.items():
        print(key, "-", round(amount, 2), "руб.")
    print("Всего:", round(sum(result.values()), 2), "руб.")


def main():
    expenses = load_expenses()
    while True:
        print()
        print("1 - Добавить расход")
        print("2 - Показать все расходы")
        print("3 - Итоги по категориям")
        print("4 - Итоги по месяцам")
        print("0 - Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_totals(totals(expenses))
        elif choice == "4":
            show_totals(totals(expenses, by_month=True))
        elif choice == "0":
            break
        else:
            print("Нет такого пункта")


if __name__ == "__main__":
    main()
