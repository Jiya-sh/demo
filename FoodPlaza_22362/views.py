from database import mydatabase,mycursor
from models import Food


class FoodView:
	
	# Instance method 
	
	def addFood(self,foodobj):
		try:
			sqlQuery ="Insert into food_22362 (foodName,foodType,foodCategory,foodPrice,foodDescription) values ('{}','{}','{}',{},'{}')".format(foodobj.getFoodName(),foodobj.getFoodType(),foodobj.getFoodCategory(),foodobj.getFoodPrice(),foodobj.getFoodDecription())
			print(foodobj)
			i = mycursor.execute(sqlQuery)
			mydatabase.commit()
			if i>0:
				return True
			
			
		except Exception as e:
			print("Error :- ",e)

		return False
	
	def updateFood(self,foodobj):
		 
			try:
				
				sql="update food_22362 set foodName='{}',foodType='{}',foodCategory='{}',foodPrice={},foodDescription='{}' where foodId={}".format(foodobj.getFoodName(),foodobj.getFoodType(),foodobj.getFoodCategory(),foodobj.getFoodPrice(),foodobj.getFoodDecription(),foodobj.getFoodId());
				i = mycursor.execute(sql)
				mydatabase.commit()
			except Exception as e:
				print("Error :- ",e)

			return False;	
	
	def deleteFood(self,foodId):
		try:
			sqlQuery="delete from food_22362 where foodId={}".format(foodId)
			
			i = mycursor.execute(sqlQuery)
			mydatabase.commit()
			if i >0 :
				return True		
			
		except Exception as e:
			print("Error ",e)
		return False
	
	def showAllFood(self):
		try:
			foodlist = []
			sqlQuery = "select * from food_22362"

			i = mycursor.execute(sqlQuery)
			if i>0:
				rows = mycursor.fetchall()
				for row in rows:
					foodobj = Food(row[0],row[1],row[2],row[3],row[4],row[5])
					foodlist.append(foodobj)
				return foodlist
		except Exception as e:
			print(e)
		
		return None
		
		
				
	
	def showFoodById(self,foodId):
		try:
			sqlQuery = "select * from food_22362 where foodId={}".format(foodId)
			i = mycursor.execute(sqlQuery)
			if i>0:
				row = mycursor.fetchone()
				foodobj = Food(row[0],row[1],row[2],row[3],row[4],row[5])
				return foodobj
		except Exception as e:
			print(e) 
		return None
	
		
	
class CustomerView:
	pass


class CartView:
	pass


class OrderView:
	pass
	
	