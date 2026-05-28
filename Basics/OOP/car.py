class Car:

    def __init__(self, model , year , colour, for_sale):
        self.model = model 
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving {self.model}")

    def stop(self):
        print(f"Your {self.model} is stopped")

    def describe_car(self):
        print(f"The car is : {self.model}, {self.year} year model, {self.colour} coloured.")