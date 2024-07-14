from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные: \n\n'
                    f"1. Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2. Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name} \n {surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('===================Вывожу данные=============== \n')
    print('Вывод из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывод из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
    print('===================Вывод завершен=============== \n')

def read_first_file():
    print('===================Вывожу данные из файла 1=============== \n')
    data_dict = {}
    list_to_dict = []
    count = 1 # первый ключ словаря
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first_list = f.readlines()
        for i in range (len(data_first_list)):
            if data_first_list[i] == '\n':
                data_dict[count] = list_to_dict
                list_to_dict = []
                count += 1
            else:
                list_to_dict.append(data_first_list[i])
            if i == len(data_first_list) - 1 :
                data_dict[count] = list_to_dict 
        for i in data_dict:
            print(f'запись {i}')
            print(''.join(data_dict[i]))
        print('===================Вывод из файла 1 завершен=============== \n')
    return data_dict

def read_second_file():
    data_dict = {}
    print('===================Вывожу данные из файла 2=============== \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        for i in range(len(data_second)):
            data_dict[i+1] = data_second[i].split(';')
        for i in data_dict:
            print(f'запись {i}: {';'.join(data_dict[i])}')
    print('===================Вывод из файла 2 завершен=============== \n')
    return data_dict



def change_data(file_type):
    if file_type == 1:
        data_dict = read_first_file()
    elif file_type == 2:
        data_dict = read_second_file()
    record_to_change = int(input('Какую запись вы хотите изменить: '))
    if record_to_change not in data_dict:
        print('Что-то пошло не так. Попробуй ввести другую цифру. напоминаю')
        change_data(file_type)
    else:
        dict_to_change = {}
        new_list = []
        c = 1
        for item in (data_dict[record_to_change]):
            dict_to_change[c] = item
            c += 1
        print('что меняем?(1 -имя, 2 - фамилия, 3 - телефон, 4 - адрес)')
        for item in dict_to_change:
            print(f'{item}. {dict_to_change[item]}')
        rec_to_change = int(input('Введите цифру: '))
        if rec_to_change in dict_to_change and file_type == 1:
            if rec_to_change == 1:
                name = name_data()
                dict_to_change[rec_to_change] = name + "\n"
            if rec_to_change == 2:
                surname = surname_data()
                dict_to_change[rec_to_change] = surname + "\n"
            if rec_to_change == 3:
                phone = phone_data() 
                dict_to_change[rec_to_change] = phone + "\n" 
            if rec_to_change == 4:
                address = address_data()
                dict_to_change[rec_to_change] = address + "\n"
        if rec_to_change in dict_to_change and file_type == 2:
            if rec_to_change == 1:
                name = name_data()
                dict_to_change[rec_to_change] = name 
            if rec_to_change == 2:
                surname = surname_data()
                dict_to_change[rec_to_change] = surname
            if rec_to_change == 3:
                phone = phone_data() 
                dict_to_change[rec_to_change] = phone 
            if rec_to_change == 4:
                address = address_data()
                dict_to_change[rec_to_change] = address + "\n"
        else:
            print('Что-то пошло не так. Попробуй ввести другую цифру')
            change_data(data_dict, record_to_change, file_type)
        for item in dict_to_change:
            new_list.append(dict_to_change[item])
        data_dict[record_to_change] = new_list
        edit_data_in_file(data_dict, file_type)
   

def edit_data_in_file(data_dict, file_type):
    if file_type == 1:
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for item in data_dict:
                f.write(f'{''.join(data_dict[item])}\n')
    if file_type == 2:
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for item in data_dict:
                f.write(f'{';1'.join(data_dict[item])}')


def edit_data():
    print_data()
    var = int(input(f'В каком файле внести изменения: \n'
                    "1. Файл 1\n"
                    "2. Файл 2\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))
    change_data(var)

def delete_data():
    var = int(input(f'В каком файле удлаить данные: \n'
                    "1. Файл 1\n"
                    "2. Файл 2\n"))
    if var == 1:
        data_dict = read_first_file()
    if var == 2:
        data_dict = read_second_file()
    record_to_del = int(input('Какую запись вы хотите удалить: '))
    if record_to_del not in data_dict:
        print('Что-то пошло не так. Попробуй ввести другую цифру. напоминаю')
        change_data(var)
    else:
        del data_dict[record_to_del]
        edit_data_in_file(data_dict, var)
