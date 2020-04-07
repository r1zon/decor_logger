from logger import path_logs
import os.path

path = input('Введите название файла для логирования.\n')

class Contact:
    def __init__(self, name, surname, phone_number, elect='нет', **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.add_info = kwargs
        self.elect = elect
        self.contact = {'Имя': self.name,
                        'Фамилия': self.surname,
                        'Телефон': self.phone_number,
                        'В избранных': self.elect,
                        'Дополнительная информация':
                            self.add_info
                        }

    def return_inf(self):
        print(f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Телефон: {self.phone_number}\n' \
        f'В избранных: {self.elect}')
        print('Дополнительная информация:')
        for key, value in self.add_info.items():
            print('{0:>5}{1}: {2}'.format(' ',key,value))

    def __str__(self):
        self.return_inf()
        return str()


class PhoneBook:
    def __init__(self, phonebook_name):
        self.name = phonebook_name
        self.contacts = []

    @path_logs(path)
    def print_contact(self, contacts):
        for key, value in contacts.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for keys, values in value.items():
                    print('{0:>5}{1}: {2}'.format(' ', keys, values))
            else:
                print('{}: {}'.format(key, value))

    @path_logs(path)
    def show_contacts(self):
        if self.contacts == []:
            print('В справочнике отсутсвуют контакты')
            return 'В справочнике отсутсвуют контакты'
        else:
            print('Список контактов:')
            for i,contacts in enumerate(self.contacts, 1):
                print('*'*25)
                print(f'Контакт №{i}')
                self.print_contact(contacts)
            return self.contacts

    @path_logs(path)
    def add_contact(self, name, surname, phone_number, *args, **kwargs):
        self.contacts.append(Contact(name, surname, phone_number, *args, **kwargs).contact)
        return Contact(name, surname, phone_number, *args, **kwargs).contact

    @path_logs(path)
    def del_contact_on_number(self, phone_number):
        count_del_contact = 0
        if self.contacts == []:
            print('В справочнике отсутсвуют контакты')
            return 'В справочнике отсутсвуют контакты'
        else:
            for contact in self.contacts:
                if contact['Телефон'] == phone_number:
                    self.contacts.remove(contact)
                    count_del_contact +=1
                    break
            if count_del_contact == 1:
                print(f'Контакт с номером {phone_number} удален.')
                return f'Контакт с номером {phone_number} удален.'
            else:
                print(f'Контакт с номером {phone_number} не найден.')
                return f'Контакт с номером {phone_number} не найден.'

    @path_logs(path)
    def find_elect_numbers(self):
        elect_contacts = []
        not_elect_contacts = 0
        if self.contacts == []:
            print('В справочнике отсутсвуют контакты')
            return 'В справочнике отсутсвуют контакты'
        else:
            for contact in self.contacts:
                if contact['В избранных'] == 'да':
                    self.print_contact(contact)
                    elect_contacts.append(contact)
                if 'да' not in contact['В избранных']:
                    not_elect_contacts += 1
        if not_elect_contacts == len(self.contacts):
            print('Избранные контакты отсутсвуют.')
            return 'Избранные контакты отсутсвуют.'
        else:
            return elect_contacts

    @path_logs(path)
    def find_on_name_surname(self, name, surname):
        if self.contacts == []:
            print('В справочнике отсутсвуют контакты')
            return 'В справочнике отсутсвуют контакты'
        else:
            full_name_f = name + ' ' + surname
            for contact in self.contacts:
                full_name = contact['Имя'] + ' ' + contact['Фамилия']
                if full_name == full_name_f:
                    self.print_contact(contact)
                    return contact
                else:
                    print(f'Контак {name} {surname} не найден.')
                    return f'Контак {name} {surname} не найден.'

def clear_logs(path):
    with open(path, 'w', encoding='utf-8') as f:
        print(f'Документ {path} очищен.')
        pass

def main():
    name_phone_book = input('Введите название телефонной книги\n')
    phone_book = PhoneBook(name_phone_book)
    while True:
        action = input('Введите команду:\n' \
                 'a - добавить контакт в книгу\n' \
                 's - показать список конатктов\n' \
                 'd - удалить контакт по номеру телефона\n'
                 'f - найти избранные контакты\n'
                 'fns - найти контакт по имени и фамилии\n'
                 'с - очистить логи\n'
                 'q - выйти из программы\n')
        if action == 'a':
            while True:
                try:
                    name, surname = input('Введите имя и фамилию контакта через пробел:\n').split()
                except ValueError:
                    print('Введите данные корректно')
                else:
                    break
            phone_number = input('Введите номер телефона:\n')
            while True:
                elect = input('Является ли контакт избранным? Введите да или нет\n').lower()
                if elect == 'да' or elect == 'нет':
                    break
                else:
                    print('Введите да или нет.\n')
            add_info_dict = {}
            while True:
                try:
                    add_info = input('Введите дополнительную информацию: название соц сети и логин через пробел\n'
                                     'Для выхода нажмите q\n').split()
                    if add_info == ['q']:
                        break
                    else:
                        add_info_dict.update(dict([add_info]))
                except ValueError:
                    print('Введите корректно дополнительную информацию')
            cont = Contact(name, surname, phone_number, elect, **add_info_dict)
            print('Демонстрация работы print задания №1:')
            print(cont)
            phone_book.add_contact(name, surname, phone_number, elect, **add_info_dict)
        if action == 's':
            phone_book.show_contacts()
        if action == 'd':
            phone_number = input('Введите номер телефона, по которому нужно удалить контакт\n')
            phone_book.del_contact_on_number(phone_number)
        if action == 'f':
            phone_book.find_elect_numbers()
        if action == 'c':
            while True:
                if os.path.exists(path):
                    clear_logs(path)
                    break
                else:
                    print(f'Файл {path} не сущестувет, попробуйте снова.')
        if action == 'fns':
            while True:
                try:
                    name, surname = input('Введите имя и фамилию искомого контакта через пробел\n').split()
                except ValueError:
                    print('Введите данные корректно')
                else:
                    break
            phone_book.find_on_name_surname(name, surname)
        if action == 'q':
            break

if __name__ == '__main__':
    main()
