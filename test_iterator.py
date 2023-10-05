from unittest import TestCase

from iterator import Calendar


class TestCalendar(TestCase):

    def test_iterator_returns_correct_date(self):
        """Календарь выдает корректные значения."""

        test_data = [
            (2023, 60, '1 марта'),
            (2020, 60, '29 февраля'),
            (2022, 1, '1 января'),
            (2019, 365, '31 декабря')
        ]
        for year, count, output in test_data:
            calendar = Calendar(year)
            for _ in range(count):
                date = next(calendar)
            with self.subTest(output=output):
                self.assertEqual(date, output)

    def test_iterator_raises_error_when_exceedes_year(self):
        """На следующем итерированиии после достижения конца года
        вызывается ошибка StopIteration."""

        with self.assertRaises(StopIteration):
            calendar = Calendar(2022)
            for _ in range(366):
                next(calendar)
