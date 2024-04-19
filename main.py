from item import Item
from phone import Phone

# item = Item("Phone", 100, 1)
# item1 = Item("Laptop", 1000, 3)
# item2 = Item("Cable", 10, 5)
# item3 = Item("Mouse", 50, 5)
# item4 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance)

Item.instantiate_from_csv()

# print(Item.all)

# print (Item.is_integer(7.0))

phone1 = Phone("HuaweiPhonev10",500,5,1)

print(Item.all)
print(Phone.all)

