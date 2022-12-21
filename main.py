from datetime import datetime
from datetime import timedelta

# Тестовий словник з датами днів народження працівників
'''test = {
    "Mary": "27-12-2022",
    "Jary": '20-12-2022',
    'Tom': "26-12-2022",
    'Artur': "22-12-2022",
    "Bob": '21-12-2022',
    "Luffy": '26-12-2022',
    "Jack": '25-12-2022',
    "Jerry": '29-12-2022',
    "Jer": '29-12-2022'}
'''
test = {
 "Mary": "19-12-2022",
 "Jary": '20-12-2022',
 'Tom': "26-12-2022",
 'Artur': "22-12-2022",
 "Bob": '21-12-2022',
 "Luffy": '24-12-2022',
 "Jack": '25-12-2022',
 "Jerry": '29-12-2022',
 "Jer": '29-12-2022'
}
main_dict = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []}


# Функція, яка перевіряє чи входить дата з словника в діапазон
# дат з цієї суботи по наступну п'ятницю та розподіляє дати по дням тижня
def get_birthdays_dict(workers: dict) -> dict:
    today = datetime.now()
    # Визначення дати цієї суботи
    s = today + timedelta((5 - today.weekday()) % 7)
    saturday = s - timedelta(days=7)
    # Визначення дати наступної п'ятниці
    f = today + timedelta((4 - today.weekday()) % 7)
    friday = f
    #friday = f + timedelta(days=7)
    for name, dat in workers.items():
        day = datetime.strptime(dat, "%d-%m-%Y")
        if saturday <= day <= friday:
            if day.weekday() in [0, 5, 6]:
                main_dict["Monday"].append(name)
            if day.weekday() == 1:
                main_dict["Tuesday"].append(name)
            if day.weekday() == 2:
                main_dict["Wednesday"].append(name)
            if day.weekday() == 3:
                main_dict["Thursday"].append(name)
            if day.weekday() == 4:
                main_dict["Friday"].append(name)
    return main_dict


def get_birthdays_per_week():
    for day, names in get_birthdays_dict(test).items():
        print(f'{day}: {names}')


def main():
    try:
        get_birthdays_per_week()
    except ValueError:
        print("Будь ласка, перевірте правильність написання дати дня народження!")


if __name__ == '__main__':
    main()
