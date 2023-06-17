from datetime import datetime, timedelta, date
from rich import print


users = [{'name': 'Христина Зінчук', 'birthday': '2023-06-17'},
         {'name': 'Валентин Копитко', 'birthday': '1989-06-18'},
         {'name': 'Нестор Авраменко', 'birthday': '1954-06-20'},
         {'name': 'Мирон Філіпенко', 'birthday': '1936-06-21'},
         {'name': 'Мартин Засенко', 'birthday': '1923-06-19'},
         {'name': 'Вікторія Каденюк', 'birthday': '1985-06-16'},
         {'name': 'Веніямин Ґалаґан', 'birthday': '1981-06-19'},
         {'name': 'Святослав Єфименко', 'birthday': '1965-06-26'},
         {'name': 'Ірина Дерегус', 'birthday': '1946-06-25'},
         {'name': 'Лариса Лупій', 'birthday': '2020-06-24'}]

    
def birth_reminder(users):
    current_year = date.today().year
    today = date.today()
    week_start = today - timedelta(days=today.weekday()-5)
    week_end = week_start + timedelta(days=6)
    delete_days = []
    print(week_start, week_end)
    DAYS = {}
    # Пошук потрібних юзерів
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], '%Y-%m-%d').date()
        age = current_year - user_birthday.year
        user_birthday = user_birthday.replace(year=current_year)
        if week_start <= user_birthday <= week_end:
            if user_birthday.weekday() < 5:
                DAYS.setdefault(user_birthday.strftime('%A'), []).append([user['name'], age])
            else:
                DAYS.setdefault('Monday', []).append([user['name'], age])
        
    return DAYS
    
    
print(birth_reminder(users))