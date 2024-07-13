from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные: \n\n'
                    f"1. Вариант: \n"
                    f"{name} \n {surname}\n{phone}\n{address}\n\n"
                    f"2. Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name} \n {surname}\n{phone}\n{address}")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


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

def edit_data():
    print_data()
    var = int(input(f'В каком файл внести изменения: \n'
                    "1. Файл 1\n"
                    "2. Файл 2\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name} \n {surname}\n{phone}\n{address}")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n") 
    
def delete_data():
    print('delete')
    
