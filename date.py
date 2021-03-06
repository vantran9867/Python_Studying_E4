import datetime


class Date:
    date: int
    month: int
    year: int

    def __init__(self, date: int, month: int, year: int):
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        date_output = datetime.datetime.strptime('{}, {}, {}'.format(self.date, self.month, self.year), '%d, %m, %y')
        return date_output
