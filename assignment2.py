import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f"Your age is {age}")

    def listAnniversaries(self):
        currentYear = 2022
        age = currentYear - self.year
        return [anniversary for anniversary in range(10, age + 1, 10)]

    def modifyYear(self, n):
        first_part = str(self.year)[:2] * n
        
        multiplied_year = str(self.year * n)
        second_part = ''.join([multiplied_year[i] for i in range(len(multiplied_year)) if i % 2 == 0])

        return first_part + second_part

    @staticmethod
    def checkGoodString(string):
        if len(string) < 9 or not string[0].islower():
            return False
        return sum(char.isdigit() for char in string) == 1

    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
            return True
        except:
            return False
