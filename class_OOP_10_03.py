# int.__dict__
# list.__dict__
# dir(int)

# class A:
    # pass
# print(A)
"""
class Car:
    consumption_fuel = 0
    tank_volume = 0
    service_count = 0

    def __init__(self, tank_volume):
        self.tank_volume = tank_volume
    
    def fill_tank(self):
        self.consumption_fuel += self.tank_volume
    
    def service(self):
        self.service_count += 1
        # self.consumption_fuel += 1

Mers = Car(100)
print(Mers.tank_volume)
Mers.fill_tank()
Mers.service()
print(Mers.__dict__)
"""
# Misol my version
# class Elf:
    # def __init__(self):
    #     self.file_test = open("test.txt", "r")
    #     self.result = ''
    # # file_test = open("test.txt", "r")
    # # result = ''

    # def sana(self):
    #     for i in self.file_test:
    #         self.result += i

    #     self.result = self.result.split("\n\n")
        
    #     for id, val in enumerate(self.result):
    #         self.result[id] = val.split('\n')

    #     res = [list(map(int, i)) for i in self.result]
    #     self.result = res
    #     sol= 0 

    #     for id, val in enumerate(self.result):
    #         sol = sum(val) if sum(val) > sol else sol
        
    #     return sol
# res = Elf()
# print(res.sana())

class ELF:
    def __init__(self):
        self.value = 0  
        self.lis = []
    def count(self, number):
        self.value += int(number)
    def Best_Hight(self):
        F = open('test.txt', 'r')
        for i in F:
            if i.strip() != '':
                self.count(i)
            else:
                self.lis.append(self.value)
                self.value = 0
        return max(self.lis)


Barry = ELF()
print(Barry.Best_Hight())

"""
file_test = open('test.txt', 'r')
result = ''
j = 0
for i in file_test:
    result += i

result = result.split("\n\n")
print(result)
for id, val in enumerate(result):
    result[id] = val.split('\n')

res = [list(map(int, i)) for i in result]
result = res
sol= 0 

for id, val in enumerate(result):
    if sum(val) > sol:
        sol = sum(val)
        
print(sol)
file_test.close()
"""