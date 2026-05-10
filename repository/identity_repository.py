from .models import (
    UserModel, 
    PatientModel, 
    PractitionerModel,
    ServiceModel 
   
)
from services.objects.identity_objects import (
    User,
    Patient,
    Practitioner
) 
class UsersRepository:
    def __init__(self, session):
        self.session = session
        
    def add(self, details):
        record = UserModel(
            fullname=details['fullname'],
            email=details['email'],
            password=details['password'],
            contact_info = details['contact_info'],
            role=details['role']             
        )
        
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return User(**record.dict(), user_=record)
    
    def _get(self,id_):
        return self.session.query(UserModel).filter(UserModel.user_id == str(id_)).first()
        
    def get(self, id_):
        user = self._get(id_)
        if user is not None:
            return User(**user.dict())    
    
    def list(self):
        def list(self, limit=None, **filters):
            query= self.session.query(UserModel)
            if 'created' in filters:
                created = filters.pop('created')
                if created:
                    query = query.filter(UserModel.created == created)
                else:
                    query = query.filter(UserModel.status != created)
                records = query.filter_by(**filters).limit(limit).all()
                return [User(**record.dict()) for record in records]        
    
    def update(self, id_, **payload):
        record = self._get(id_)
        if name in payload:
            name = record.name                     
            self.session.delete(name)
            record.name = payload.pop('name')
        if email in payload:
            email = record.email                     
            self.session.delete(email)
            record.email = payload.pop('email')
        if contact_info in payload:
            contact_info = record.contact_info                     
            self.session.delete(contact_info)
            record.contact_info = payload.pop('contact_info')    
        for key, value in payload.items():
            setattr(record, key, value)
        return User(**record.dict())
    
    def delete(self, id_):
        self.session.delete(self._get(id_))    
        
class PatientsRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, details):
        record = PatientModel(
            user_id=details['user_id'],
            DOD=details['DOB'],
            gender=details['gender'],
            medical_history=details['medical_history'],
            allergies=details['allergies']         
        )
        #ordered_services_ids = [str(s.service_id) for s in details['orderd_services_id']]
        #ordered_services = self.session.query(ServiceModel).filter(ServiceModel.service_id.in_(ordered_services_ids)).all()
        #record.ordered_services = ordered_services
        
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return Patient(**record.dict(), patient_=record)  
    
    def _get(self,id_):
        return self.session.query(PatientModel).filter(PatientModel.patient_id == str(id_)).first()
    
    def get(self, id_):
        patient = self._get(id_)
        if patient is not None:
            return Patient(**patient.dict())
    

    def list(self, limit=None, **filters):
        query= self.session.query(PatientModel)
        if 'created' in filters:
            created = filters.pop('created')
            if created:
                query = query.filter(PatientModel.created == created)
            else:
                query = query.filter(PatientModel.status != created)
            records = query.filter_by(**filters).limit(limit).all()
            return [Patient(**record.dict()) for record in records]        
        
    def update(self, id_, **payload):
        record = self._get(id_)
        if DOB in payload:
            DOB = record.DOB                     
            self.session.delete(DOB)
            record.DOB = payload.pop('DOB')
        if gender in payload:
            gender = record.gender                     
            self.session.delete(gender)
            record.gender = payload.pop('gender')
        if medical_history in payload:
            medical_history = record.medical_history                     
            self.session.delete(medical_history)
            record.medical_history = payload.pop('medical_history')
        for key, value in payload.items():
            setattr(record, key, value)
        return User(**record.dict())
    
    
    def delete(self, id_):
        self.session.delete(self._get(id_))
                
        
class PractitionersRepository:
    def __init__(self, session):
        self.session = session
        
    def add(self, details):
        record = PractitionerModel(
            user_id=details['user_id'],
            DOB=details['DOB'],
            gender=details['gender'],
            specialization=details['specialization'],
            certification_number=details['certification_number']           
        )
        services = self.session.query(ServiceModel).filter(ServiceModel.category==str(details['specialization'])).all()
        if services is not None:
            for service in services:
                service.specialists = [record]
            
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return Practitioner(**record.dict(), practitioner_=record)
    
    def _get(self,id_):
        return self.session.query(PractitionerModel).filter(PractitionerModel.practitioner_id == str(id_)).first()
    
    def get(self, id_):
        practitioner = self._get(id_)
        if practitioner is not None:
            return Practitioner(**practitioner.dict())
        
    

    def list(self, limit=None, **filters):
        query= self.session.query(PractitionerModel)
        if 'created' in filters:
            created = filters.pop('created')
            if created:
                query = query.filter(PractitionerModel.created == created)
            else:
                query = query.filter(PractitionerModel.status != created)
            records = query.filter_by(**filters).limit(limit).all()
            return [Practitioner(**record.dict()) for record in records]    
        
    def update(self, id_, **payload):
        record = self._get(id_)
        if specialization in payload:
            specialization = record.specialization                     
            self.session.delete(specialization)
            record.specialization = payload.pop('specialization')
        for key, value in payload.items():
            setattr(record, key, value)
        return PractitionerModel(**record.dict()) 
    
    
    def delete(self, id_):
        self.session.delete(self._get(id_))            