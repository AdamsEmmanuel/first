import requests

class User:
    def __init__(self, user_id, fullname, email, contact_info, created, role, user_ =None):
        self._user = user_
        self._user_id = user_id
        self.fullname = fullname
        self.contact_info = contact_info
        self.email = email
        self._role = role
        self._created = created
    @property
    def user_id(self):
        return self._user_id or self._user.user_id

    @property
    def created(self):
        return self._created or self._user.created    
    
    def role(self):
        return self._role or self._user.role
    def dict(self):
        return {
            'user_id': self.user_id,
            'fullname': self.fullname,
            'email': self.email,            
            'role': self.role,
            'contact_info': self.contact_info,
            'created': self.created          
             
        }
        
class Patient:
    def __init__(self, user_id, patient_id, DOB, gender, medical_history,
                 allergies,consent_id, bloodType, created, patient_=None):
        self._patient = patient_
        self.user_id = user_id
        self._patient_id = patient_id
        self.DOB = DOB
        self.gender = gender
        self.medical_history = medical_history
        self.allergies = allergies
        self.consent_id = consent_id
        self.bloodType = bloodType        
        self._created = created
    
    @property
    def patient_id(self):
        return self._patient_id or self._patient.patient_id

    @property
    def created(self):
        return self._created or self._patient.created
    
    def dict(self):
        return {
            'user_id': self.user_id,
            'patient_id': self.patient_id,
            'DOB': self.DOB,
            'gender': self.gender,
            'medical_history': self.medical_history,            
            'allergies': self.allergies,
            'consent_id': self.consent_id,
            'created': self.created          
             
        }
                
    def view_progress(self):
        pass               
    
    def get_meal_plans(self):
        pass
    
    def view_notifications(self):
        pass
    
        
class Practitioner:
    def __init__(self, user_id,  practitioner_id, DOB, gender, specialization, certification_number, verificationStatus, created, practitioner_):
        self._practitioner = practitioner_
        self.user_id = user_id
        self._practitioner_id = practitioner_id
        self.DOB = DOB
        self.gender = gender
        self.specialization = specialization
        self.certification_number = certification_number
        self.verificationStatus = verificationStatus
        self._created = created
    
    @property
    def practitioner_id(self):
        return self._practitioner_id or self._practitioner.practitioner_id

    @property
    def created(self):
        return self._created or self._practitioner.created        
    def dict(self):
        return {
            'user_id': self.user_id,
            'practitioner_id': self.practitioner_id,
            'DOB': self.DOB,
            'gender': self.gender,
            'specialization': self.specialization,            
            'certification_number': self.certification_number,
            'verificationStatus': self.verificationStatus,
            'created': self.created          
             
        }    
    
    def assess_patient(self):
        pass
    
    def create_diet_plan(self):
        pass
    
    def prescribe_therapy(self):
        pass
    
    def generate_report(self):
        pass      