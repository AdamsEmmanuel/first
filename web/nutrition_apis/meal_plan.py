from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import MealPlanNotFoundError
from services.services.nutrition_services import MealPlansService
from repository.nutrition_repository import MealPlansRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreateMealPlanSchema,
    GetMealPlanSchema,
    GetMealPlansSchema   
)
router = APIRouter(prefix="/mealplans", tags=["MealPlans"])


@router.get("/", response_model=GetMealPlansSchema)
def get_mealplans(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = MealPlansRepository(unit_of_work.session)
        mealplan_service = MealPlansService(repo)
        results = mealplan_service.list_mealplans(limit=limit, created=created)      
    return { "mealplans": [result.dict() for result in results]}


@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetMealPlanSchema)
def create_mealplan(payload: CreateMealPlanSchema):
    with UnitOfWork() as unit_of_work:       
        repo = MealPlansRepository(unit_of_work.session)        
        mealplan_service = MealPlansService(repo)
        mealplan = payload.dict()        
        mealplan = mealplan_service.create_mealplan(mealplan)
        unit_of_work.commit()
        return_payload = mealplan.dict()
    return return_payload

@router.get("/{mealplan_id}" ,response_model=GetMealPlanSchema)
def get_mealplan(mealplan_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = MealPlansRepository(unit_of_work.session)
            mealplan_service = MealPlansService(repo)            
            mealplan = mealplan_service.get_mealplan(mealplan_id=mealplan_id)
        return mealplan.dict()    
    except MealPlanNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Mealplan with ID {mealplan_id} not found"            
        )


router.put("/{mealplan_id}", response_model=GetMealPlanSchema)
def update_mealplan(mealplan_id: UUID, mealplan_details: CreateMealPlanSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = MealPlansRepository(unit_of_work.session)
            mealplan_service = MealPlansService(repo)            
            mealplan = mealplan_details.dict()
            mealplan = mealplan_service.update_mealplan(mealplan_id=mealplan_id, payload=mealplan)
            unit_of_work.commit()
        return mealplan.dict()
    except MealPlanNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'Mealplan with ID {mealplan_id} not found'
 )   
       
  

@router.delete("/{mealplan_id}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_mealplan(mealplan_id: UUID):
    
    try:
        with UnitOfWork() as unit_of_work:
            repo = MealPlansRepository(unit_of_work.session)
            mealplan_service = MealPlansService(repo)            
            mealplan_service.delete_mealplan(mealplan_id=mealplan_id)
            unit_of_work.commit()
        return 
    except MealPlanNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Mealplan with ID {mealplan_id} not found"            
        )              

                                                                                                                                     
         