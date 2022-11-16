from item import Item

# INHERITANCE
# Inheriting from the parent class Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # Call to super method to have acess to all attributes / methods
        super().__init__(name, price, quantity)
        
        assert broken_phones >= 0, f"Broken Phone {broken_phones} is not greater than equal to zero"
        
        self.broken_phones = broken_phones