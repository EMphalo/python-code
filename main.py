import csv

class Item:
    
    all = []

    pay_rate = 0.8 #the pay rate after 20% discount
    
    def __init__(self, name:str, price:float, quantity = 0):
        #run validation
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price= float( item.get('price')),
                quantity = int( item.get('quantity')),
            )
        
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity })"
    
# item = Item("Phone", 100, 1)
# item1 = Item("Laptop", 1000, 3)
# item2 = Item("Cable", 10, 5)
# item3 = Item("Mouse", 50, 5)
# item4 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance)

Item.instantiate_from_csv()

print(Item.all)


