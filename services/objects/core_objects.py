import requests
class Service:
    def __init__(self, service_id,name, short_description, long_description, price, session_numder,
                 category, duration, created, service_=None):
        self._service = service_
        self._service_id = service_id
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.price = price
        self.session_number = session_numder
        self.category = category
        self.duration = duration
        self._created = created
    @property
    def service_id(self):
        return self._service_id or self._service.service_id

    @property
    def created(self):
        return self._created or self._service.created    
    
    def dict(self):
        return {
            'service_id': self.service_id,
            'name': self.name,
            'short_description': self.short_description,            
            'long_description': self.long_description,
            'price': self.price,
            'session_number': self.session_number,
            'category': self.category,
            'duration': self.duration,
            'created': self.created               
        }

class TherapySession:
    def __init__(self, session_id, service_id, title, patient_id, practitioner_id, datetime, duration,clinical_notes,status, created, session_=None):
        self._session = session_
        self._session_id = session_id
        self.service_id = service_id
        self.patient_id = patient_id
        self.practitioner_id = practitioner_id
        self.title = title
        self.session_datetime = datetime
        self.duration = duration
        self.clinical_notes = clinical_notes
        self.status = status
        self._created = created
    @property
    def session_id(self):
        return self._session_id or self._session.session_id

    @property
    def created(self):
        return self._created or self._session.created 
    def dict(self):
        return {
            'session_id': self.session_id,
            'service_id': self.service_id,
            'title': self.title,
            'patient_id': self.patient_id,
            'practitioner_id': self.practitioner_id,
            'session_datetime': self.session_datetime,
            'duration': self.duration,            
            'status': self.status,
            'clinical_notes': self.clinical_notes,
            'created': self.created              
        }
    def schedule(self):
        pass
        
    def reschedule(self,details):
        pass
    
    def cancel(self):
        pass
    
    def log_outcome(self):
        pass
        