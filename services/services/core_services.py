from repository.core_repository import (
    ServicesRepository,
    TherapySessionsRepository as SessionRepo
)
from services.exceptions import (
    ServiceNotFoundError,
    TherapySessionNotFoundError
)

class ServicesService:
    def __init__(self, service_repository: ServicesRepository):
        self.service_repository = service_repository

    def create_service(self, details):
        return self.service_repository.add(details) 
    
    def get_service(self, service_id):
        service = self.service_repository.get(service_id)
        if service is not None :
            return service
        raise ServiceNotFoundError(f'Service with id {service_id} not found')
    
    def list_services(self, **filters):
        limit = filters.pop('limit', None)
        return self.service_repository.list(limit, **filters) 

    def update_service(self, service_id, **payload):
        service = self.service_repository.get(service_id)
        if service is None:
            raise ServiceNotFoundError(f'Service with id {service_id} not found')
        return self.service_repository.update(service_id, **payload)
    
    def delete_service(self, service_id):
        service = self.service_repository.get(service_id)
        if service is None:
            raise ServiceNotFoundError(f'Service with id {service_id} not found')
        return self.service_repository.delete(service_id)
    def get_available_specialists(self, service_id):
        available_specialists = self.service_repository.get_available_specialists(service_id)
        if available_specialists is not None :
            return available_specialists
        raise ServiceNotFoundError(f'No Available specialists for service with id {service_id} found')
    def enroll_service(self, service_id):
        service = self.service_repository.get(service_id)
        if service is None:
            raise ServiceNotFoundError(f'Service with id {service_id} not found')
        #add to patients enrolled services
        #send  request notification to selected avilable specialist
        return self.service_repository.delete(service_id)

class TherapySessionsService:
    def __init__(self,session_repository: SessionRepo):
        self.session_repository = session_repository   
    
    def create_session(self, details):
        return self.session_repository.add(details)
    
    def get_sesion(self, session_id):
        session = self.session_repository.get(session_id)
        if session is not None :
            return session
        raise TherapySessionNotFoundError(f'Session with id {session_id} not found') 
    
    def list_sessions(self, **filters):
        limit = filters.pop('limit', None)
        return self.session_repository.list(limit, **filters) 
    
    def update_session(self, session_id, **payload):
        session = self.session_repository.get(session_id)
        if session is None:
            raise TherapySessionNotFoundError(f'Session with id {session_id} not found')
        return self.session_repository.update(session_id, **payload)
    
    def delete_session(self,session_id):
        session = self.session_repository.get(session_id)
        if session is None:
            raise TherapySessionNotFoundError(f'Session with id {session_id} not found')
        return self.session_repository.delete(session_id)
       
    
