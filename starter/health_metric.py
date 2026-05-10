from enum import Enum

class MetricType(Enum):
    water_intake = 'water_intake'
    sleepHours = 'sleepHours'
    mood = 'mood'
    blood_glucose = 'blood_glucose'
    steps = 'steps'
 
class HealtMetric:
    def __init__(self, metricId, patientId, metricType, value, unit, entryDate):
        self.metricId = metricId
        self.patientId = patientId
        self.metricType = MetricType(metricType)
        self.value = value
        self.unit = unit
        self.entryDate = entryDate
    
    
    def validate_range(self):
        pass
    
    def get_weekly_average(self):
        pass
    
    def check_threshold(self):
        pass


       