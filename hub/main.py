class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()}, {self.cuisine_type.title()}')

    def open_rest(self):
        print(f'Ресторан {self.restaurant_name.title()} открыт!')

rest = restaurant('Mish', 'rus')

rest.describe_restaurant()

rest.open_rest()
