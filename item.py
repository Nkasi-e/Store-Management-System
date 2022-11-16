# Creating parent class
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
       self.__name = name
       self.__price = price
       self.quantity = quantity
       
    # Actions to execute
       Item.all_items.append(self)
    
     # Property Decorator = Read-Only Attribute - can't set attributes
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price =self.__price + self.__price * increment_value
        
    # Property Decorator - for setting attribute
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('Name must be less than 11 character long')
        elif len(value) < 5:
            raise Exception('Name must be at least 5 character long')
        else:
            self.__name = value
            
    @price.setter
    def price(self, value):
       self.__price = value
       
       # Methods
    def calculate_total_price(self,):
        return self.__price * self.quantity
    
    # Reading/Instantiate from csv file
    @classmethod # Decorator
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # to covert csv into python dictionary
            items = list(reader) # converting into a list
        
        for item in items:
           Item(
               name=item.get('name'),
               price=float(item.get('price')),
               quantity=int(item.get('quantity'))
           )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    # representing our list as a list and not default python rep, using the magic method __repr__
    # generic way to access to the name of the class from the instance is using the magic method self.__class__.__name__
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    # Abstraction
    def __connect(self, smtp_server, smtp_port):
        pass
    
    def __email_body(self):
        return f"""
        Hello {self.__name}.
        We have {self.quantity} times
        Best Regards, OOPBecklin
        """
        
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect()
        self.__email_body()
        self.__send()