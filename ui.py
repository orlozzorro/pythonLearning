from logger import input_data, print_data, edit_data, delete_data

def interface():
    print("Добрый день! Вы попали на спецаильный бот \n 1. - запись данных \n 2. - вывод данных"
          "\n 3. - редактировать данные \n 4. - удалить данные")
    command = int(input('Введите число '))
    while command not in [1,2,3,4]:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        delete_data()

interface()