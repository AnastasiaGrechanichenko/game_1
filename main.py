class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__name} | {self.__age}"

class Group:
    __students = set()
    def __init__(self,name):
        self.__name = name


    def __str__(self):
        result = ""
        for i in self.__students:
            result += str(i) +"\n"
        return f"{self.__name} \n{result}"
    def add_student(self,student):
        if isinstance(student,Student):
            self.__students.add(student)

            print("Это студент ")# записать дома
        else:
            print("Это не студент")



if __name__ == '__main__':
    st = Student("Vasian", 25)
    print(st)
    info = str(st)

    group = Group("1A")
