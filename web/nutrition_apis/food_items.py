from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import FoodItemNotFoundError
from services.services.nutrition_services import FoodItemsService
from repository.nutrition_repository import FoodItemsRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreateFoodItemSchema,
    GetFoodItemSchema,
    GetFoodItemsSchema   
)
router = APIRouter(prefix="/foodItems", tags=["FoodItems"])


@router.get("/", response_model=GetFoodItemsSchema)
def get_foodItems(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = FoodItemsRepository(unit_of_work.session)
        fooditems_service = FoodItemsService(repo)
        results =  fooditems_service.list_foodItems(limit=limit, created=created)      
    return { "fooditems": [result.dict() for result in results]}



@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=GetFoodItemSchema)
def create_foodItem(payload: CreateFoodItemSchema):
    with UnitOfWork() as unit_of_work:       
        repo = FoodItemsRepository(unit_of_work.session)        
        fooditem_service = FoodItemsService(repo)
        fooditem = payload.dict()        
        fooditem = fooditem_service.create_foodItem(fooditem)
        unit_of_work.commit()
        return_payload = fooditem.dict()
    return return_payload

@router.get("/{foodItem_id}" ,response_model=GetFoodItemSchema)
def get_foodItem(foodItem_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = FoodItemsRepository(unit_of_work.session)
            foodItem_service = FoodItemsService(repo)            
            foodItem =foodItem_service.get_foodItem(foodItem_id=foodItem_id)
        return foodItem.dict()    
    except FoodItemNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"foodItem with ID {foodItem_id} not found"            
        )


router.put("/{foodItem_id}", response_model=GetFoodItemSchema)
def update_foodItem(foodItem_id: UUID, foodItem_details: CreateFoodItemSchema):
    try:
        with UnitOfWork() as unit_of_work:
            repo = FoodItemsRepository(unit_of_work.session)
            foodItem_service = FoodItemsService(repo)            
            foodItem = foodItem_details.dict()
            foodItem = foodItem_service.update_foodItem(foodItem_id=foodItem_id, payload=foodItem)
            unit_of_work.commit()
        return foodItem.dict()
    except FoodItemNotFoundError:       
        raise HTTPException(
 status_code=404, detail=f'foodItem with ID {foodItem_id} not found'
 )   
       
  

@router.delete("/{foodItem_id}", status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_foodItem(foodItem_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = FoodItemsRepository(unit_of_work.session)
            foodItem_service = FoodItemsService(repo)            
            foodItem_service.delete_foodItem(foodItem_id=foodItem_id)
            unit_of_work.commit()
        return 
    except FoodItemNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"foodItem with ID {foodItem_id} not found"            
        )              

                                                                                                                                     
         
