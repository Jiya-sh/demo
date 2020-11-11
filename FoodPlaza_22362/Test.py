
from templates import FoodTemplate
print("1.Food ")
print("2.Customer")
print("3.Cart")
print("4.Order")
print("5.Exit")

choice = int(input("Enter Your choice"))
if choice == 1:
	foodtemplateobj = FoodTemplate()
	foodtemplateobj.foodOperation()
elif choice == 2:
	pass
elif choice == 3:
	pass
elif choice == 4:
	pass
elif choice == 5:
	pass
else:
	print("Invalid ")
		