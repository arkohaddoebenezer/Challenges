import math

class Main:
    def get_century(self, year):
        return math.ceil(year / 100)
        
my_object = Main()
year = 2024
century = my_object.get_century(year)

print(f"Year: {year} is in the {century}th century.")
