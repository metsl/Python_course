class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("move in the water")

    def breathe(self):
        super().breathe()
        print("doing this Under water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"number of eyes are {nemo.num_eyes}")