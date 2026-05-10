class MarcoNutrients:
    def __init__(self, carbs, protein, fats, vitamins):
        self.carbs = carbs
        self.protien = protein
        self.fats = fats
        self.vitamins =  vitamins

class FoodItem:
    def __init__(self, foodId, name,portionSize, calories, isAllergen: bool):
        self.foodId = foodId
        self.name = name
        self.portionSize = portionSize
        self.calories = calories
        self.marconurtients = []
        self.isAllergen = isAllergen        

    def getNutritionalValue(self):
        pass
    
    def updatePortion(self):
        pass
    
        