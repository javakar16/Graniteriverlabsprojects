class DataSet:
    def __init__(self,dist,time):
        self.dist=dist
        self.time=time
        self.speed=0
    def calculate(self):
        self.speed=self.dist//self.time
class UserInput():
    Attribute1=[]
    def Method1(self):
        for i in range(10):
            UserInput.Attribute1.append(DataSet(int(input()),int(input())))

class Measure(UserInput):
    def Method1(self):
        for i in range(10):
            UserInput.Attribute1[i].calculate()

class ShowResults(UserInput):
    def Method1(self):
        import csv
        with open('output.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            for i in range(10):
                print(UserInput.Attribute1[i].dist, UserInput.Attribute1[i].time, UserInput.Attribute1[i].speed)
                row=[UserInput.Attribute1[i].dist,UserInput.Attribute1[i].time,UserInput.Attribute1[i].speed]
                writer.writerow(row)


u1=UserInput()
u1.Method1()
u2=Measure()
u2.Method1()
u3=ShowResults()
u3.Method1()
