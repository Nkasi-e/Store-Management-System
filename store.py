# Creating class
import csv  # importing csv to be able to read the csv file



class Item:
    # class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all_items = []
    
    def __init__(self, name: str, price: float, quantity=0) -> None:
        
    # Run validations to the received arguments using #assert
       assert price >= 0, f'Price {price} is not greater than or equal to 0'
       assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to 0'
       
    # Assign to self Object
       self.name = name
       self.price = price
       self.quantity = quantity
       
    # Actions to execute
       Item.all_items.append(self)
       
       # Methods
    def calculate_total_price(self,):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    # Reading/Instantiate from csv file
    @classmethod # Decorator
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f) # to covert csv into python dictionary
            items = list(reader) # converting into a list
        
        for item in items:
           Item(
               name=item.get('name'),
               price=float(item.get('price')),
               quantity=int(item.get('quantity'))
           )
    
    # representing our list as a list and not default python rep, using the magic method __repr__
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        

# creating and instance of the above class
# Instance Attribute
# item1 = Item('Phone', 100, 8)
# item2 = Item('Laptop', 200, 10)
# item3 = Item('Car', 150, 5)
# item4 = Item('Monitor', 400, 1)
# item5 = Item('Book', 600, 3)

Item.instantiate_from_csv()

# print(Item.all_items)






