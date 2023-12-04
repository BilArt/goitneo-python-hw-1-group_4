from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_by_weekday = defaultdict(list)
    
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Оцінка Дати на Цей Рік
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # Визначення Дня Тижня
        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"

            birthdays_by_weekday[weekday].append(name)

    for weekday, names in birthdays_by_weekday.items():
        print(f"{weekday}: {', '.join(names)}")

users = [
    {"name": "Vasia Pupkin", "birthday": datetime(1989, 12, 4)},
    {"name": "Gadia Petrovich Hrenova", "birthday": datetime(1989, 12, 4)},
    {"name": "Valia Bas", "birthday": datetime(1988, 10, 10)},
    {"name": "Andrii Prihodko", "birthday": datetime(1999, 9, 6)},
    {"name": "Baba Jaga", "birthday": datetime(1111, 11, 5)},
]

get_birthdays_per_week(users)
