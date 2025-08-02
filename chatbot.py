'''
class - blueprint
object/instance of that class - object created using the blueprint


examples:

blueprint - digram of your house
object - your actual house built using that digram

blueprint - cake recipe
object - cake made using that recipe

'''
# class Car:
#     def __init__(self, name, color, brand, year):
#         self.name = name
#         self.color = color
#         self.brand = brand
#         self.year = year

#     def create(self):
#         print(f"Creating a car: {self.name}, Color: {self.color}, Brand: {self.brand}, Year: {self.year}")

#     def get_cars_year(self):
#         print(f"Car Year: {self.year}")

#     def get_cars_name(self):
#         print(f"Car Name: {self.name}")

# car = Car("Model S", "Red", "Tesla", 2020)
# car.get_cars_year()

# car2 = Car("Mustang", "Blue", "Ford", 2021)
# car2.get_cars_name()

class Chatbot:
    def __init__ (self, model_name):
        self.model_name = model_name
        self.message_history = []
    
    def get_model_name(self):
        print(f"Model Name: {self.model_name}")

    def add_message_to_history(self, message, sender):
        if message is None or message.strip() == "":
            raise ValueError("message cannot be empty")
        
        self.message_history.append(
            {'role': sender, 'content': message}
        )

    def get_ai_response(self):
        
    
