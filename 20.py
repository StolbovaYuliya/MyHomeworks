

# Игра в города

# Делаем импорт списка городов
from cities import cities
cities_set = {city['name'].lower() for city in cities}

# Список букв, на которые нет городов
bad_letter_list = ['ь', 'ц', 'ъ', 'ы', 'й']

# Индекс искомой буквы в наименовании города
last_letter = -1

# Создаем пустое множество для использованных названий
used_cities = set()

# Переменная, содержащая ответ компьютера
computer_city = None

# Цикл игры
while True:

    user_city = input("Введите название города (или 'стоп' для завершения игры): ").lower()

    # Проверка на стоп
    if user_city.lower() == "стоп":
        print("Вы ввели Стоп. Вы проиграли!")
        break

    # Проверка правил игры
    if computer_city:

        # Определяем индекс буквы
        if computer_city[-1] in bad_letter_list:
            # Если в списке плохих букв
            last_letter = -2
        else:
            last_letter = -1

        if computer_city[last_letter].lower() != user_city[0]:
            print("Город на чинается не с той буквы. Вы проиграли!")
            break

    # Проверка хода пользователя
    # Проверяем есть ли введеное значение в списке использованных
    if user_city not in used_cities:

        if user_city in cities_set:

            used_cities.add(user_city)
            print('Ход принят!')

        else:
            print('Город не найден! Вы проиграли!')
            break
    else:
        print("Этот город уже был использован. Вы проиграли!")
        break

    # Проверяем ход компьютера
    for city in cities_set:
        if user_city[-1] in bad_letter_list:
            last_letter = -2
        else:
            last_letter = -1

        if city[0] == user_city[last_letter] and city not in used_cities:
            computer_city = city
            used_cities.add(computer_city.lower())
            print(f"Компьютер: {computer_city}")
            break
    else:
        print("Компьютер не смог найти новый город. Вы выиграли!")
        break
