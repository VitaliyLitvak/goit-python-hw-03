from datetime import datetime, timedelta, date
from rich import print


users = [{'name': 'Христина Зінчук', 'birthday': '2023-06-19'},
         {'name': 'Валентин Копитко', 'birthday': '1989-06-19'},
         {'name': 'Нестор Авраменко', 'birthday': '1954-06-20'},
         {'name': 'Мирон Філіпенко', 'birthday': '1936-06-21'},
         {'name': 'Мартин Засенко', 'birthday': '1923-06-13'},
         {'name': 'Вікторія Каденюк', 'birthday': '1985-06-16'},
         {'name': 'Веніямин Ґалаґан', 'birthday': '1981-06-19'},
         {'name': 'Святослав Єфименко', 'birthday': '1965-06-23'},
         {'name': 'Ірина Дерегус', 'birthday': '1946-06-25'},
         {'name': 'Лариса Лупій', 'birthday': '2020-06-24'}]
DAYS = {'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
        }
TODAY = date.today()
CURRENT_YEAR = date.today().year
    
def birth_reminder(users):
    week_start = TODAY - timedelta(days=TODAY.weekday()-7)
    week_end = week_start + timedelta(days=6)
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], '%Y-%m-%d').date()
        age = CURRENT_YEAR - user_birthday.year
        user_birthday = user_birthday.replace(year=CURRENT_YEAR)
        if week_start <= user_birthday <= week_end:
            if user_birthday.weekday() < 5:
                DAYS[user_birthday.strftime('%A')].append([user['name'], age])
            else:
                DAYS['Monday'].append([user['name'], age])
    return DAYS
    
print(birth_reminder(users))