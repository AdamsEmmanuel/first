import uuid
from datetime import datetime
from enum import Enum

class ConsentStatus(Enum):
    pending = 'pending'
    active = 'active'
    partial = 'partial'
    revorked = 'revorked'
    expired = 'expired'
    

class User:
    def __init__(self, fullname, email, contact_info, created):
        self.userId = uuid.uuid1()
        self.fullname = fullname
        self.contact_info = contact_info
        self.email = email
        self.created = created

    def register(details):
        pass
    
    def update_profile():
        pass          
class Patient:
    def __init__(self, patientId, DOB, gender, medical_history,
                 allergies,consentStatus,bloodType):
        self.patientId = patientId
        self.DOB = DOB
        self.gender = gender
        self.medical_history = medical_history
        self.allergies = allergies
        self.consentStatus = ConsentStatus(consentStatus)
        self.bloodType = bloodType        
    
    def view_progress(self):
        pass               
    
    def get_meal_plans(self):
        pass
        
class Practitioner:
    def __init__(self, staffId, specialization, certification_number):
        self.staffId = staffId
        self.specialization = specialization
        self.certification_number = certification_number
        self.schedules = []
        self.assigned_patients = []
    
    def assess_patient(self):
        pass
    
    def create_diet_plan(self):
        pass
    
    def prescribe_therapy(self):
        pass
    
    def generate_report(self):
        pass      