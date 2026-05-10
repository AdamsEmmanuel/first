from .models import (
    ServiceModel,
    TherapySessionModel as SessionModel,
    PractitionerModel
) 
from services.objects.core_objects import(
    Service,
    TherapySession as Session
)



class ServicesRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, details):
        specialists =self.session.query(PractitionerModel).filter(PractitionerModel.specialization == str(details['category'])).all() 
        record = ServiceModel(
            name=details['name'],
            short_description=details['short_description'],
            long_description=details['long_description'],
            price = details['price'],
            session_number=details['session_number'], 
            category=details['category'],
            duration=details['duration'],
            created=details['created'],         
        )
        record.specialists = specialists
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return Service(**record.dict(), service_=record)
    
        
    
    def _get(self,id_):
        return self.session.query(ServiceModel).filter(ServiceModel.service_id==str(id_)).first()
        
    def get(self, id_):
        service = self._get(id_)
        if service is not None:
            return Service(**service.dict()) 
        
    def get_available_specialists(self, id_):
        service =  self.session.query(ServiceModel).filter(ServiceModel.service_id==str(id_)).first()
        
        specialists_ids = [str(s.practitioner_id) for s in service.specialists]
        specialists_schedules = self.session.query(PractitionerModel).filter(PractitionerModel.schedules.in_(specialists_ids)).all()
        for schedule in specialists_schedules:
            self.session.query(SessionModel).filter(SessionModel.session_id == str(schedule.session_id)).first()
        
        #specialists_ids = self.session.query(ServiceModel.specialists).filter(ServiceModel.service_id==str(id_)).first()   
        #specialists_schedules = self.session.query(PractitionerModel.schedules).filter(PractitionerModel.practitioner_id.in_(specialists_ids)).all()        
        if service is not None:
            return Service(**service.dict())
       
        
    
    def list(self):
        def list(self, limit=None, **filters):
            query= self.session.query(ServiceModel)
            if 'created' in filters:
                created = filters.pop('created')
                if created:
                    query = query.filter(ServiceModel.created == created)
                else:
                    query = query.filter(ServiceModel.status != created)
                records = query.filter_by(**filters).limit(limit).all()
                return [Service(**record.dict()) for record in records]        
    
    def update(self, id_, **payload):
        record = self._get(id_)
        if name in payload:
            name = record.name                     
            self.session.delete(name)
            record.name = payload.pop('name')
        if short_description in payload:
            short_description = record.short_description                     
            self.session.delete(short_description)
            record.short_description = payload.pop('short_description')
        if long_description in payload:
            long_description = record.long_description                     
            self.session.delete(long_description)
            record.long_description = payload.pop('long_description')
        if price in payload:
            price = record.price                     
            self.session.delete(price)
            record.price = payload.pop('price')
        if session_number in payload:
            session_number = record.session_number                    
            self.session.delete(session_number)
            record.session_number = payload.pop('session_number')
        if category in payload:
            category = record.category                   
            self.session.delete(category)
            record.category= payload.pop('category') 
        if duration in payload:
            duration = record.duration                  
            self.session.delete(duration)
            record.duration = payload.pop('duration') 
        for key, value in payload.items():
            setattr(record, key, value)
        return Service(**record.dict())
    
    def delete(self, id_):
        self.session.delete(self._get(id_))    
        
            
        
class TherapySessionsRepository:
    def __init__(self, session):
        self.session = session

    def add(self, details):
        record = SessionModel(
            service_id =details['service_id '],
            title=details['title'],
            practitioner_id =details['practitioner_id '],
            patient_id = details['patient_id'],
            session_datetime=details['session_datetime'],
            duration=details['duration'], 
            status=details['status'], 
            clinical_notes=details['clinical'], 
            session_datetime=details['session_datetime'],             
        )
        
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return Session(**record.dict(), session_=record)
    
    def _get(self,id_):
        return self.session.query(SessionModel).filter(SessionModel.session_id == str(id_)).first()
        
    def get(self, id_):
        session = self._get(id_)
        if session is not None:
            return Session(**session.dict())    
    
    def list(self):
        def list(self, limit=None, **filters):
            query= self.session.query(SessionModel)
            if 'created' in filters:
                created = filters.pop('created')
                if created:
                    query = query.filter(SessionModel.created == created)
                else:
                    query = query.filter(SessionModel.status != created)
                records = query.filter_by(**filters).limit(limit).all()
                return [Session(**record.dict()) for record in records]        
    
    def update(self, id_, **payload):
        record = self._get(id_)
        if title in payload:
            title = record.title                     
            self.session.delete(title)
            record.title = payload.pop('title')
        if session_datetime in payload:
            session_datetime = record.session_datetime                     
            self.session.delete(session_datetime)
            record.session_datetime = payload.pop('session_datetime')
        if duration in payload:
            duration = record.duration                     
            self.session.delete(duration)
            record.duration = payload.pop('duration')    
        for key, value in payload.items():
            setattr(record, key, value)
        return Session(**record.dict())
    
    def delete(self, id_):
        self.session.delete(self._get(id_))    
        

