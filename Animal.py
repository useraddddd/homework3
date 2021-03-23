class Animal:
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
    def call(self):
        print("叫...")
    def run(self):
        print("跑...")

class Cat(Animal):
    def __init__(self,name,color,age,sex):
        super().__init__(name,color,age,sex)
        self.hair = "短毛"
        # print(f"{name,color,age,sex,hair}")
    def call(self):
        print("喵喵叫")
    def catch(self):
        print(f"{self.name} catch mouse")
class Dog(Animal):
    def __init__(self,name,color,age,sex):
        super().__init__(name,color,age,sex)
        self.hair = "长毛"
        # print(f"{name, color, age, sex, hair}")
    def call(self):
        print("汪汪")
    def home(self):
        print(f"{self.name} stay home")

if __name__ == '__main__':
    cat1 = Cat("tom","green","20","man")
    cat1.catch()
    print(f"{cat1.name,cat1.color,cat1.age,cat1.sex,cat1.hair}")
    dog1 = Dog("jerry","red","100","man")
    dog1.home()
    print(f"{dog1.name,dog1.color,dog1.age,dog1.sex,dog1.hair}")


