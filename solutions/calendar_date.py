class Date:
    def __init__(self, day: int, month: int, year: int):
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть от 1 до 12")
        if not (1 <= day <= self._days_in_month(month, year)):
            raise ValueError("Несуществующая дата")
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @staticmethod
    def _is_leap(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def _days_in_month(cls, month: int, year: int) -> int:
        if month in (4, 6, 9, 11):
            return 30
        if month == 2:
            return 29 if cls._is_leap(year) else 28
        return 31

    @classmethod
    def _days_before_year(cls, year: int) -> int:
        """Дней от 1.1.1 до 1.1.year."""
        y = year - 1
        return y * 365 + y // 4 - y // 100 + y // 400

    @classmethod
    def _to_ordinal(cls, day: int, month: int, year: int) -> int:
        """Номер дня от 1.1.1 (1.1.1 -> 1)."""
        days = cls._days_before_year(year)
        for m in range(1, month):
            days += cls._days_in_month(m, year)
        return days + day

    @classmethod
    def _from_ordinal(cls, ordinal: int) -> "Date":
        """Обратное преобразование: номер дня -> Date."""

        lo, hi = 1, 1
        while cls._days_before_year(hi + 1) < ordinal:
            hi *= 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if cls._days_before_year(mid) < ordinal:
                lo = mid
            else:
                hi = mid - 1
        year = lo
        rem = ordinal - cls._days_before_year(year)
        month = 1
        while rem > cls._days_in_month(month, year):
            rem -= cls._days_in_month(month, year)
            month += 1
        return cls(rem, month, year)

    def __add__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return self._from_ordinal(self._to_ordinal(self._day, self._month, self._year) + n)

    def __sub__(self, other):
        if isinstance(other, Date):
            return (self._to_ordinal(self._day, self._month, self._year)
                    - self._to_ordinal(other._day, other._month, other._year))
        if isinstance(other, int):
            return self + (-other)
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self._year, self._month, self._day) < (other._year, other._month, other._day)

    def __hash__(self):
        return hash((self._day, self._month, self._year))

    def __repr__(self):
        return f"Date({self._day}, {self._month}, {self._year})"

    def __str__(self):
        return f"{self._day:02d}.{self._month:02d}.{self._year:04d}"