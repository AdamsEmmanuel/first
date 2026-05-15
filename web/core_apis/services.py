from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import ServiceNotFoundError
from services.services.core_services import ServicesService
from repository.core_repository import ServicesRepository
from repository.unit_of_work import UnitOfWork

from web.schemas import (
    CreateServiceSchema,
    GetServiceSchema,
    GetServicesSchema
)


router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/", response_model=GetServicesSchema)
def get_services(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = ServicesRepository(unit_of_work.session)
        service_service = ServicesService(repo)
        results = service_service.list_services(limit=limit, created=created)      

    return { "services": [result.dict() for result in results]}



    
@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetServiceSchema)
def create_service(payload: CreateServiceSchema):
    with UnitOfWork() as unit_of_work:       
        repo = ServicesRepository(unit_of_work.session)        
        service_service = ServicesService(repo)
        service = payload.dict()        
        service = service_service.create_service(service)
        unit_of_work.commit()
        return_payload = service.dict()
    return return_payload


@router.get("/{service_id}" ,response_model=GetServiceSchema)
def get_service(service_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = ServicesRepository(unit_of_work.session)
            service_service = ServicesService(repo)            
            service = service_service.get_service(service_id=service_id)
        return service.dict()    
    except ServiceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Service with ID {service_id} not found"            
        ) 
                     
@router.get("/{service_id}/available_specialists" ,response_model=GetServiceSchema)
def get_service_available_specialists(service_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = ServicesRepository(unit_of_work.session)
            service_service = ServicesService(repo)            
            available_specialists = service_service.get_available_specialists(service_id=service_id)
        return { "availiable_specialists": [available_specialist.dict() for available_specialist in available_specialists]}    
    except ServiceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Service with ID {service_id} not found"            
        )              

@router.post("/{service_id}/enroll" ,response_model=GetServiceSchema)
def enroll_service(service_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = ServicesRepository(unit_of_work.session)
            service_service = ServicesService(repo)            
            service = service_service.enroll_service(service_id=service_id)
            unit_of_work.commit()
        return service.dict()    
    except ServiceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Service with ID {service_id} not found"            
        )               
    
          
@router.put("/{service_id}", response_model=GetServiceSchema)
def update_service(service_id: UUID, service_details: CreateServiceSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = ServicesRepository(unit_of_work.session)
            service_service = ServicesService(repo)            
            service = service_details.dict()
            service = service_service.update_service(service_id=service_id, payload=service)
            unit_of_work.commit()
        return service.dict()
    except ServiceNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'Service with ID {service_id} not found'
 )   
       
  

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_sevice(service_id: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = ServicesRepository(unit_of_work.session)
            service_service = ServicesService(repo)            
            service_service.delete_service(service_id=service_id)
            unit_of_work.commit()
        return 
    except ServiceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Service with ID {service_id} not found"            
        )              

        