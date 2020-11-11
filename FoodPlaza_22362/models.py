
class Food:
	
	def __init__(self,foodId,foodName,foodType,foodCategory,foodPrice,foodDescription):
		self.__foodId = foodId
		self.__foodName = foodName
		self.__foodType = foodType
		self.__foodCategory = foodCategory;
		self.__foodPrice = foodPrice
		self.__foodDescription = foodDescription
		
	def setFoodId(self,foodId):
		self.__foodId = foodId
	
	def getFoodId(self):
		return self.__foodId
	
	
	def setFoodName(self,foodName):
		self.__foodName = foodName
	
	def getFoodName(self):
		return self.__foodName
	
	
	def setFoodType(self,foodType):
		self.__foodType = foodType
	
	def getFoodType(self):
		return self.__foodType
	
	
	def setFoodCategory(self,foodCategory):
		self.__foodCategory = foodCategory
	
	def getFoodCategory(self):
		return self.__foodCategory
	
	
	def setFoodPrice(self,foodPrice):
		self.__foodPrice = foodPrice
	
	def getFoodPrice(self):
		return self.__foodPrice
	
	
	def setFoodDecription(self,foodDecription):
		self.__foodDecription = foodDecription
	
	def getFoodDecription(self):
		return self.__foodDescription
	
	
	def __str__(self):
		return "Food[Id:{}, Name:{},Type:{},Category:{},Price:{},Description:{}]".format(self.__foodId,
																						 self.__foodName,
																						 self.__foodType,
																						 self.__foodCategory,
																						 self.__foodPrice,
																						 self.__foodDescription)
	

class Customer:
	pass

class Cart:
	pass

class Order:
	pass