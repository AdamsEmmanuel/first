from repository.nutrition_repository import(
    FoodItemsRepository,
    MealPlanDataRepository as DataRepo,
    MealPlansRepository 
)
from services.exceptions import (
    FoodItemNotFoundError,
    MealPlanDataNotFoundError,
    MealPlanNotFoundError 
)


class FoodItemsService:
    def __init__(self, foodItem_repository: FoodItemsRepository) -> None:
        self.foodItem_repository = foodItem_repository
        
    def create_foodItem(self, details):
        return self.foodItem_repository.add(details)
    
    def get_foodItem(self, foodItem_id):
        foodItem = self.foodItem_repository.get(foodItem)
        if foodItem is not None:
            return foodItem
        raise FoodItemNotFoundError(f'FoodItem  with id {foodItem_id}')
    def list_foodItems(self, **filters):
        limit = filters.pop('limit', None)
        return self.foodItem_repository.list(limit, **filters)
    
    def update_foodItem(self, foodItem_id, **payload):
        foodItem = self.foodItem_repository.get(foodItem_id)
        if foodItem is None:
            raise FoodItemNotFoundError(f'FoodItem with id {foodItem_id} not found')
        return self.foodItem_repository.update(foodItem_id, **payload)  
    
    def delete_foodItem(self, foodItem_id):
        foodItem = self.foodItem_repository.get(foodItem_id)
        if foodItem is None:
            raise FoodItemNotFoundError(f'FoodItem with id {foodItem_id} not found')
        return self.foodItem_repository.delete(foodItem_id)  
            
class MealPlanDataService:
    def __init__(self, data_repository: DataRepo) -> None:
        self.data_repository = data_repository
    
    def create_mealplandata(self, details):
        return self.data_repository.add(details)
    
    def get_mealplan_data(self, mealplan_id):
        mealplan_data = self.data_repository.get(mealplan_id)
        if mealplan_data is not None:
            return mealplan_data
        raise MealPlanDataNotFoundError(f'Data for Mealplan with id {mealplan_id} not found') 
    
    def update_mealplan_data(self, mealplan_id, **payload):
        mealplan_data = self.data_repository.get(mealplan_id)
        if mealplan_data is None:
            raise MealPlanDataNotFoundError(f'Data for Mealplan with id {mealplan_id} not found')
        return self.data_repository.update(mealplan_id, **payload)

    def delete_mealplan_data(self, mealplan_id):
        mealplan_data = self.data_repository.get(mealplan_id)
        if mealplan_data is None:
            raise MealPlanDataNotFoundError(f'Data for Mealplan with id {mealplan_id} not found')
        return self.data_repository.delete(mealplan_id)

    
class MealPlansService:
    def __init__(self, mealplan_repository: MealPlansRepository) -> None:
        self.mealplan_repository = mealplan_repository
    
    def create_mealplan(self, details):
        return self.mealplan_repository.add(details)    

    def get_mealplan(self, mealplan_id):
        mealplan = self.mealplan_repository.get(mealplan_id)
        if mealplan is not None:
            return  mealplan
        raise MealPlanNotFoundError(f'Mealplan with id {mealplan_id}')
    
    def list_mealplans(self, **filters):
        limit = filters.pop('limit', None)
        return self.mealplan_repository.list(limit, **filters)
    
    def update_mealplan(self, mealplan_id, **payload):
        mealplan = self.mealplan_repository.get(mealplan_id)
        if mealplan is None:
            raise MealPlanNotFoundError(f'Mealplan with id {mealplan_id} not found')
        return self.mealplan_repository.update(mealplan_id, **payload)
    
    def delete_mealplan(self, mealplan_id):
        mealplan = self.mealplan_repository.get(mealplan_id)
        if mealplan is None:
            raise MealPlanDataNotFoundError(f'Mealplan with id {mealplan_id} not found')
        return self.mealplan_repository.delete(mealplan_id)     