import os
import unittest

import rashody

EXPENSES = [
    ["01.11.2026", "Еда", "250.0", "обед"],
    ["05.11.2026", "Транспорт", "60.0", "метро"],
    ["18.11.2026", "Еда", "300.5", "продукты"],
    ["02.12.2026", "Связь", "500.0", "телефон"],
]


class TestRashody(unittest.TestCase):
    def test_by_category(self):
        """Итоги по категориям"""
        result = rashody.totals(EXPENSES)
        self.assertEqual(result, {"Еда": 550.5, "Транспорт": 60.0, "Связь": 500.0})

    def test_by_month(self):
        """Итоги по месяцам"""
        result = rashody.totals(EXPENSES, by_month=True)
        self.assertEqual(result, {"11.2026": 610.5, "12.2026": 500.0})

    def test_empty(self):
        """Пустой список расходов"""
        self.assertEqual(rashody.totals([]), {})

    def test_save_and_load(self):
        """Сохранение в файл и чтение из файла"""
        rashody.FILE_NAME = "test_rashody.csv"
        rashody.save_expenses(EXPENSES)
        self.assertEqual(rashody.load_expenses(), EXPENSES)
        os.remove("test_rashody.csv")


if __name__ == "__main__":
    unittest.main()
