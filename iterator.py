import datetime as dt


class Calendar:
    """Класс-итератор для вывода дней заданного года.
    При создании экземляра класса необходимо в параметрах указать год.
    Для вывода следующего дня заданного года используйте функцию next()."""

    def __init__(self, year: int):
        self._year = year
        self._month_out = (
            '',
            'января',
            'февраля',
            'марта',
            'апреля',
            'мая',
            'июня',
            'июля',
            'августа',
            'сентября',
            'октября',
            'ноября',
            'декабря',
        )
        self._next_date = dt.date(year, 1, 1)
        self.date = ''

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_date.year > self._year:
            raise StopIteration
        self.date = (f'{self._next_date.day} '
                     f'{self._month_out[self._next_date.month]}')
        self._next_date += dt.timedelta(1)
        return self.date
