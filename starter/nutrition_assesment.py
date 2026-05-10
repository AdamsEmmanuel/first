class NutritionAssessment:
    def __init__(self, assessmentId, date, weight, height, BMI, bodyFatPercentage, bloodsugar, bloodpressure):
        self.assessmentId = assessmentId
        self.date = date
        self.weight = weight 
        self.height = height
        self.BMI = BMI
        self.bodyFatPercentage = bodyFatPercentage
        self.bloodsugar = bloodsugar
        self.bloodpressure = bloodpressure
        
    def calculate_BMI(self):
        pass
    
    def compare_with_prev(self):
        pass
    
    def flag_abnormalites(self):
        pass    