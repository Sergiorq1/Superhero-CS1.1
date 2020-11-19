class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
my_dog = Dog("Rex", "SuperDoggo")
print(my_dog.breed)
