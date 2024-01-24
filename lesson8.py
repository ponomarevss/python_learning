def show_menu() -> int:
    print("Введите номер пункта меню:\n"
          "1. Импорт таблицы из 'phonebook.txt'\n"
          "2. Добавить строку\n"
          "3. Показать таблицу\n"
          "4. Сохранить актуальное состояние таблицы\n"
          "5. Найти строку по части строки\n"
          "6. Удалить строку по номеру\n"
          "7. Экспортировать строку по номеру\n"
          "9. Закончить работу")
    choice = int(input())
    return choice


def run_phonebook():
    phb = ''
    choice = show_menu()
    while choice != 9:
        if choice == 1:
            phb = import_phonebook()
        elif choice == 2:
            phb = input_line(phb)
        elif choice == 3:
            show_phonebook(phb)
        elif choice == 4:
            save_phonebook(phb)
        elif choice == 5:
            find_line(phb)
        elif choice == 6:
            phb = delete_line(phb)
        elif choice == 7:
            export_line(phb)
        choice = show_menu()
    close_phonebook()


def import_phonebook(name='phonebook.txt') -> str:
    with open(name, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(f'Импортирована телефонная книга')
    return read_data


def input_line(phb: str):
    print("Добавить запись. Ввести фамилию, имя, отчество, номер телефона")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    f_name = input("Введите отчество: ")
    phone_num = input("Введите номер телефона: ")
    line = f"\n{first_name},{last_name},{f_name},{phone_num}"
    return phb + line


def save_phonebook(phb: str):
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(phb)
    print('Телефонная книга сохранена')


def show_phonebook(phb):
    print('Актуальное состояние книги:')
    fields = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    lines = map(lambda x: dict(zip(fields, x.split(','))), phb.split('\n'))
    print(f'{"#":5} {fields[0]:20}{fields[1]:20}{fields[2]:20}{fields[3]:20}')
    for line in list(enumerate(lines)):
        print(
            f'{str(line[0]):5} {line[1]["Фамилия"]:20}{line[1]["Имя"]:20}'
            f'{line[1]["Отчество"]:20}{line[1]["Номер телефона"]:20}')


def find_line(phb):
    print('Поиск записи')
    field = int(input("Введите номер критерия поиска: 0 = Фамилия, 1 = Имя, 2 = Отчество, 3 = Номер телефона: "))
    value = input("Введите часть строки для поиска: ").lower()
    lines = map(lambda x: x.split(','), phb.split('\n'))
    print(f'{"Фамилия":20}{"Имя":20}{"Отчество":20}{"Номер телефона":20}')
    for line in lines:
        if line[field].lower().find(value) >= 0:
            print(f'{line[0]:20}{line[1]:20}{line[2]:20}{line[3]:20}')


def delete_line(phb):
    print('Удаление записи по номеру')
    ind = int(input("Введите номер строки для удаления: "))
    lines = phb.split('\n')
    deleted_line = lines.pop(ind).split(',')
    result = ''
    for line in lines:
        result += line + '\n'
    print(f'Удалена запись #{str(ind):5} {deleted_line[0]:10}'
          f'{deleted_line[1]:10}{deleted_line[2]:10}{deleted_line[3]:10}')
    return result[:-1]


def export_line(phb):
    print('Экспорт записи по номеру')
    file_name = input('Введите имя файла для экспорта: ')
    ind = int(input("Введите номер строки для экспорта: "))
    lines = phb.split('\n')
    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(f'\n{lines[ind]}')
    exported_line = lines[ind].split(',')
    print(f'Экспортирована запись #{str(ind):5} {exported_line[0]:10}'
          f'{exported_line[1]:10}{exported_line[2]:10}{exported_line[3]:10}')


def close_phonebook():
    print("Программа закрыта")


if __name__ == '__main__':
    run_phonebook()
