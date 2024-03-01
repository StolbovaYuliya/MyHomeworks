
# Задание 1


telephone_user = input("Введите номер телефона").strip()

TELEFHONE_LEN = 11
telephone = telephone_user
error_telephone = ""


# Убираем +, если есть
if telephone.startswith('+'):
    telephone = telephone.replace("+","")


# Удаляем скобки
if telephone.find("(") or telephone.find(")"):
    telephone = telephone.replace("(","")
    telephone = telephone.replace(")", "")


# удаляем тире
if telephone.find("-"):
    telephone = telephone.replace("-","")


# Убираем лишние пробелы
if telephone.find(" "):
    telephone = telephone.replace(" ","")


# Проверяем длину, она должна быть равна 11
if len(telephone) < TELEFHONE_LEN:

    error_telephone += "Номер телефона слишком короткий!" + '\n'

if len(telephone) > TELEFHONE_LEN:
    error_telephone += "Номер телефона слишком длинный!" + '\n'

# Проверяем, что номер телефона состоит только из цифр
if not telephone.isdigit():
    error_telephone += "Номер телефона должен состоять только из цифр!" + '\n'

# Проверяем начинается ли номер на 7 или 8
if not telephone.startswith('8'):
    if not telephone.startswith('7'):
        error_telephone += "Номер телефона должен начинаться на цифры 7 или 8!" + '\n'



if error_telephone:
    print(f' Номер телефона {telephone_user} введен не корректно! Причины: \n {error_telephone}')
else:
    print(f' {telephone_user} - номер телефона принят.')




# Задание2

PASS_LEN = 7

user_input = input("Ведите пароль не менее 7 символов: ")
user_error = ""
password = user_input.strip()


# Проверяем длину пароля
if len(password) < PASS_LEN:
    user_error += 'Пароль слишком короткий. Он должен содержать не менее 7 символов!' + '\n'

#  Проверяем на содержание пробелов
if ' ' in password:
    user_error += 'Пароль содержит пробел' + '\n'

if password.isalpha():
    user_error += 'Пароль содержит только буквы' + '\n'


if password.isdigit():
    user_error += 'Пароль содержит только цифры' + '\n'

if password.isupper():
    user_error += 'Пароль состоит только из заглавных букв' + '\n'

if password.islower():
    user_error += 'Пароль состоит только из строчных букв' + '\n'


if not any(char in ".,:;!_*-+()/#¤%&)" for char in password):
    user_error += 'Пароль должен содержать хотябы один спецсимвол' + '\n'


if  user_error:
    print(f'Пароль {user_input} не корректный. Причины:\n {user_error}')
else:
    print(f'Пароль {user_input} принят.')


# Задание3

# Секретное послание
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
['и$ #sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


secret_message = ""

for row in secret_letter:
    for letter in row[0]:
        if letter.islower():  # проверяем, что символ является маленькой буквой
            if letter in small_rus:  # проверяем, что символ есть в списке small_rus

                secret_message += letter +" " # добавляем букву  к расшифрованному сообщению


print(secret_message)

