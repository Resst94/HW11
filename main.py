from datetime import datetime
from collections import UserDict
import re

class Field:
    
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self._validate(new_value)
        self.__value = new_value

    def _validate(self, value):
        pass

    def __str__(self):
        return str(self.__value)

class Name(Field):
    """class for validate name field"""

    def _validate(self, value):
        name_pattern = re.compile(r'^[a-zA-Z0-9а-яА-Я\s]+$')

        if len(value) < 1 or not name_pattern.match(value):
            raise ValueError("Invalid name format")

        print(f'{value} is a valid name')
        super()._validate(value)
class Phone(Field):
    """class for validate phone field"""

    def _validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits")
        
        print(f'{value} is valid phone number')
        super()._validate(value)

class Birthday(Field):
    """class for validating birthday field"""

    def _validate(self, value):
        try:
            day, month, year = map(int, value.split('-'))

            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:

                print(f'{value} is valid birthday')
                return super()._validate(value)
            else:
                raise ValueError('Invalid date: {value}. The date is not correct.')
        except ValueError:
            raise ValueError('Incorrect date format (must be in day-month-year)')

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f'Number phone {phone} has been add'

    def remove_phone(self, phone):
        tel = Phone(phone)
        self.phones = [item for item in self.phones if tel.value != item.value]
        print(f'Number phone {phone} has been delete')

    def edit_phone(self, phone_old, phone_new):
        tel_new = Phone(phone_new)
        for item in self.phones:
            if phone_old == item.value:
                idx = self.phones.index(item)
                self.phones.remove(item)
                self.phones.insert(idx, tel_new)
                return f'Number phone {phone_old} has been edited to {tel_new.value}'
        raise ValueError("Phone number not found for editing")

    def find_phone(self, phone):
        tel = Phone(phone)
        return next((item for item in self.phones if tel.value == item.value), None)

    def days_to_birthday(self):
        today = datetime.now()

        if self.birthday is not None and self.birthday.value is not None:
            birth_day = self.birthday.value
            birth_day = datetime.strptime(birth_day, "%d-%m-%Y")

            next_birthday = datetime(today.year, birth_day.month, birth_day.day)

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birth_day.month, birth_day.day)

            days_until_birthday = (next_birthday - today).days

            return days_until_birthday
        else:
            raise ValueError('Birthday is not set')
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, obj):
        self.data[str(obj.name)] = obj
        phone_numbers = [phone.value for phone in obj.phones]
        print(f"Key {obj.name} with value {phone_numbers} added")

    def find(self, name):
        if name in self.data:
            result = self.data[name]
            return result
        else:
            print(f'{name} not found')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f'{name} deleted')
        else:
            print(f'{name} not found')

    def iterator(self, n=1):
        for i in range(0, len(self.data), n):
            yield list(self.data.values())[i:i + n]

if __name__ == '__main__':
    address_book = AddressBook()
