from models import Food
from views import FoodView


class FoodTemplate:
	
	#static object of FoodView
	foodviewobj = FoodView()
	
	def foodOperation(self):
		
		print("1.Add Food ")
		print("2.Show All Food ")
		print("3.Show Food By Id ")
		print("4.delete Food")
		print("5.Update Food")
		
		choice = int(input("Enter Your choice"))
		
		if choice == 1:
			print("Enter New Food Details")
			#foodId = int(input("Enter Food Id "))
			foodName = input("Enter Food Name ")
			foodType = input("Enter Food Type ")
			foodCategory = input("Enter Food Category ")
			foodPrice = float(input("Enter Food Price "))
			foodDescription = input("Enter Food Description ")
			
			foodobj = Food(0,foodName,foodType,foodCategory,foodPrice,foodDescription)
			flag = FoodTemplate.foodviewobj.addFood(foodobj)
			
			if flag==True:
				print("Food is Added")
			else:
				print("Food is Not Added")
		
		elif choice ==2:
			foodlist = FoodTemplate.foodviewobj.showAllFood()
			if foodlist is not None:
				for food in foodlist:
					print(food)
			else:
				print("No Food Found ")
				
		elif choice ==3:
			foodId = int(input("Enter Food Id  to be Search "))
			foodobj = FoodTemplate.foodviewobj.showFoodById(foodId)
			if foodobj is not None:
				print(foodobj)
			else:
				print("No Food Found ")
				
		elif choice == 4:
			foodId = int(input("Enter Food Id  to be Delete "))
			
			foodobj = FoodTemplate.foodviewobj.showFoodById(foodId)
			
			if foodobj is not None:
				isdelete = input("Do you Want to delete this food(press y/n)")

				if isdelete == "y":
					flag = FoodTemplate.foodviewobj.deleteFood(foodId)

					if flag==True:
						print("Food is Deleted.")
					else:
						print("Food is Not Deleted.")
				else:
					print("Okay No Probleam")
			else:
				print("No Food Found ")
		elif choice == 5:
		
		#foodId = int(input(Enter Food Id "))
			foodId=input("Enter food ID : ")
			foodName = input("Enter Food Name ")
			foodType = input("Enter Food Type ")
			foodCategory = input("Enter Food Category ")
			foodPrice = float(input("Enter Food Price "))
			foodDescription = input("Enter Food Description ")
			
			foodobj = Food(foodId,foodName,foodType,foodCategory,foodPrice,foodDescription,)
			flag = FoodTemplate.foodviewobj.updateFood(foodobj)
			
			if flag==True:
				print("Food is updated")
			else:
				print("Food is Not Added")
				
			
						

			
			
				
			
