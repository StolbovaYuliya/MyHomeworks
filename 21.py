# Игра в города с использованием строк Json

""" Коментируем код с прошлого задания
cities_set = set()

# Делаем импорт списка городов
from cities import cities
cities_set = {city['name'].lower() for city in cities}

"""

import json

# записываем в json список городов из файла cities.py
# with open('cities.json', 'w', encoding='utf-8') as f:
#     json.dump(list(cities_set), f, ensure_ascii=False)

# открываем json для чтения городов
with open("cities.json", "r", encoding='utf-8') as file:
    cities_json = file.read()

# Делаем сет с городами
cities_set = set(json.loads(cities_json))

# Список букв, на которые нет городов
bad_letter_list = ['ь', 'ц', 'ъ', 'ы', 'й']

def main():
    """
    Основная функция для запуска игры в города
    :return:
    """


    # Индекс искомой буквы в наименовании города
    last_letter = -1

    # Создаем пустое множество для использованных названий
    used_cities = set()

    # Переменная, содержащая ответ компьютера
    computer_city = None

    # счет компьютера
    comp_game = 0

    # счет игрока
    user_game = 0

    # Цикл игры
    while True:

        user_city = input("Введите название города (или 'стоп' для завершения игры): ").lower().strip()

        # Проверка на стоп
        if user_city.lower() == "стоп":
            # записываем очко компьютеру
            comp_game += 1
            print(f'Вы ввели Стоп. Вы проиграли! Счет: Игрок - {user_game}; Компьютер - {comp_game}')
            break

        # Проверка правил игры
        if computer_city:

            # Определяем индекс буквы
            last_letter = get_last_letter(computer_city[-1])

            if computer_city[last_letter].lower() != user_city[0]:
                comp_game += 1
                print(f'Город на чинается не с той буквы. Вы проиграли! Счет: Игрок - {user_game}; Компьютер - {comp_game}')
                break

        # Проверка хода пользователя
        # Проверяем есть ли введеное значение в списке использованных
        if user_city not in used_cities:

            if user_city in cities_set:

                used_cities.add(user_city)
                # записываем очко игроку
                user_game += 1
                print(f'Ход принят! Счет: Игрок - {user_game}; Компьютер - {comp_game}')

            else:
                comp_game += 1
                print(f'Город не найден! Вы проиграли! Счет: Игрок - {user_game}; Компьютер - {comp_game}')
                break
        else:
            comp_game += 1
            print(f'Этот город уже был использован. Вы проиграли! Счет: Игрок - {user_game}; Компьютер - {comp_game}')
            break

        # Проверяем ход компьютера
        for city in cities_set:

            # Определяем индекс буквы
            last_letter = get_last_letter(user_city[-1])

            if city[0] == user_city[last_letter] and city not in used_cities:
                computer_city = city
                used_cities.add(computer_city.lower())
                comp_game += 1
                print(f'Компьютер: {computer_city}  Счет: Игрок - {user_game}; Компьютер - {comp_game}')
                break
        else:
            user_game += 1
            print(f'Компьютер не смог найти новый город. Вы выиграли! Счет: Игрок - {user_game}; Компьютер - {comp_game}')
            break

def get_last_letter(last_letter:str) -> int:
    """
    Функция определяет индекс последней буквы
    :param last_letter: последняя буква в слове, которую ищем в
        списке "плохихи букв"
    :return: индекс буквы
    """
    if last_letter in bad_letter_list:
        return -2
    else:
        return -1

if __name__ == '__main__':
    main()