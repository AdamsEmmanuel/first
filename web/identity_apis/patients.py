from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
import json
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import PatientNotFoundError
from services.services.identity_services import PatientsService
from repository.identity_repository import PatientsRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreatePatientSchema,
    GetPatientSchema,
    GetPatientsSchema

)


router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/", response_model=GetPatientsSchema)
def get_patients(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = PatientsRepository(unit_of_work.session)
        patient_service = PatientsService(repo)
        results = patient_service.list_patients(limit=limit, created=created)      

    return { "users": [result.dict() for result in results]}
    
@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetPatientSchema)
def create_user(payload: CreatePatientSchema):
    with UnitOfWork() as unit_of_work:       
        repo = PatientsRepository(unit_of_work.session)        
        patient_service = PatientsService(repo)
        patient = payload.dict()        
        patient = patient_service.create_patient(patient)
        unit_of_work.commit()
        return_payload = patient.dict()
    return return_payload



@router.get("/{user_id}" ,response_model=GetPatientSchema)
def get_atient(patient_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = PatientsRepository(unit_of_work.session)
            patient_service = PatientsService(repo)            
            patient = patient_service.get_patient(patient_id=patient_id)
        return patient.dict()    
    except PatientNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Patient with ID {patient_id} not found"            
        )              
          
@router.put("/{patient_id}", response_model=GetPatientSchema)
def update_profile(patient_id: UUID, patient_details: CreatePatientSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = PatientsRepository(unit_of_work.session)
            patient_service = PatientsService(repo)            
            patient = patient_details.dict()
            patient = patient_service.update_patient(patient_id=patient_id, payload=patient)
            unit_of_work.commit()
        return patient.dict()
    except PatientNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'Patient with ID {patient_id} not found'
 )   
       
  

@router.delete("/{patientId}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_user(patientId: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = PatientsRepository(unit_of_work.session)
            patient_service = PatientsService(repo)            
            patient_service.delete_patient(patient_id=patientId)
            unit_of_work.commit()
        return 
    except PatientNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Patient with ID {patientId} not found"            
        )              


