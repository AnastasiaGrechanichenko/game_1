class Person:
    __section = set ()
    def __init__(self,fio,phone):
        self.__fio = fio
        self.__phone = phone
    def __str__(self):
        return (f"fio:{self.__fio} | phone: {self.__phone}| {self.__section}")
    @property # press props  + Tab
    def fio(self):
        return self.__fio
    @fio.setter
    def fio(self,value):
        self.__fio = value

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,value):
        self.__phone = value

    def add_section(self,name):
        self.__section.add(name)

    def del_section(self,name):
        self.__section.remove(name)






if __name__ == '__main__':
    person = Person("fio","1234")
    print(person)
    person.add_section("бокс")
    print(person)
    person.add_section("аэробика")
    print(person)
    person.del_section("аэробика")
    print(person)


