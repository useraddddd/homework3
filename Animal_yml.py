
import yaml


class Animal:
    def __init__(self,name,color,age,sex):
        self.name:str = name
        self.color:str = color
        self.age:str = age
        self.sex:str = sex
    def call(self):
        print("叫...")
    def run(self):
        print("跑...")

class Cat(Animal):
    def __init__(self,name,color,age,sex,hair):
        super().__init__(name,color,age,sex)
        self.hair:str = hair
    def call(self):
        print("喵喵叫")
    def catch(self):
        print(f"{self.name} catch mouse")
class Dog(Animal):
    def __init__(self,name,color,age,sex,hair):
        super().__init__(name,color,age,sex)
        self.hair:str = hair
    def call(self):
        print("汪汪")
    def home(self):
        print(f"{self.name} stay home")

if __name__ == '__main__':
    with open("animal.yaml") as f:
        data = yaml.safe_load(f)

    cat1 = Cat(*tuple(data['no1']))
    print(f"小猫属性: {cat1.name,cat1.color,cat1.age,cat1.sex,cat1.hair}")
    dog1 = Dog(*tuple(data['no2']))
    print(f"小狗属性: {dog1.name,dog1.color,dog1.age,dog1.sex,dog1.hair}")



