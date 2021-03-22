# <super>

# super: 다중 상속일 경우 맨 처음 클래스에 대해서만 생성자를 호출함

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() => 단일 상속일 때
        Unit.__init__(self) #=> 다중 상속일 때
        FlyableUnit.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

