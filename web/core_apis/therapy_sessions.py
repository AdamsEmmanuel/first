from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import TherapySessionNotFoundError as SessionNotFoundError
from services.services.core_services import TherapySessionsService as SessionsService
from repository.core_repository import TherapySessionsRepository as SessionsRepository
from repository.unit_of_work import UnitOfWork

from web.schemas import (
    CreateTherapySessionSchema as CreateSessionSchema,
    GetTherapySessionSchema as GetSessionSchema,
    GetTherapySessionsSchema as GetSessionsSchema
)

router = APIRouter(prefix="/sessions", tags=["Sessions"])

@router.get("/", response_model=GetSessionsSchema)
def get_sessions(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = SessionsRepository(unit_of_work.session)
        session_service = SessionsService(repo)
        results = session_service.list_sessions(limit=limit, created=created)      

    return { "sessions": [result.dict() for result in results]}



@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetSessionSchema)
def create_service(payload: CreateSessionSchema):
    with UnitOfWork() as unit_of_work:       
        repo = SessionsRepository(unit_of_work.session)        
        session_service = SessionsService(repo)
        session = payload.dict()        
        session = session_service.create_session(session)
        unit_of_work.commit()
        return_payload = session.dict()
    return return_payload


@router.get("/{session_id}" ,response_model=GetSessionSchema)
def get_session(session_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = SessionsRepository(unit_of_work.session)
            session_service = SessionsService(repo)            
            session = session_service.get_session(session_id=session_id)
        return session.dict()    
    except SessionNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Session with ID {session_id} not found"            
        ) 
        

@router.put("/{session_id}", response_model=GetSessionSchema)
def update_session(session_id: UUID, session_details: CreateSessionSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = SessionsRepository(unit_of_work.session)
            session_service = SessionsService(repo)            
            session = session_details.dict()
            session = session_service.update_session(session_id=session_id, payload=session)
            unit_of_work.commit()
        return session.dict()
    except SessionNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'Session with ID {session_id} not found'
 )   
       
  

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_session(session_id: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = SessionsRepository(unit_of_work.session)
            session_service = SessionsService(repo)            
            session_service.delete_session(session_id=session_id)
            unit_of_work.commit()
        return 
    except SessionNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Session with ID {session_id} not found"            
        )              

        
