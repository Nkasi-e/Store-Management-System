# Most notes here refers to the main code snipet.. You may need to refer to the code to understand if you're a beginner

# Decorators in Python is just a quick way to change the behaviors of the function we would write by basically calling them just before the line that we create our function, and it starts with the @ sign e.g @classmethod, it also convert a function to be a class method


print(Item.__dict__) # __dict__ gives All the attributes for Class level
print(item1.__dict__) # __dict__ gives All the attributes for Class level
pass # so we wont receive any error inside this class definition

item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.5 # setting your attribute from your instance to override the class attribute value
item2.apply_discount() # Accessing class attributes from your instance

# Looping through your List
for instance in Item.all_items:
    print(instance.name)
    
# A class attribute is an attribute that is going to belong to the class itself burt however you can also access this attribute from the instance level as well