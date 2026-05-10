from repository.identity_repository import(
    UsersRepository,
    PatientsRepository,
    PractitionersRepository
 )
from services.exceptions import(
    UserNotFoundError,
    PatientNotFoundError,
    PractitionerNotFoundError
)

class UsersService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository
    def create_user(self, details):
        return self.user_repository.add(details)
        
        
    def get_user(self, user_id):
        user = self.user_repository.get(user_id)
        if user is not None :
            return user
        raise UserNotFoundError(f'User with id {user_id} not found')
    
    def list_users(self, **filters):
        limit = filters.pop('limit', None)
        return self.user_repository.list(limit, **filters) 
    
    def update_user(self, user_id, **payload):
        user = self.user_repository.get(user_id)
        if user is None:
            raise UserNotFoundError(f'User with id {user_id} not found')
        return self.user_repository.update(user_id, **payload)
    def delete_user(self, user_id):
        user = self.user_repository.get(user_id)
        if user is None:
            raise UserNotFoundError(f'User with id {user_id} not found')
        return self.user_repository.delete(user_id)
               

class PatientsService:
    def __init__(self, patient_repository: PatientsRepository):
        self.patient_repository = patient_repository
    
    def create_patient(self, details):
        self.patient_repository.add(details)
    
    def get_patient(self, patient_id):
        patient = self.patient_repository.get(patient_id)  
        if patient is not None:
            return patient 
        raise PatientNotFoundError(f'Paient with id {patient_id} not found')  

    def update_patient_profile(self, patient_id, **payload):
        patient = self.patient_repository.get(patient_id)
        if patient is None:
            raise PatientNotFoundError(f'Paient with id {patient_id} not found')  
        return self.patient_repository.update(patient_id, **payload)
    
    def list_patients(self, **filters):
        limit = filters.pop('limit', None)
        return self.patient_repository.list(limit,**filters)
    
    def update_allergies(self, patient_id, **payload):
        patient = self.patient_repository.get(patient_id)  
        if patient is None:
            raise PatientNotFoundError(f'Paient with id {patient_id} not found')              
        return self.patient_repository.update_allergies(patient_id, **payload)  
    
    def delete_patient(self, patient_id):
        patient = self.patient_repository.get(patient_id)
        if patient is None:
            raise PatientNotFoundError(f'Paient with id {patient_id} not found')  
        return self.patient_repository.delete(patient_id)    
    
    
class PractitionersService:
    def __init__(self, practitioner_repository: PractitionersRepository):
        self.practitioner_repository = practitioner_repository
        
    def create_practitioner(self, details):
        self.practitioner_repository.add(details)
    
    def get_practitioner(self,practitioner_id):
        practitioner = self.practitioner_repository.get(practitioner_id)
        if practitioner is not None:
            return practitioner
        raise PractitionerNotFoundError(f'Practitioner with id {practitioner_id} not found')            
        
    def list_practitioners(self, **filters):
        limit = filters.pop('limit', None)
        return self.practitioner_repository.list(limit, **filters)
    

    def delete_practitioner(self, practitioner_id):
        order = self.practitioner_repository.get(practitioner_id)
        if order is None:
            raise PractitionerNotFoundError(f'Practitioner with id {practitioner_id} not found')
        return self.practitioner_repository.delete(practitioner_id)