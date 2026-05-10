from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
import json
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import PractitionerNotFoundError
from services.services.identity_services import PractitionersService
from repository.identity_repository import PractitionersRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreatePractitionerSchema,
    GetPractitionerSchema,
    GetPractitionersSchema   
)
router = APIRouter(prefix="/practitioners", tags=["Practitioners"])

@router.get("/", response_model=GetPractitionerSchema)
def get_practitioners(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = PractitionersRepository(unit_of_work.session)
        diary_service = PractitionersService(repo)
        results = diary_service.list_practitioners(limit=limit, created=created)      

    return { "practitioners": [result.dict() for result in results]}



@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetPractitionerSchema)
def create_practitioner(payload: CreatePractitionerSchema):
    with UnitOfWork() as unit_of_work:       
        repo = PractitionersRepository(unit_of_work.session)        
        practitioner_service = PractitionersService(repo)
        practitioner = payload.dict()
        practitioner = practitioner_service.create_practitioner(practitioner)
        unit_of_work.commit()
        return_payload = practitioner.dict()
    return return_payload

@router.get("/{practitioner_id}" ,response_model=GetPractitionerSchema)
def get_practitioner(practitioner_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = PractitionersRepository(unit_of_work.session)
            practitioner_service = PractitionersService(repo)            
            practitioner = practitioner_service.get_practitioner(practitioner_id=practitioner_id)
        return practitioner.dict()    
    except PractitionerNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"practitioner with ID {practitioner_id} not found"            
        )  

@router.put("/{practitioner_id}", response_model=GetPractitionerSchema)
def update_practitioner_profile(practitioner_id: UUID, practitioner_details: CreatePractitionerSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = PractitionersRepository(unit_of_work.session)
            practitioner_service = PractitionersService(repo)            
            practitioner = practitioner_details.dict()
            practitioner = practitioner_service.update_practitioner(practitioner_id=practitioner_id, payload=practitioner)
            unit_of_work.commit()
        return practitioner.dict()
    except PractitionerNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'Practitioner with ID {practitioner_id} not found'
 )   

@router.delete("/{practitionerId}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_practitioner(practitionerId: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = PractitionersRepository(unit_of_work.session)
            practitioner_service = PractitionersService(repo)            
            practitioner_service.delete_practitioner(practitioner_id=practitionerId)
            unit_of_work.commit()
        return 
    except PractitionerNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Practitioner with ID {practitionerId} not found"            
        )          
    