class MealPlan:
    def __init__(self, planId, startDate, endDate, dailyCalorieGoal, marconutrientsRatio, restrictions, notes):
        self.planId = planId
        self.startDate = startDate
        self.endDate = endDate
        self.dailyCarlorieGoal = dailyCalorieGoal
        self.marconutrientsRatio = marconutrientsRatio
        self.restrictions = restrictions
        self.notes = notes
        self.foodItems = []
    
    def add_meal(self):
        pass
    
    def modify_plan(self):
        pass
    
    def calculate_total_nutrients(self):
        pass
    
    def check_allergens(self):
        pass    
        