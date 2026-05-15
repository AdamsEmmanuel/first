from .models import (
    FoodItemModel,
    DataModel,
    MealPlanModel
)
from services.objects.nutrition_objects import (
    FoodItem,
    MealPlanData,
    MealPlan
)

class FoodItemsRepository:
    def __init__(self, session):
        self.session = session
    def add(self, details):
        record = FoodItemModel(
            name = details['name'],
            portionSize = details['portionSize'],
            calories = details['calories'],
            protein = details['protein'],
            carbs = details['carbs'],
            fats = details['fats'],
            vitamins = details['vitamins'],
            image_url = details['image_url']             
        )
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return FoodItem(**record.dict(), foodItem_=record)

    def _get(self, id_):
        return self.session.query(FoodItemModel).filter(FoodItemModel.food_id==str(id_)).first()
    
    def get(self, id_):
        food_item = self._get(id_)
        if food_item is not None:
            return FoodItem(**food_item.dict()) 
        
    def list(self, limit=None, **filters):
        query= self.session.query(FoodItemModel)
        if 'created' in filters:
            created = filters.pop('created')
            if created:
                query = query.filter(FoodItemModel.created == created)
            else:
                query = query.filter(FoodItemModel.created != created)
            records = query.filter_by(**filters).limit(limit).all()
            return [FoodItem(**record.dict()) for record in records]
                
    def update(self, id_, **payload):
        pass
    
    
    def delete(self, id_):
        self.session.delete(self._get(id_)) 
        
         
class MealPlanDataRepository:
    def __init__(self, session):
        self.session = session
    def add(self, details):
        record = DataModel(
            mealplan_id = details['mealplan_id'],
            day = details['day'],
            breakfast = details['breakfast'],
            snack1 = details['snack1'],
            lunch = details['lunch'],
            snack2 = details['snack2'],
            dinner = details['dinner'],
            snack3 = details['snack3']
        )
        return MealPlanData(**record.dict(), data_=record)    

    def _get(self, id_):
        return self.session.query(DataModel).filter(DataModel.data_id==str(id_)).first()
    
    def get(self, id_):
        mealplan_data = self._get(id_)
        if mealplan_data is not None:
            return MealPlanData(**mealplan_data.dict()) 
        
    def list(self, limit=None, **filters):
        query= self.session.query(DataModel)
        if 'created' in filters:
            created = filters.pop('created')
            if created:
                query = query.filter(DataModel.created == created)
            else:
                query = query.filter(DataModel.created != created)
            records = query.filter_by(**filters).limit(limit).all()
            return [MealPlanData(**record.dict()) for record in records]        
    
    def update(self, id_, **payload):
        pass
    
    def delete(self, id_):
        self.session.delete(self._get(id_))
            
class MealPlansRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, details):
        record = MealPlanModel(
           title = details['title'],
           start_date = details['start_date'],
           end_date = details['end_date'],
           restrictions = details['restrictions'],
           notes = details['notes']
        )
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return MealPlan(**record.dict(), mealplan_=record)
    
    def _get(self, id_):
        return self.session.query(MealPlanModel).filter(MealPlanModel.data_id==str(id_)).first()
    
    def get(self, id_):
        mealplan = self._get(id_)
        if mealplan is not None:
            return MealPlan(**mealplan.dict()) 
        
    def list(self, limit=None, **filters):
        query= self.session.query(MealPlanModel)
        if 'created' in filters:
            created = filters.pop('created')
            if created:
                query = query.filter(MealPlanModel.created == created)
            else:
                query = query.filter(MealPlanModel.created != created)
            records = query.filter_by(**filters).limit(limit).all()
            return [MealPlanModel(**record.dict()) for record in records]        
       
    def update(self, id_, **payload):
        pass
    
    def delete(self, id_):
        self.session.delete(self._get(id_))  