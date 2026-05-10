from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
import json
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import UserNotFoundError
from services.services.identity_services import UsersService
from repository.identity_repository import UsersRepository
from repository.unit_of_work import UnitOfWork

from web.schemas import (
    CreateUserSchema,
    GetUserSchema,
    GetUsersSchema

)


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=GetUsersSchema)
def get_users(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = UsersRepository(unit_of_work.session)
        user_service = UsersService(repo)
        results = user_service.list_users(limit=limit, created=created)      

    return { "users": [result.dict() for result in results]}
    
@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetUserSchema)
def create_user(payload: CreateUserSchema):
    with UnitOfWork() as unit_of_work:       
        repo = UsersRepository(unit_of_work.session)        
        user_service = UsersService(repo)
        user = payload.dict()        
        user = user_service.create_user(user)
        unit_of_work.commit()
        return_payload = user.dict()
    return return_payload



@router.get("/{user_id}" ,response_model=GetUserSchema)
def get_user(user_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = UsersRepository(unit_of_work.session)
            user_service = UsersService(repo)            
            user = user_service.get_user(user_id=user_id)
        return user.dict()    
    except UserNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"            
        )              
          
@router.put("/{user_id}", response_model=GetUserSchema)
def update_profile(user_id: UUID, user_details: CreateUserSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = UsersRepository(unit_of_work.session)
            user_service = UsersService(repo)            
            user = user_details.dict()
            user = user_service.update_user(user_id=user_id, payload=user)
            unit_of_work.commit()
        return user.dict()
    except UserNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'User with ID {user_id} not found'
 )   
       
  

@router.delete("/{userId}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_user(userId: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = UsersRepository(unit_of_work.session)
            user_service = UsersService(repo)            
            user_service.delete_user(user_id=userId)
            unit_of_work.commit()
        return 
    except UserNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"User with ID {userId} not found"            
        )              

    







    