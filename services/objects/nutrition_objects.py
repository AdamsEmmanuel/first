import requests

class FoodItem:
    def __init__(self, food_id, name, portionSize, calories, protein, carbs, fats, vitamins, isAllergen: bool, image_url,created, foodItem_ = None):
        self ._foodItem = foodItem_
        self._food_id = food_id
        self.name = name
        self.portionSize = portionSize
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.vitamins =  vitamins
        self.isAllergen = isAllergen
        self.image_url = image_url
        self._created = created
    @property
    def food_id(self):
        return self._food_id or self._foodItem.food_id

    @property
    def created(self):
        return self._created or self._foodItem.created
    
    def dict(self):
        return {
            'food_id': self.food_id,
            'name': self.name,
            'portionSize': self.portionSize,            
            'protein': self.protein,
            'carbs': self.carbs,
            'fats': self.fats,
            'vitamins': self.vitamins,
            'image_url': self.image_url,
            'created': self.created                      
        }                      

    def getNutritionalValue(self):
        pass
    
    def updatePortion(self):
        pass

class MealPlanData:
    def __init__(self, data_id, mealplan_id, day, breakfast, snack1, lunch, snack2, dinner, snack3, created, data_=None) -> None:
        self. _data = data_
        self._data_id = data_id
        self.mealplan_id = mealplan_id
        self.day = day
        self.breakfast = breakfast
        self.snack1 = snack1
        self.lunch = lunch
        self.snack2 =snack1
        self.dinner = dinner
        self.snack3 = snack3
        self._created = created
    
    @property
    def data_id(self):
        return self._data_id or self._data.data_id

    @property
    def created(self):
        return self._created or self._data.created  

    def dict(self):
        return {
            'data_id': self.data_id,
            'mealplan_id': self.mealplan_id,
            'day': self.day,            
            'breakfast': self.breakfast,
            'snack1': self.snack1,
            'lunch': self.lunch,
            'snack2': self.snack2,
            'dinner': self.dinner,
            'snack3': self.snack3,
            'created': self.created          
             
        }
   
        

class MealPlan:
    def __init__(self, mealplan_id, title, start_date, end_date, restrictions, notes,created, mealplan_= None):
        self._mealplan = mealplan_
        self._mealplan_id = mealplan_id
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        #self.dailyCarlorieGoal = dailyCalorieGoal
        #self.marconutrientsRatio = marconutrientsRatio
        self.restrictions = restrictions
        self.notes = notes
        self._created = created
    @property
    def mealplan_id(self):
        return self._mealplan_id or self._mealplan.service_id

    @property
    def created(self):
        return self._created or self._mealplan.created 
    
    def dict(self):
        return {
            'mealplan_id': self.mealplan_id,
            'title': self.title,
            'start_date': self.start_date,            
            'end_date': self.end_date,
            'restrictions': self.restrictions,
            'notes': self.notes,
            'created': self.created          
             
        }   
    
    def add_meal(self):
        pass
    
    def modify_plan(self):
        pass
    
    def calculate_total_nutrients(self):
        pass
    
    def check_allergens(self):
        pass    
            